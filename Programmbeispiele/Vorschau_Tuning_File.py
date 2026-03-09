#!/usr/bin/python3

# picamera2-library Example of setting controls using Tuning-File and the "direct" attribute method.

'''
Beschreibung: Programm für Raspberry Pi Camera Vorschau mit Tuning-File
'''

from picamera2 import Picamera2, Preview
from picamera2.controls import Controls
import time

# Laden des Tuning-Files
tuning = Picamera2.load_tuning_file("imx708.json") # Für Raspberry Pi Kamera IR "imx708_noir.json" --> Tuning-Files in /usr/share/libcamera/ipa/rpi/pisp

# Erstellen und Konfigurieren der Kamera mit dem geladenen Tuning-File
picam2 = Picamera2(tuning=tuning)
picam2.configure(picam2.create_preview_configuration())

# Starten d. Kameravorschau
#picam2.start_preview(Preview.QTGL) # Bei Remote-Desktop Verbindung QTGL nicht möglich, bei VNC-Verbindung schon
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
     ctrl.AnalogueGain = 5.0
#    Belichtungszeit in Mikrosekunden (500 bedeutet 0.5ms) einstellen
     ctrl.ExposureTime = 3000
#    Rauschreduktion aktivieren (Modus 4)
     ctrl.NoiseReductionMode = 4
#    Bildschärfe einstellen
     ctrl.Sharpness = 6

# Kamera ist mit den festgelegten Einstellungen und dem Tuning-File konfiguriert
time.sleep(2)
print("Bildaufnahme gestartet")

time.sleep(30)

# Kamera stoppen
picam2.stop()