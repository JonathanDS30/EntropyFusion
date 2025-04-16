# 🔐 Générateur d'Aléatoire Sécurisé basé sur l'Entropie Humaine

Ce projet en Python génère un nombre aléatoire en utilisant plusieurs sources d'entropie imprévisibles. Il peut être utilisé à des fins de démonstration, d'apprentissage en cybersécurité ou même comme base pour des générateurs cryptographiques plus avancés.

---

## 🚀 Fonctionnalités

Le générateur collecte de l'entropie depuis plusieurs sources :
- 🧠 **Texte aléatoire** tapé par l'utilisateur
- 🖱️ **Mouvements de la souris** capturés pendant 10 secondes dans une fenêtre graphique
- 📸 **Capture d'image via webcam**
- 🎙️ **Enregistrement sonore de 10 secondes via le micro**

Ces données sont fusionnées, hachées avec SHA-512, puis utilisées pour produire un nombre pseudo-aléatoire.

---

## 🛠️ Installation

### 1. Cloner le projet
```bash
git clone https://github.com/JonathanDS30/EntropyFusion.git
cd generateur-entropie
