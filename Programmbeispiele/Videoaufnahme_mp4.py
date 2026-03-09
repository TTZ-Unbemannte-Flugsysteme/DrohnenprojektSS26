'''
Beschreibung: Programm zur Aufnahme eines Videos im mp4-Format + Laden von Kamera-Einstellungen mit einem Tuning-File
Variable Parameter: Dateispeicherort (Zeile 45 und Videolänge (Zeile 52)
'''

#!/usr/bin/python3
from picamera2 import Picamera2, Preview
from picamera2.controls import Controls
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import time
import os

# Laden eines Tuning-Files
tuning = Picamera2.load_tuning_file("imx708.json") # Für Raspberry Pi Kamera IR "imx708_noir.json" --> Tuning-Files in /usr/share/libcamera/ipa/rpi/pisp

# Erstellen und Konfigurieren der Kamera mit dem geladenen Tuning-File
picam2 = Picamera2(tuning=tuning)
picam2.configure(picam2.create_preview_configuration())

# Starten d. Kameravorschau
# picam2.start_preview(Preview.QTGL) # Bei Remote-Desktop Verbindung QTGL nicht möglich, bei VNC-Verbindung schon
picam2.start_preview(Preview.QT)

# Manuelle Einstellung einzelner Kamera-Parameter
with picam2.controls as ctrl:
#    Automatische Belichtung deaktivieren
     ctrl.AeEnable = False
#    Automatischen Weißabgleich deaktivieren
     ctrl.AwbEnable = False
#    Analoger Gain (Helligkeit ohne Rauschen) einstellen
     ctrl.AnalogueGain = 6.0
#    Belichtungszeit in Mikrosekunden (500 bedeutet 0.5ms) einstellen
     ctrl.ExposureTime = 3000
#    Rauschreduktion aktivieren (Modus 4)
     ctrl.NoiseReductionMode = 4
#    Bildschärfe einstellen
     ctrl.Sharpness = 6

# Kamera ist mit den festgelegten Einstellungen und dem Tuning-File konfiguriert
time.sleep(2)
print("Bildaufnahme starten")

# Speicherverzeichnis erstellen (falls nicht vorhanden)
SAVE_PATH = '/home/aviator/Desktop/Video'
os.makedirs(SAVE_PATH, exist_ok=True)

encoder = H264Encoder(10000000)
output = FfmpegOutput(f'{SAVE_PATH}/test.mp4')

picam2.start_recording(encoder, output)
time.sleep(10)
picam2.stop_recording()