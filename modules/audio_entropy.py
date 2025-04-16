import sounddevice as sd
import numpy as np
import hashlib  # ← manquant dans ton erreur

def record_audio_entropy(seconds=10, samplerate=44100):  # ← durée augmentée à 10s
    print("Parle, tape ou fais du bruit près du micro pendant 10 secondes...")
    audio = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    return hashlib.sha256(audio.tobytes()).hexdigest()
