from moviepy.editor import VideoFileClip

# Input video file path
input_file = 'HunterXHunterPhantom20Rouge-TPX.mp4'

# Output video file path (compressed)
output_file = 'example.mp4'

# Load the video clip
video_clip = VideoFileClip(input_file)

# Define the target bitrate for compression (in kbps)
target_bitrate = '1000k'  # Adjust this value as needed

# Write the compressed video to the output file with the specified bitrate
video_clip.write_videofile(output_file, codec='libx264', bitrate=target_bitrate)

# Close the video clip
video_clip.close()
