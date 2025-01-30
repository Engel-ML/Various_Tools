# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:51:05 2025

@author: colin
"""

import os
import shutil
import csv

def categorize_file(file_name):
    categories = {
        "Grundlagen": ["Primer", "Beginning", "Introduction"],
        "Visualisierung": ["Visualization", "Graphs", "Plotting"],
        "Algorithmen": ["Algorithms", "Data Structures"],
        "Frameworks": ["Kivy", "Flask", "Django"],
        "Statistik und Graphenmodelle": ["Probabilistic", "Statistical", "Bayesian", "Graphical"],
        "Webentwicklung": ["Web", "Flask", "Django"],
        "Maschinelles Lernen": ["Machine Learning", "Neural", "Deep Learning"],
        "Spieleentwicklung": ["Game", "Pygame"],
        "Automatisierung": ["Automation", "Scripting", "Task"],
        "Python-Syntax und Standardbibliothek": ["Python Standard Library", "Syntax"],
        "Erweiterte Python-Techniken": ["Advanced", "Expert", "Design Patterns"]
    }

    for category, keywords in categories.items():
        if any(keyword.lower() in file_name.lower() for keyword in keywords):
            return category
    return "Sonstiges"

def organize_files(csv_file, target_base_path):
    # Erstelle das Zielverzeichnis, falls es nicht existiert
    if not os.path.exists(target_base_path):
        os.makedirs(target_base_path)

    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            file_path = row['Full Path']
            file_name = row['File Name']

            # Kategorisiere die Datei basierend auf dem Dateinamen
            category = categorize_file(file_name)

            # Zielpfad erstellen
            category_path = os.path.join(target_base_path, category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)

            # Verschiebe die Datei
            try:
                shutil.move(file_path, os.path.join(category_path, file_name))
                print(f"{file_name} -> {category}")
            except Exception as e:
                print(f"Fehler beim Verschieben von {file_name}: {e}")

# Eingabedatei (CSV) und Zielverzeichnis anpassen
csv_file = r"D:\Output\file_list_Python.csv"  # Pfad zur CSV-Datei
target_base_path = r"D:\Sorted_Python_Files"  # Zielbasisverzeichnis

# Funktion aufrufen
organize_files(csv_file, target_base_path)
