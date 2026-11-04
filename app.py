from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip

video = VideoFileClip("video.mp4")
voice = AudioFileClip("voice.mp3")

try:  # the try statement tells python that the following code might encounter errors
    final_audio = CompositeAudioClip([
        video.audio,  # extracts the audio from the given video
        voice
    ])

    final_video = video.with_audio(final_audio)

    final_video.write_videofile(
        "final_output.mp4",
        codec="libx264",  # video encoder
        audio_codec="aac"  # audio encoder
    )
    # this is resource management
finally:
    if final_video is not None:
        final_video.close()

    video.close()
    voice.close()

print(video.rotation)
