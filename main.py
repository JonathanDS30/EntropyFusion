import hashlib

from modules.text_entropy import get_text_entropy
from modules.mouse_entropy import collect_mouse_entropy
from modules.webcam_entropy import capture_webcam_entropy
from modules.audio_entropy import record_audio_entropy

def generate_final_entropy():
    print("[1] Collecte d'entropie via texte")
    text = get_text_entropy()

    print("[2] Collecte d'entropie via mouvements de souris")
    mouse = collect_mouse_entropy()

    print("[3] Collecte d'entropie via webcam")
    webcam = capture_webcam_entropy()

    print("[4] Collecte d'entropie via micro")
    audio = record_audio_entropy()

    # Combinaison de toutes les sources
    combined = text + mouse + webcam + audio
    print("\nFusion des entropies et hachage SHA-512...")
    final_hash = hashlib.sha512(combined.encode()).hexdigest()
    
    # Génération d'un nombre pseudo-aléatoire (cryptographiquement fort si on veut aller + loin)
    random_number = int(final_hash, 16) % 1_000_000
    print(f"\n🎲 Nombre aléatoire sécurisé généré : {random_number}")

if __name__ == "__main__":
    generate_final_entropy()
