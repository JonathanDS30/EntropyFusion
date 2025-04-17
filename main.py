from modules.pool_entropy import EntropyPool
from modules.random_daemon import RandomDaemon
from modules.secure_rng import chacha20_rng
from modules.text_entropy import get_text_entropy
from modules.audio_entropy import record_audio_entropy
from modules.webcam_entropy import capture_webcam_entropy
from modules.mouse_entropy import collect_mouse_entropy
import numpy as np
import os
import time
import base64

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def analyse_entropie_pure_python(data: bytes):
    print("\n📊 Analyse statistique en Python :")
    data_np = np.frombuffer(data, dtype=np.uint8)
    entropy = -np.sum([p * np.log2(p) for p in np.bincount(data_np, minlength=256) / len(data_np) if p > 0])
    mean = np.mean(data_np)
    serial_corr = np.corrcoef(data_np[:-1], data_np[1:])[0, 1]

    print(f"   🔹 Entropie (Shannon) : {entropy:.4f} bits par octet")

    print("\n📈 Plage de qualité de l'entropie :")
    seuils = [
        (7.9, 8.0, "✅ Excellent : adapté à la production"),
        (7.5, 7.9, "✅ Acceptable : utilisable en production"),
        (7.0, 7.5, "⚠️ Moyen : amélioration recommandée"),
        (0.0, 7.0, "❌ Faible : non adapté à la production"),
    ]

    for bas, haut, label in seuils:
        if bas <= entropy < haut or (haut == 8.0 and entropy == 8.0):
            print(f" 👉 {bas:.1f} - {haut:.1f} bits : {label}  ← ✅ ENTROPIE MESURÉE ICI")
        else:
            print(f"     {bas:.1f} - {haut:.1f} bits : {label}")
    print()




def collecte_entropie_humaine(pool):
    print("\n🧠 Collecte manuelle d'entropie humaine...")
    print("⌨️ Entropie via texte clavier")
    user = get_text_entropy()

    print("📸 Capture d'image (webcam)")
    webcam = capture_webcam_entropy()

    print("🖱️ Capture des mouvements de souris")
    mouse = collect_mouse_entropy(duration=10)

    print("🎙️ Enregistrement sonore (10 sec)")
    audio = record_audio_entropy(seconds=10)

    combined = (user + webcam + mouse + audio).encode()
    pool.mix(combined)
    print("✅ Entropie humaine ajoutée au pool avec succès !\n")


def main():
    clear()
    print("====== 🧠 GÉNÉRATION COMPLÈTE ======\n")

    print("Étape 1/3 : Ajout d'entropie humaine\n")
    pool = EntropyPool()
    pool.start_auto_refresh()
    daemon = RandomDaemon(pool)
    daemon.start()

    collecte_entropie_humaine(pool)

    print("Étape 2/3 : Génération d'octets aléatoires\n")
    entropy = pool.get_entropy()
    rnd = chacha20_rng(entropy, size=64)


    b64 = base64.b64encode(rnd).decode('ascii')
    print("🎲 Résultat (64 octets en Base64) :")
    print(b64, "\n")

    print("Étape 3/3 : Test statistique (256 Ko)")
    print("⏳ Remplissage du tampon...")
    try:
        data = daemon.get_random_bytes(256 * 1024, timeout=15.0)
        analyse_entropie_pure_python(data)
    except TimeoutError as e:
        print(f"❌ Erreur : {e}")

    print("✅ Terminé.\n")


if __name__ == "__main__":
    main()
