import tkinter as tk
import time
import requests
from io import BytesIO
from PIL import Image, ImageTk
import os
from dotenv import load_dotenv

def get_random_photo_url():
    """
    Récupère l'URL d'une photo aléatoire depuis l'API Unsplash.
    Charge les variables d'environnement et utilise la clé d'API Unsplash.
    Renvoie l'URL de la version 'regular' de la photo.
    """
    # Charge les variables d'environnement depuis le fichier .env
    load_dotenv()
    
    # Récupère la clé d'API Unsplash depuis les variables d'environnement
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    if not access_key:
        raise ValueError("La clé d'API Unsplash n'est pas définie dans le fichier .env")
    
    endpoint = "https://api.unsplash.com/photos/random"
    headers = {
        "Authorization": f"Client-ID {access_key}",
        "Accept-Version": "v1"
    }
    # Paramètre pour obtenir une image en orientation paysage
    params = {
        "orientation": "landscape"
    }
    
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()  # Vérifie que la requête s'est bien passée
        data = response.json()
        # Récupère l'URL de la version 'regular' de l'image
        photo_url = data["urls"]["regular"]
        return photo_url
    except Exception as e:
        print("Erreur lors de la récupération de la photo :", e)
        return None

def collect_mouse_entropy(duration=10):
    """
    Télécharge une image aléatoire depuis Unsplash et l'affiche dans une fenêtre Tkinter.
    Capture les mouvements de la souris sur cette image pendant 'duration' secondes.
    Pour chaque déplacement, récupère les coordonnées (x, y), la couleur du pixel survolé (R, G, B)
    ainsi qu'un timestamp précis. Les valeurs sont affichées en direct dans la console.
    Retourne les données d'entropie sous forme de chaîne.
    """
    # Récupération de l'URL de la photo aléatoire
    photo_url = get_random_photo_url()
    if photo_url is None:
        print("Impossible de récupérer une image aléatoire.")
        return ""
    
    try:
        # Téléchargement de l'image en mémoire
        response = requests.get(photo_url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
    except Exception as e:
        print("Erreur lors du téléchargement de l'image :", e)
        return ""
    
    # Création de la fenêtre Tkinter et configuration du Canvas
    root = tk.Tk()
    root.title("Déplace la souris sur l'image ! (10 secondes)")
    
    tk_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(root, width=image.width, height=image.height)
    canvas.pack()
    
    # Affichage de l'image sur le Canvas
    canvas.create_image(0, 0, image=tk_image, anchor="nw")
    # Conserver une référence de l'image pour éviter qu'elle soit collectée par le garbage collector
    canvas.image = tk_image
    
    mouse_data = []  # Liste pour stocker les données d'entropie

    def on_mouse_move(event):
        """
        Fonction appelée à chaque mouvement de la souris.
        Récupère les coordonnées (x, y), la couleur du pixel survolé et le timestamp,
        puis affiche ces valeurs dans la console.
        """
        # Vérifie que les coordonnées sont dans la zone de l'image
        if 0 <= event.x < image.width and 0 <= event.y < image.height:
            pixel_color = image.getpixel((event.x, event.y))
            # Si l'image n'est pas en mode tuple (ex: image en niveaux de gris), conversion en tuple RGB
            if not isinstance(pixel_color, tuple):
                pixel_color = (pixel_color, pixel_color, pixel_color)
        else:
            pixel_color = (0, 0, 0)  # Valeur par défaut si en dehors des bornes

        # Format de la donnée collectée : x,y,R,G,B,timestamp
        data_str = f"{event.x},{event.y},{pixel_color[0]},{pixel_color[1]},{pixel_color[2]},{time.time_ns()}"
        mouse_data.append(data_str)
        
        # Affiche les informations dans la console en direct
        print(f"Position: ({event.x},{event.y}) - Couleur: {pixel_color} - Timestamp: {time.time_ns()}")
    
    # Liaison de l'événement 'Motion' du canvas avec la fonction on_mouse_move
    canvas.bind("<Motion>", on_mouse_move)
    
    # Fermeture automatique de la fenêtre après 'duration' secondes
    root.after(duration * 1000, root.destroy)
    root.mainloop()
    
    # Retourne les données d'entropie collectées sous forme de chaîne
    return ''.join(mouse_data)

if __name__ == "__main__":
    entropy = collect_mouse_entropy()
    print("Entropie collectée :", entropy)
