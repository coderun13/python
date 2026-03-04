import os
from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_ext="mp3"):
    # 1. Check if the video file exists
    if not os.path.exists(video_path):
        print(f"Error: File '{video_path}' not found.")
        return

    try:
        # 2. Load the video file
        print(f"Loading video: {video_path}")
        video = VideoFileClip(video_path)
        
        # 3. Define the output filename
        # This replaces the old extension (e.g., .mp4) with the new one (.mp3)
        filename, _ = os.path.splitext(video_path)
        output_filename = f"{filename}.{output_ext}"

        # 4. Extract and save audio
        print(f"🎵 Extracting audio to: {output_filename}...")
        video.audio.write_audiofile(output_filename)
        
        # 5. Close the video to release the file
        video.close()
        print("Success! Audio extraction complete.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure your video file (e.g., sample_video.mp4) is in the same folder
    extract_audio("sample_video.mp4")