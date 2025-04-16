import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def chacha20_rng(key: bytes, size: int = 64) -> bytes:
    """
    Génère un flux d'octets pseudo-aléatoires sécurisé en utilisant ChaCha20.
    :param key: Une clé de 32 octets (256 bits), typiquement issue du pool d'entropie
    :param size: Nombre d'octets à générer
    :return: Un flux d'octets aléatoires
    """
    if len(key) != 32:
        raise ValueError("La clé doit faire exactement 32 octets.")

    nonce = os.urandom(16)  # ChaCha20 de cryptography attend un nonce de 16 octets
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None)
    encryptor = cipher.encryptor()
    return encryptor.update(b'\x00' * size)
