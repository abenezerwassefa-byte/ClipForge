from moviepy import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, CompositeAudioClip
import whisper
# 1. Transcribe audio
model = whisper.load_model('base')

result = model.transcribe("video.mp4", fp16=False)

segments = result["segments"]

# 2. Generate caption clips
caption_clips = []

final_video = None

try:
    video = VideoFileClip("video.mp4")
    voice = AudioFileClip("voice.mp3").with_volume_scaled(0.2)

    for segment in segments:

        caption = TextClip(
            text=segment["text"].strip(),
            font_size=45,
            color="white",
            stroke_color="black",
            stroke_width=2,
            method="caption",
            size=(int(video.w * 0.85), None)
        )

        caption = (
            caption
            .with_start(segment["start"])
            .with_duration(segment["end"] - segment["start"])
            .with_position(("center", "bottom"))
        )

        caption_clips.append(caption)

    # This is what makes your captions appear inside the exported video rather than in the terminal.
    final_video = CompositeVideoClip(
        [video, *caption_clips],
        size=video.size
    )

    # 4. Attach your existing mixed audio
    final_audio = CompositeAudioClip([
        video.audio,
        voice
    ])

    final_video = (
        final_video
        .with_duration(video.duration)
        .with_audio(final_audio)
    )

    # Export
    final_video.write_videofile(
        "output.mp4",
        codec="libx264",  # video encoder
        audio_codec="aac"  # audio encoder

    )

# this is resource management
finally:
    if final_video is not None:
        final_video.close()
    video.close()
    voice.close()
