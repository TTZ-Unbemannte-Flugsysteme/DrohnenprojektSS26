#!/usr/bin/python3

"""
Beschreibung: Programm zur Bildaufnahme mit synchronisierten Telemetrie-Daten (z.B. Batteriestatus) und Abspeichern in CSV-Datei
Anpassbare Parameter:
- Anzahl der Bilder: Zeile 34
- Zeitintervall zwischen den Bildaufnahmen: Zeile 53
- Dateispeicherort: Zeile 18
"""

import asyncio
from mavsdk import System           # Bibliothek zur Kommunikation mit der Drohne (Pixhawk)
from picamera2 import Picamera2     # Kamerasteuerung
from datetime import datetime       # Für Zeitstempel der Bilder
import os                           # Für Speicherverzeichnis

# Speicherverzeichnis erstellen (falls nicht vorhanden)
SAVE_PATH = '/home/aviator/Desktop/battery_images'
os.makedirs(SAVE_PATH, exist_ok=True)

# Kamera initialisieren
picam2 = Picamera2()

async def main():
    # Drohnenobjekt initialisieren und Verbindung herstellen
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyAMA0:57600")
    print("Verbunden mit Pixhawk --> Abruf von Telemetriedaten")

    # Kamera starten
    picam2.start()

    # Bilder aufnehmen und dazugehörige Telemetriedaten speichern
    for i in range(3):  # Anzahl der Bilder (anpassbar)
        # Zeitstempel für fortlaufenden Bildnamen erzeugen
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = f'image_{timestamp}.jpg'
        
        # Bild im gewählten Verzeichnis speichern
        picam2.capture_file(f'{SAVE_PATH}/{image_filename}')

        # Batteriestatus abrufen
        battery_data = await get_battery_status(drone)

        # Synchronisierte Telemetriedaten (Batteriestatus) in eine CSV-Datei schreiben
        with open(f"{SAVE_PATH}/image_battery_log.csv", "a") as log_file:
            log_file.write(f"{image_filename}, {round(battery_data.voltage_v, 2)}V, {battery_data.remaining_percent}%\n")
        
        print(f"Bild {image_filename} gespeichert mit Batteriestatus: {round(battery_data.voltage_v, 2)}V, "
              f"{battery_data.remaining_percent}%.")

        # Zeitintervall zwischen Bildaufnahmen (anpassbar)
        await asyncio.sleep(3)  # 10 Sekunden Pause zwischen den Aufnahmen

    # Kamera stoppen
    picam2.stop()

async def get_battery_status(drone):
    """
    Auslesen des aktuellen Batteriestatus (Spannung und verbleibende Prozent)
    von der Drohne mithilfe der MAVSDK-Telemetrie.
    """
    async for battery in drone.telemetry.battery():
        return battery

# Hauptfunktion starten (asyncio Event Loop)
asyncio.run(main())
