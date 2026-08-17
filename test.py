from utils.audio_processor import process_input
from core.transcriber import transcribe_all

chunks=process_input("https://www.youtube.com/watch?v=t6nHfdKgshg&list=RDt6nHfdKgshg&start_radio=1")
transcript=transcribe_all(chunks)
print(transcript    )