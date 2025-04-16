import os
import time
import threading
import hashlib
import random

class EntropyPool:
    def __init__(self):
        self.entropy_data = bytearray()
        self.lock = threading.Lock()

    def mix(self, data: bytes):
        """Ajoute de l'entropie dans le pool"""
        with self.lock:
            self.entropy_data.extend(data)

    def get_entropy(self):
        """Retourne un hash SHA-256 de l'entropie accumulée"""
        with self.lock:
            digest = hashlib.sha256(self.entropy_data).digest()
            return digest

    def _auto_refresh(self):
        """Ajoute périodiquement de l'entropie système"""
        while True:
            system_entropy = os.urandom(32)
            timestamp = time.time_ns().to_bytes(8, 'big')
            random_bits = random.getrandbits(256).to_bytes(32, 'big')
            self.mix(system_entropy + timestamp + random_bits)
            time.sleep(1)

    def start_auto_refresh(self):
        """Lance un thread qui ajoute en continu de l'entropie système"""
        threading.Thread(target=self._auto_refresh, daemon=True).start()
