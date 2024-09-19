import tkinter as tk
from tkinter import filedialog
import random


# Fonction pour ouvrir le fichier et sélectionner une ligne aléatoire
def choisir_fichier():
    fichier = filedialog.askopenfilename(title="Choisir un fichier", filetypes=[("Fichiers texte", "*.txt")])

    if fichier:
        try:
            # Lire les lignes du fichier
            with open(fichier, 'r', encoding='utf-8') as f:
                lignes = f.readlines()

            if lignes:
                # Mise à jour du champ texte avec le nom du fichier sélectionné
                champ_fichier.config(state='normal')
                champ_fichier.delete(0, tk.END)
                champ_fichier.insert(0, fichier)
                champ_fichier.config(state='readonly')

                # Activer le bouton pour recommencer le tirage
                bouton_tirage.config(state='normal')

                # Stocker les lignes dans une variable globale pour les réutiliser
                global lignes_fichier
                lignes_fichier = lignes
            else:
                afficher_tirage("Le fichier sélectionné est vide.")
        except Exception as e:
            afficher_tirage(f"Erreur lors de la lecture du fichier : {str(e)}")


# Fonction pour réaliser un tirage aléatoire et l'afficher dans une case
def tirage_aleatoire():
    if lignes_fichier:
        ligne_aleatoire = random.choice(lignes_fichier).strip()
        afficher_tirage(ligne_aleatoire)


# Fonction pour afficher les résultats dans des cases dans la zone scrollable
def afficher_tirage(resultat):
    # Créer une nouvelle case pour afficher le tirage
    nouvelle_case = tk.Label(frame_scrollable, text=resultat, relief="solid", width=60)

    # Insérer la nouvelle case au début de la liste des enfants du frame
    nouvelle_case.pack(pady=2, anchor='w')

    # Forcer la mise à jour de la scrollbar
    frame_scrollable.update_idletasks()
    canvas.yview_moveto(1)  # Scroll vers le bas pour afficher le dernier tirage


# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Tirage aléatoire")
fenetre.geometry("600x400")

# Création du bouton pour choisir un fichier
bouton_fichier = tk.Button(fenetre, text="Choisir un fichier txt", command=choisir_fichier)
bouton_fichier.pack(pady=10)

# Champ texte pour afficher le fichier sélectionné
champ_fichier = tk.Entry(fenetre, width=60, state='readonly')
champ_fichier.insert(0, "None")
champ_fichier.pack(pady=10)

# Création du bouton pour recommencer un tirage
bouton_tirage = tk.Button(fenetre, text="Realiser un tirage", command=tirage_aleatoire, state='disabled')
bouton_tirage.pack(pady=10)

# Création de la zone scrollable pour les résultats
frame_scrollable_container = tk.Frame(fenetre)
frame_scrollable_container.pack(fill="both", expand=True, padx=10, pady=10)

# Création du Canvas pour contenir la Frame scrollable
canvas = tk.Canvas(frame_scrollable_container)
canvas.pack(side="left", fill="both", expand=True)

# Ajout de la scrollbar
scrollbar = tk.Scrollbar(frame_scrollable_container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Frame contenant les résultats (scrollable)
frame_scrollable = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_scrollable, anchor="nw")

# Configurer la scrollbar avec le canvas
canvas.config(yscrollcommand=scrollbar.set)


# Assurer que la zone scrollable redimensionne correctement
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


frame_scrollable.bind("<Configure>", on_frame_configure)

# Lancer la boucle principale
fenetre.mainloop()
