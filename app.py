from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip

video = VideoFileClip("video.mp4")
voice = AudioFileClip("voice.mp3")

try:  # the try statement tells python that the following code might encounter errors
    final_video = video.with_audio(voice)

    final_video.write_videofile(
        "final_output.mp4",
        codec="libx264",
        audio_codec="aac"
    )
finally:
    video.close()
    voice.close()
    final_video.close()
print(video.duration)
