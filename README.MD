# Random Selector

Ce script python permet de choisir aléatoirement un élément parmi une liste d'éléments, contenus dans un fichier texte.

Ce projet adhére au [Changelog Convention](https://keepachangelog.com/en/1.0.0/) et au [Semantic Versioning](https://semver.org/).

# Sommaire

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Compilation depuis le code source](#compilation-depuis-le-code-source)
- [Changelog](#changelog)

# Installation

Pour installer le script, il suffit de séléctionner la version souhaitée dans la section [Releases](https://github.com/Darkbriks/Random_Selector_PY/releases) et de télécharger le fichier exécutable correspondant à votre système d'exploitation.

**Note:** A l'heure actuelle, seul les systèmes d'exploitation Windows sont supportés.

# Utilisation

Pour utiliser le script, il suffit de lancer le fichier exécutable téléchargé. Une fenêtre s'ouvrira et vous demandera de sélectionner le fichier texte contenant les éléments du tirage.

Le fichier texte doit être formaté de la manière suivante:
```
Element 1
Element 2
Element 3
...
Element n
```

Une fois le fichier sélectionné, le script choisira aléatoirement un élément parmi la liste et l'affichera dans la fenêtre.

# Compilation depuis le code source

Pour compiler le script depuis le code source, il vous faudra les dépendances suivantes:
- Python 3.8 ou supérieur
- PyInstaller

Pour installer PyInstaller, exécutez la commande suivante:
```
pip install pyinstaller
```

Ensuite, pour compiler le script, exécutez la commande suivante:
```
pyinstaller --onefile --noconsole main.py --name Random_Selector_<Version_Label>_<Version_Number>
```

Pour ajouter une icône au fichier exécutable, ajoutez l'option `--icon=<Path_To_Icon>` à la commande précédente.

# Changelog

## **Unreleased**

## **Version 0.2.0 - Altair**

### **Added**
  - Classe reel pour gérer les rouleaux
  - Classe window pour gérer la fenêtre principale
  - Utilisation d'un fichier de configuration pour rendre la fenêtre plus modulaire

### **Changed**
  - Le main utilise désormais la classe window pour gérer la fenêtre principale
  - L'interface a été améliorée pour ce raprocher de la version souhaitée

## **Version 0.1.1**

### **Changed**
  - Le script n'affiche plus le chemin du fichier sélectionné, mais uniquement son nom

## **Version 0.1.0 - Capella**
  - Première version du script
  - Ajout de la fonctionnalité de tirage aléatoire
  - Ajout de la fonctionnalité de sélection de fichier
  - Ajout de la fonctionnalité d'affichage du résultat