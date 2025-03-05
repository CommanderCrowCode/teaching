import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from datasets import load_dataset
import librosa
import numpy as np
import argparse
import sys
import os

def transcribe_audio(audio_path, model_name="openai/whisper-large-v2"):
    """
    Transcribe an audio file using the Whisper model.
    
    Args:
        audio_path (str): Path to the audio file
        model_name (str): Name of the Whisper model to use
        
    Returns:
        str: Transcribed text
    """
    print("Loading model and processor...")
    processor = WhisperProcessor.from_pretrained(model_name)
    model = WhisperForConditionalGeneration.from_pretrained(model_name)
    
    # Check if GPU is available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    model = model.to(device)
    
    # Load and preprocess the audio file
    print("Processing audio file...")
    
    # Get the audio duration first
    audio_duration = librosa.get_duration(filename=audio_path)
    print(f"Audio duration: {audio_duration:.2f} seconds")
    
    # Process audio in chunks if it's long
    chunk_length = 30 * 16000  # 30 seconds chunks
    transcription = []
    
    for offset in range(0, int(audio_duration * 16000), chunk_length):
        end_offset = min(offset + chunk_length, int(audio_duration * 16000))
        print(f"Processing chunk {offset//chunk_length + 1}...")
        
        # Load audio chunk
        audio_chunk, _ = librosa.load(audio_path, sr=16000, offset=offset/16000, 
                                    duration=(end_offset-offset)/16000)
        
        # Convert audio to float32 if needed
        if audio_chunk.dtype != np.float32:
            audio_chunk = audio_chunk.astype(np.float32)
        
        # Create input features
        input_features = processor(
            audio_chunk,
            sampling_rate=16000,
            return_tensors="pt"
        ).input_features
        
        # Move input to the same device as model
        input_features = input_features.to(device)
        
        # Generate token ids
        predicted_ids = model.generate(input_features)
        
        # Decode the token ids to text
        chunk_transcription = processor.batch_decode(
            predicted_ids, 
            skip_special_tokens=True
        )[0]
        
        transcription.append(chunk_transcription.strip())
    
    # Join all chunks with proper spacing
    return ' '.join(transcription)

def save_transcript(audio_path, transcription):
    """
    Save the transcription to a text file with the same name as the audio file.
    
    Args:
        audio_path (str): Path to the original audio file
        transcription (str): The transcribed text
    
    Returns:
        str: Path to the saved transcript file
    """
    # Get the base filename without extension
    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    # Create output filename in current directory
    output_file = f"{base_name}_transcript.txt"
    
    # Save the transcription
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(transcription)
    
    return output_file

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Transcribe audio file using Whisper model')
    parser.add_argument('audio_path', type=str, help='Path to the audio file')
    parser.add_argument('--model', type=str, default='openai/whisper-large-v2',
                        choices=['openai/whisper-tiny', 'openai/whisper-base', 
                                'openai/whisper-small', 'openai/whisper-medium',
                                'openai/whisper-large', 'openai/whisper-large-v2'],
                        help='Whisper model to use (default: openai/whisper-large-v2)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.exists(args.audio_path):
        print(f"Error: The file '{args.audio_path}' does not exist.")
        sys.exit(1)
    
    try:
        print(f"Starting transcription of: {args.audio_path}")
        print(f"Using model: {args.model}")
        
        # Get transcription
        transcription = transcribe_audio(args.audio_path, args.model)
        
        # Save transcript to file
        output_file = save_transcript(args.audio_path, transcription)
        
        print("\nTranscription completed!")
        print(f"Transcript saved to: {output_file}")
        print("\nTranscript preview (first 500 characters):")
        print("-" * 50)
        print(f"{transcription[:500]}{'...' if len(transcription) > 500 else ''}")
        print("\nFull transcription has been saved to the output file.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()