import wave
import vosk
import os
import sys
import json

# Check if Vosk model is downloaded
if not os.path.exists(r"base/vosk-model-small-uz"):
    print("""Please download the Vosk model from 
          https://alphacephei.com/vosk/models 
          and unpack as 'model' in the current folder.""")
    exit(1)

def stt(wav_file):
  if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be WAV format mono PCM.")
    sys.exit(1)

  # Open the wave file
  with wave.open(wav_file, "rb") as wf:
   
  # Load the Vosk model 
   model = vosk.Model(r"base/vosk-model-small-uz")
   
   # Create a KaldiRecognizer
   rec = vosk.KaldiRecognizer(model, wf.getframerate())

  while True:
        data = wf.readframes(wf.getnframes())

        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            return result["text"]
        else:
            # f.write(rec.PartialResult() + "\n")
            pass
