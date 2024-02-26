import wave
import vosk
import os
import json

# Define input and output file paths
# wave_file = "test.wav"
# text_file = "output.txt"

# Check if Vosk model is downloaded
if not os.path.exists(r"vosk-model-small-uz"):
    print("""Please download the Vosk model from 
          https://alphacephei.com/vosk/models 
          and unpack as 'model' in the current folder.""")
    exit(1)

def stt(wave_file):
   
  # Open the wave file
  with wave.open(wave_file, "rb") as wf:
   # Load the Vosk model 
   model = vosk.Model(r"vosk-model-small-uz")

   # Create a KaldiRecognizer
   rec = vosk.KaldiRecognizer(model, wf.getframerate())

   
   data = json.loads(rec.Result())
   return data["text"]
  
   # Write transcribed text to file
