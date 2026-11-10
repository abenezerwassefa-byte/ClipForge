# ClipForge🎬

A Python-based video processing tool that combines audio tracks, transcribes speech using OpenAI Whisper, and generates synchronized, burned-in captions using MoviePy.

## Features

- **Speech Recognition:** Uses OpenAI Whisper (`base` model) to transcribe speech directly from a video.
- **Automatic Caption Generation:** Converts transcription segments into individual visual caption clips.
- **Timestamp Synchronization:** Uses Whisper's segment timestamps to synchronize captions with the original speech.
- **Audio Mixing:** Combines the video's original audio with an additional voice-over track.
- **Video Export:** Produces an MP4 video with embedded captions and mixed audio.

## Tech Stack

- Python
- [MoviePy](https://zulko.github.io/moviepy/)
- [OpenAI Whisper](https://github.com/openai/whisper)
- FFmpeg

## Project Structure

```text
ClipForge/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/abenezerwassefa-byte/ClipForge.git
cd ClipForge
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

You may also need to install FFmpeg separately and ensure it is accessible from your system PATH.

## Usage

Place your input files in the project directory:

```text
ClipForge/
├── app.py
├── video.mp4
└── voice.mp3
```

Run the application:

```bash
python app.py
```

The application will:

1. Load the Whisper speech recognition model.
2. Transcribe the speech in `video.mp4`.
3. Extract the transcription segments and their timestamps.
4. Generate caption clips.
5. Overlay the captions onto the original video.
6. Mix the original video audio with `voice.mp3`.
7. Export the processed video as `output.mp4`.

## Output

The processed video is saved as:

```text
output.mp4
```
## The Process + The Code Logic
LOAD WHISPER
TRANSCRIBE VIDEO
EXTRACT SEGMENTS

LOAD VIDEO
LOAD VOICE

TRY:

    GENERATE CAPTION CLIPS

    COMBINE ORIGINAL AUDIO + VOICE

    COMBINE VIDEO + CAPTIONS

    ATTACH MIXED AUDIO

    EXPORT VIDEO

FINALLY:

    CLOSE FINAL VIDEO
    CLOSE ORIGINAL VIDEO
    CLOSE VOICE

The output contains synchronized, permanently embedded captions and the combined audio tracks.

## Current Limitations

- Input filenames are currently hardcoded in `app.py`.
- Caption appearance is configured directly in the Python script.
- Transcription accuracy depends on audio quality and the Whisper model.
- The application currently processes one video and one additional audio track per execution.
- There is no graphical user interface yet.

## Future Improvements

- Configurable input and output paths.
- Customizable caption positioning, fonts, and styling.
- Adjustable audio levels.
- Improved caption segmentation and formatting.
- A graphical interface for easier video processing.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

