#!/usr/bin/python3

'''
Beschreibung: Programm zur Aufnahme und Speichern von Bildsequenzen + Laden von Kamera-Einstellungen mit einem Tuning-File
Variable Parameter: Dateispeicherort (Zeile 47), Anzahl d. Bilder (Zeile 51) und Zeitintervall zwischen den Bildaufnahmen (Zeile 53)
'''

from picamera2 import Picamera2, Preview
from picamera2.controls import Controls
import time
import os

# Laden des Tuning-Files "imx708.json"
tuning = Picamera2.load_tuning_file("imx708.json") # Für Raspberry Pi Kamera IR "imx708_noir.json" --> Tuning-Files in /usr/share/libcamera/ipa/rpi/pisp

# Kamera initialisieren und konfigurieren mit dem geladenen Tuning-File
picam2 = Picamera2(tuning=tuning)
picam2.configure(picam2.create_preview_configuration())

# Starten d. Kameravorschau
# picam2.start_preview(Preview.QTGL) # Bei Remote-Desktop Verbindung QTGL nicht möglich, nur via VNC-Verbindung QTGL möglich
picam2.start_preview(Preview.QT)

# Starten d. Kamera
picam2.start()

# Manuelle Einstellung einzelner Kamera-Parameter
with picam2.controls as ctrl:
#    Automatische Belichtung deaktivieren
     ctrl.AeEnable = False
#    Automatischen Weißabgleich deaktivieren
     ctrl.AwbEnable = False
#    Analoger Gain (Helligkeit ohne Rauschen) einstellen
     ctrl.AnalogueGain = 2.0
#    Belichtungszeit in Mikrosekunden (500 bedeutet 0.5ms) einstellen
     ctrl.ExposureTime = 3000
#    Rauschreduktion aktivieren (Modus 4)
     ctrl.NoiseReductionMode = 4
#    Bildschärfe einstellen
     ctrl.Sharpness = 6

# Kamera ist mit den festgelegten Einstellungen und dem Tuning-File konfiguriert
time.sleep(2)
print("Bildaufnahme gestartet")

# Speicherverzeichnis erstellen (falls nicht vorhanden)
SAVE_PATH = '/home/aviator/Desktop/Bildsequenz'
os.makedirs(SAVE_PATH, exist_ok=True)

# Bilder in Schleife als .jpg speichern
for i in range(10):        # Anzahl der Bilder, die aufgenommen werden soll (variabel)
    picam2.capture_file(f'{SAVE_PATH}/image_{i}.jpg') # Speichern der Bilder mit fortlaufendem Index als image_i.jpg
    time.sleep(1)          # Zeitintervall zwischen den Bildern, 1 Sekunde (variabel)

# Kamera stoppen
picam2.stop()