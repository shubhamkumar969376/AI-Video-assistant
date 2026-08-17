import os
import re

import yt_dlp
import imageio_ffmpeg

from pydub import AudioSegment
from pydub.utils import which


# --------------------------------------------------
# Configuration
# --------------------------------------------------

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Get FFmpeg from imageio-ffmpeg
FFMPEG_PATH = imageio_ffmpeg.get_ffmpeg_exe()

# Tell pydub which FFmpeg to use
AudioSegment.converter = FFMPEG_PATH


# --------------------------------------------------
# Helper: make Windows-safe filename
# --------------------------------------------------

def safe_filename(name: str) -> str:
    """
    Remove characters that are not allowed in Windows filenames.
    """

    # Windows does not allow:
    # < > : " / \ | ? *

    name = re.sub(r'[<>:"/\\|?*]', '', name)

    # Remove trailing spaces and dots
    name = name.strip().rstrip(".")

    # Avoid empty filename
    if not name:
        name = "audio"

    return name


# --------------------------------------------------
# Download YouTube audio
# --------------------------------------------------

def download_audio_from_youtube(url: str) -> str:

    output_path = os.path.join(
        DOWNLOAD_DIR,
        "%(title)s.%(ext)s"
    )

    ydl_opts = {
        "format": "bestaudio/best",

        "outtmpl": output_path,

        # FFmpeg location
        "ffmpeg_location": FFMPEG_PATH,

        # Convert audio to WAV
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],

        "noplaylist": True,

        "quiet": False,
    }

    print("Downloading audio from YouTube...")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(
            url,
            download=True
        )

        # Get the actual filename produced by yt-dlp
        downloaded_file = ydl.prepare_filename(info)

        # Replace original extension with .wav
        wav_path = os.path.splitext(
            downloaded_file
        )[0] + ".wav"

        # If necessary, normalize the filename
        if not os.path.exists(wav_path):

            title = safe_filename(
                info.get("title", "audio")
            )

            wav_path = os.path.join(
                DOWNLOAD_DIR,
                title + ".wav"
            )

    print(f"WAV file: {wav_path}")

    return wav_path


# --------------------------------------------------
# Convert local audio to WAV
# --------------------------------------------------

def convert_audio_to_wav(input_file: str) -> str:

    base_name = os.path.splitext(
        input_file
    )[0]

    output_file = (
        base_name +
        "_converted.wav"
    )

    print(
        f"Converting {input_file} to WAV..."
    )

    audio = AudioSegment.from_file(
        input_file
    )

    # Mono
    audio = audio.set_channels(1)

    # 16 kHz
    audio = audio.set_frame_rate(16000)

    audio.export(
        output_file,
        format="wav"
    )

    return output_file


# --------------------------------------------------
# Chunk audio
# --------------------------------------------------

def chunk_audio(
    wav_path: str,
    chunks_minutes: int = 1
) -> list:

    print("Loading WAV file...")

    audio = AudioSegment.from_wav(
        wav_path
    )

    chunk_length_ms = (
        chunks_minutes *
        60 *
        1000
    )

    chunks = []

    for i in range(
        0,
        len(audio),
        chunk_length_ms
    ):

        chunk = audio[
            i:i + chunk_length_ms
        ]

        chunk_number = (
            i // chunk_length_ms
        )

        chunk_filename = (
            f"{os.path.splitext(wav_path)[0]}"
            f"_chunk_{chunk_number}.wav"
        )

        chunk.export(
            chunk_filename,
            format="wav"
        )

        chunks.append(
            chunk_filename
        )

    return chunks


# --------------------------------------------------
# Process input
# --------------------------------------------------

def process_input(source: str) -> list:

    if (
        source.startswith("http://")
        or
        source.startswith("https://")
    ):

        print("Source: YouTube")

        wav_path = (
            download_audio_from_youtube(
                source
            )
        )

    else:

        print("Source: Local audio file")

        wav_path = (
            convert_audio_to_wav(
                source
            )
        )

    print(
        "Chunking audio..."
    )

    chunks = chunk_audio(
        wav_path,
        chunks_minutes=1
    )

    print(
        f"Created {len(chunks)} chunks."
    )

    return chunks


# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__ == "__main__":

    youtube_url = (
        "https://www.youtube.com/watch?v=DFbbpMD3taw&list=RDDFbbpMD3taw&start_radio=1"
    )

    chunks = process_input(
        youtube_url
    )

    print("\nGenerated chunks:")

    for chunk in chunks:
        print(chunk)