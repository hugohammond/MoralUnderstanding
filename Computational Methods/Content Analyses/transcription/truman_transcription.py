# Hugo Hammond: 14 Sept 23
# This file transcribes the audio for the Truman Show

import pandas as pd
import whisper


model = whisper.load_model("large")
result = pd.DataFrame(model.transcribe("data/audio_truman.mov"))
result.to_csv('data/truman_transcript.csv')
