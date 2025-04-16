import hashlib
import time

def get_text_entropy():
    print("Écris quelque chose de totalement aléatoire (spam ton clavier) :")
    user_input = input()
    timestamp = str(time.time_ns())
    entropy = user_input + timestamp
    return entropy