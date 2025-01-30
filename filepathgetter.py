# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:43:14 2025

@author: colin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:31:44 2025

@author: colin
"""

import os
import csv
from datetime import datetime

def list_files_in_directory(base_path, output_file):
    # Liste für die Dateiinformationen
    files_info = []

    # Durchlaufe das Verzeichnis rekursiv
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)  # Vollständiger Pfad
            file_size = os.path.getsize(file_path)  # Dateigröße in Bytes
            file_ext = os.path.splitext(file)[-1].lower()  # Dateiendung
            mod_time = os.path.getmtime(file_path)  # Änderungszeitpunkt
            mod_time_readable = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')

            # Dateiinfo speichern
            files_info.append({
                'Full Path': file_path,
                'File Name': file,
                'File Extension': file_ext,
                'File Size (Bytes)': file_size,
                'Last Modified': mod_time_readable
            })

    # Speichere die Informationen in einer CSV-Datei
    with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['Full Path', 'File Name', 'File Extension', 'File Size (Bytes)', 'Last Modified'])
        writer.writeheader()
        writer.writerows(files_info)

    print(f"Dateiinformationen erfolgreich in {output_file} gespeichert.")

# Hauptverzeichnis hier anpassen
base_path = r"D:\Literatur_sortiert\02_ML_und_KI" # Verwende r"" für Rohstring
# base_path = "/Pfad/zum/Hauptverzeichnis"  # Beispiel für Linux/Mac

# Pfad zur Ausgabe-CSV-Datei
output_file = r"D:\Output\file_list_2.csv"  # Verwende r"" für Rohstring

# Funktion aufrufen
list_files_in_directory(base_path, output_file)
