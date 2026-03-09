'''
Beschreibung: Programm zum Zählen von erkannten Farbobjekten Blau, Rot und Gelb
Anpassbare Parameter: Hinzufügen von Farbprofilen
'''

import cv2
from picamera2 import Picamera2

# Definieren von Farbprofilen für die Farberkennung
def colorProfiles(n):
    if n == 0:
        name = "Blau"
        hsv_lower = (95,100,100)
        hsv_upper = (115,255,255)
        return (name,hsv_lower,hsv_upper)
    if n == 1:
        name = "Rot"
        hsv_lower = (160,100,100)
        hsv_upper = (180,255,255)
        return (name,hsv_lower,hsv_upper)
    if n == 2:
        name = "Gelb"
        hsv_lower = (15, 100, 100)
        hsv_upper = (35, 255, 255)
        return (name,hsv_lower,hsv_upper)
    if n == 3:
        name = "Rot2"
        hsv_lower = (0,100,100)
        hsv_upper = (12,255,255)
        return (name,hsv_lower,hsv_upper)

# Mindestfläche des zu erkennden Objekts (z.B. 3000 Pixel)
min_area = 3000                                         # mögliche Verbesserung durch dynamische Anpassung in Abhängigkeit von der Flughöhe

counter = 0

blueObject = False
redObject = False
yellowObject = False
redObject2 = False

# Starten eines neuen Threads für ein OpenCV-Fenster
cv2.startWindowThread()

#picam2 = Picamera2()
tuning = Picamera2.load_tuning_file("imx708.json")      # Für Raspberry Pi IR Kamera "imx708_noir.json"
picam2 = Picamera2(tuning=tuning)

picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
#
# picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (1280, 720)}))

picam2.start()

with picam2.controls as ctrl:
    ctrl.AeEnable = False       # Automatische Belichtung deaktivieren
    ctrl.AwbEnable = False      # Automatischen Weißabgleich deaktivieren
    ctrl.AnalogueGain = 9.0     # Helligkeit durch analogen Gain (ohne Rauschen) erhöhen
    ctrl.ExposureTime = 2300    # Belichtungszeit in Mikrosekunden (z. B. 2300 = 2.3ms)
    ctrl.NoiseReductionMode = 4 # Rauschreduzierung aktivieren
    ctrl.Sharpness = 6          # Bildschärfe einstellen

#time.sleep(2)
print("Starten der Bilderkennung")

while True:
    # Einlesen eines Frames von der Kamera
    im = picam2.capture_array()
        
    # Konvertieren des Bildes in den HSV-Farbraum
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    
    # Iterieren durch alle definierten Farben in colorProfiles
    for i in range(4):
        name, hsv_lower, hsv_upper = colorProfiles(i)
                
        mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
            
        # Erkennen von Konturen in der Maske
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            
        if contours:
            # Sortieren der Konturen nach Flächengröße (absteigend)
            biggest = sorted(contours, key=cv2.contourArea, reverse=True)[0]
            area = cv2.contourArea(biggest)
                
            # Überprüfen ob die Fläche der vorgegebenen Mindestgröße entspricht
            if area >= min_area:
                x, y, w, h = cv2.boundingRect(biggest)
                    
                # Einrahmen der erkannten Kontur
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    
                # Label mit Namen und Koordinaten im OpenCV Vorschaufenster
                text = f"{name} ({x}, {y})"
                cv2.putText(im, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                
                # Überprüfung der Flag für jede Farbe um sofortige mehrfachzählung zu vermeiden (Alternativ Kombination mit time.sleep um Wartezeit hinzuzufügen)
                if name == "Blau" and blueObject == False:
                    counter += 1
                    blueObject = True
                    print(f"Farbe: {name}, Counter: {counter}")
                elif name == "Rot" and redObject == False:
                    counter += 1
                    redObject = True
                    print(f"Farbe: {name}, Counter: {counter}")
                elif name == "Gelb" and yellowObject == False:
                    counter += 1
                    yellowObject = True
                    print(f"Farbe: {name}, Counter: {counter}")
                elif name == "Rot2" and redObject2 == False:
                    counter += 1
                    redObject2 = True
                    print(f"Farbe: {name}, Counter: {counter}")
                
            else:
                # Zurücksetzen der Flag bei zu kleiner Fläche
                if name == "Blau":
                    blueObject = False
                elif name == "Rot":
                    redObject = False
                elif name == "Gelb":
                    yellowObject = False
                elif name == "Rot2":
                    redObject2 = False
        else:
            # Zurücksetzen der Flag falls keine Kontur gefunden worden ist
            if name == "Blau":
                blueObject = False
            elif name == "Rot":
                redObject = False
            elif name == "Gelb":
                yellowObject = False
            elif name == "Rot2":
                redObject2 = False

    # Anzeigen des erkannten Objekts
    cv2.putText(im, f"Anzahl erkannter Objekte: {counter}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.imshow("HSV",hsv)
    cv2.imshow("Kamera Vorschau", im)

    # Beenden des Programms mit der Taste 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()