import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def generate_countdown_video(duration, output_file):
    # Set video dimensions and FPS
    width, height = 640, 480
    fps = 30

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Load a font for the countdown numbers
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 128)

    for seconds_left in range(duration, 0, -1):
        # Calculate minutes and seconds
        minutes = seconds_left // 60
        seconds = seconds_left % 60

        # Create a blank frame
        frame = np.zeros((height, width, 3), dtype=np.uint8)

        # Create a PIL Image object from the frame
        img_pil = Image.fromarray(frame)

        # Draw the countdown timer on the PIL Image
        draw = ImageDraw.Draw(img_pil)
        text = f"{minutes:02d}:{seconds:02d}"
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        x = (width - text_width) // 2
        y = (height - text_height) // 2
        draw.text((x, y), text, font=font, fill=(255, 255, 255))

        # Convert the PIL Image back to a NumPy array
        frame = np.array(img_pil)

        # Write the frame to the video for 1 second
        for _ in range(fps):
            video.write(frame)

    # Release the video object
    video.release()

# Example usage
duration = 300  # Countdown duration in seconds (3 minutes)
output_file = "countdown.mp4"  # Output video file name
generate_countdown_video(duration, output_file)
