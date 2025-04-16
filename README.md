# 🔐 EntropyFusion — Générateur d'Aléatoire Sécurisé basé sur l'Entropie Humaine

<p align="center">
  <img src="assets/logo.png" alt="FusedEntropy Logo" width="400"/>
</p>

**EntropyFusion** est un générateur de nombres aléatoires en Python qui s’appuie sur des sources d’entropie *humaines et physiques*. Il est conçu à des fins éducatives ou expérimentales, notamment en cybersécurité ou en cryptographie.

---

## 🚀 Fonctionnalités

Le système collecte des données imprévisibles à partir de plusieurs sources :

- ⌨️ **Texte libre** saisi par l’utilisateur
- 🖱️ **Mouvements de la souris** sur une **image aléatoire** issue d’Unsplash, avec capture de la **position**, **timestamp** et **couleur du pixel**
- 📸 **Image capturée depuis la webcam**
- 🎙️ **Audio ambiant** enregistré pendant 10 secondes via le micro
- 🔁 **Entropie système (CPU, horloge, `os.urandom`)** automatiquement ajoutée en arrière-plan

Toutes les données sont fusionnées, mélangées via un `EntropyPool`, puis utilisées pour :
- 🔐 Générer un flux aléatoire cryptographiquement sûr avec l’algorithme **ChaCha20**
- 📊 Réaliser une **analyse statistique** basique de l'entropie sur un bloc de 256 Ko

---

## 📁 Structure du projet

```bash
EntropyFusion/
│
├── main.py                    # Point d'entrée principal
├── .env                       # Clé d'API Unsplash (non versionnée)
├── requirements.txt           # Dépendances Python
├── README.md
├── assets/
│   └── logo.png               # Logo du projet
├── modules/
│   ├── audio_entropy.py       # Source audio (micro)
│   ├── webcam_entropy.py      # Source image (webcam)
│   ├── mouse_entropy.py       # Source souris + couleurs pixels
│   ├── text_entropy.py        # Source clavier
│   ├── pool_entropy.py        # Pool d'entropie partagé
│   ├── secure_rng.py          # Générateur ChaCha20
│   ├── random_daemon.py       # Daemon de génération en continu
```

## 🛠️ Installation

### 1. Cloner le projet

`git clone https://github.com/JonathanDS30/EntropyFusion.git cd EntropyFusion`

### 2. Installer les dépendances

`pip install -r requirements.txt`

---

## 🔑 Configuration de l'API Unsplash

Le module de collecte de mouvements de souris utilise une image aléatoire récupérée via l’API d’[Unsplash](https://unsplash.com). Une clé d’API personnelle est nécessaire.

### Étapes pour obtenir une clé Unsplash :

1. Créer un compte sur unsplash.com/join
    
2. Accéder au portail développeur : [unsplash.com/developers](https://unsplash.com/developers)
    
3. Cliquer sur **"New Application"**
    
4. Donner un nom à l’application (ex. _EntropyFusion_) et accepter les conditions
    
5. Copier l’**Access Key** générée une fois l’application créée
    

### Ajouter la clé dans un fichier `.env`

1. Dupliquer le fichier `template.env` en `.env`
    
2. Renseigner la clé dans ce fichier :

`UNSPLASH_ACCESS_KEY=your_api_key_here`

---

## ▶️ Lancement

Une fois les dépendances installées et la configuration terminée, exécuter le projet avec :

`python main.py`

Le programme effectuera successivement :

- La collecte d’entropie humaine (texte, souris, webcam, audio)
    
- La génération d’un flux aléatoire de 64 octets (hexadécimal)
    
- Une analyse statistique simple sur un bloc de 256 Ko

## 👥 Créateurs du projet

- 🧑‍💻 [JonathanDS30](https://github.com/JonathanDS30)
    
- 🧑‍💻 [ml704457](https://github.com/ml704457)