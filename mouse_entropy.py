import tkinter as tk
import time

mouse_data = []

def on_mouse_move(event):
    mouse_data.append(f"{event.x},{event.y},{time.time_ns()}")

def collect_mouse_entropy(duration=10):  # ← durée augmentée à 10 secondes
    root = tk.Tk()
    root.title("Déplace la souris ! (10 secondes)")
    root.geometry("800x600")  # ← plus grande fenêtre

    root.bind('<Motion>', on_mouse_move)
    root.after(duration * 1000, root.destroy)
    root.mainloop()

    return ''.join(mouse_data)
