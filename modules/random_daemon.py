import threading
import time
from modules.secure_rng import chacha20_rng
from modules.pool_entropy import EntropyPool

class RandomDaemon:
    def __init__(self, entropy_pool):
        self.pool = entropy_pool
        self.buffer = bytearray()
        self.lock = threading.Lock()
        self.running = True
        self.thread = threading.Thread(target=self._generate_loop, daemon=True)

    def _generate_loop(self):
        """Alimente le tampon d’aléa en continu en arrière-plan"""
        while self.running:
            entropy = self.pool.get_entropy()
            random_block = chacha20_rng(entropy, size=64)
            with self.lock:
                self.buffer.extend(random_block)
                # Limite la taille du buffer pour éviter qu’il devienne trop gros
                if len(self.buffer) > 1024 * 1024:  # 1 Mo
                    self.buffer = self.buffer[-1024 * 1024:]
            time.sleep(0.001)  # accélération de la génération

    def start(self):
        """Lance le thread de génération"""
        self.thread.start()

    def stop(self):
        """Arrête la génération en fond"""
        self.running = False
        self.thread.join()

    def get_random_bytes(self, n: int, timeout: float = 10.0) -> bytes:
        """Retourne n octets depuis le buffer sécurisé, avec timeout"""
        start_time = time.time()
        while True:
            with self.lock:
                if len(self.buffer) >= n:
                    result = self.buffer[:n]
                    del self.buffer[:n]
                    return bytes(result)
            if time.time() - start_time > timeout:
                raise TimeoutError(f"⏰ Timeout : impossible d’obtenir {n} octets en {timeout} secondes.")
            time.sleep(0.01)
