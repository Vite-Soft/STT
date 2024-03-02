import wave
import vosk
import os
import json

# Check if Vosk model is downloaded
if not os.path.exists(r"base/vosk-model-small-uz"):
    print("""Please download the Vosk model from 
          https://alphacephei.com/vosk/models 
          and unpack as 'model' in the current folder.""")
    exit(1)

def stt(wav_file):
  # Open the wave file
  with wave.open(wav_file, "rb") as wf:
  # Load the Vosk model 
   print("Model not foun")
   model = vosk.Model(r"base/vosk-model-small-uz")
   # Create a KaldiRecognizer
   rec = vosk.KaldiRecognizer(model, wf.getframerate())

  while True:
        data = wf.readframes(400000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            data = json.loads(rec.Result())
            return data["text"]
        else:
            # f.write(rec.PartialResult() + "\n")
            pass
