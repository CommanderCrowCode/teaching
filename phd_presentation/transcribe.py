import sys
from flamingotools import ai_tools
from dotenv import load_dotenv
import os
load_dotenv()

if len(sys.argv) < 2:
  print("Please provide the path to the audio file as an argument.")
  sys.exit(1)

# Get the file path from the command line argument
file_path = sys.argv[1]

# Transcribe the audio file
transcription = ai_tools.transcribe_audio(file_path)

# Get the input file name without the extension
file_name = os.path.splitext(os.path.basename(file_path))[0]

# Create the output file path with the same name as the input file but with ".txt" extension
output_file_path = f"{file_name}.txt"

# Save the output to the file with the modified file path
with open(output_file_path, "w") as f:
  f.write(transcription.text)
