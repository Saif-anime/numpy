import cv2
import numpy as np

# Define video parameters
output_file = 'output_video.mp4'
frame_width, frame_height = 640, 480
fps = 30
duration_seconds = 10

# Create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

# Generate frames and write them to the video
for frame_num in range(duration_seconds * fps):
    # Create a black frame
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

    # Draw a moving square
    x = int(frame_width * frame_num / (duration_seconds * fps))
    cv2.rectangle(frame, (x, 100), (x + 50, 200), (0, 255, 0), -1)

    # Write the frame to the video
    out.write(frame)

# Release the VideoWriter
out.release()

print(f"Video '{output_file}' generated successfully.")
