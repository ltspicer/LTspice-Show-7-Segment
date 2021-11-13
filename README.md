Deutsch:

Visualisierung von 7-Segment Anzeige aus LTspice-Plot (Python3 Programm)

Benötigt: Python3.7+ (Windows User müssen Python3.7 oder höher installieren / In Linux ist das bereits vorinstalliert)

Siehe: https://bodo-schoenfeld.de/installation-von-python-unter-windows-10/

Fehlende Bibliotheken werden automatisch beim Erststart installiert.

Jede der Segmentspannungen V(a) .. V(g), steuern dabei ein Segment an; die Spannungen V(RBO) und V(Carryout) steuern zwei "LEDs" an. Diese Spannungen entnimmt das Programm einer Text-Datei, die die Simulationsergebnisse enthält. Die Text-Datei exportiert man folgendermaßen:

Nach der Simulation klicke auf das Plot-Fenster und dann auf File / Export. Dort wählst Du die oben benannten Spannungen aus. Als Dateiname wird der Name der Simulation mit der Endung .txt vorgeschlagen. Das Programm sucht später in der Kopfzeile der Text-Datei nach diesen Spannungen, merkt sich die jeweilige Spalte und zeigt sie an. Die Spalten-Bezeichnungen können ggf in den Einstellungen im ersten Fenster angepasst werden. Es können auf Wunsch noch 2 weitere Signale verarbeitet werden (x1 und x2).

Dann starte das Programm s7s.py.

Nach dem Aufruf, dem Öffnen der txt Datei und ev weiteren Anpassungen, auf "Fertig" drücken. Meistens passen die Voreinstellungen. Sonst ggf anpassen. Nun wird die 7-Segment-Anzeige und die 4 zusätzlichen LEDs animiert.

Startzeit Anfang des betrachteten Zeitbereichs in Sekunden, siehe Plot-Fenster (voreingestellt: 0.0000)

Stopzeit Ende des betrachteten Zeitbereichs in Sekunden (voreingestellt: 999.9999)

Abtastintervall In diesem Zeitintervall in Sekunden wird die exportierte txt Datei "abgetastet". Bei einem Clock von 1 ms wäre hier z.B. Intervall=0.001 sinnvoll. (voreingestellt: 0.001)

Verzögerung Verzögerungszeit für die Anzeige aufeinanderfolgender Abtastungen, in Sekunden (voreingestellt: 0.2)

H/L Schwelle Höhe der Hell/Dunkel-Schwelle in V (voreingestellt: 2.5)

nun die weniger wichtigen Eintragungen:

Farbe hell RGB-Wert für ein eingeschaltetes Digit, (V(<Segment>) >= <Schwelle>). (voreingestellt: FF4000)
  
Farbe dunkel RGB-Wert für ein ausgeschaltetes Digit, (V(<Segment>) < <Schwelle>).(voreingestellt: C0C0C0)
  
nun noch die Spalten-Bezeichnungen wie in der txt eintragen.....wenn überhaupt nötig. Normalerweise passen diese "Labels", wenn die in LTspice so angegeben wurden ( V(a), V(b)....).

Wenn Du die Segmente/LEDs nur zu einem bestimmten Zeitpunkt betrachten willst - z.B. bei 1.45 ms - , dann gib zBsp Startzeit=0.00141 Stopzeit=0.00149 an....eine kleine Zeitspanne nach gesundem Menschenverstand einberechnen.

Desktop Icon: Linux-User können einen Starter anlegen (Typ: Anwendung, Befehl: s7s >> Bedingung ist, dass die s7s in /usr/local/bin gespeichert ist) und dieses Icon (7segment.png) dazu einpflegen.  
  
-----------------------------------------
  
English:  

Visualization of 7-segment display from LTspice plots (Python3 program)

Requirements: Python3.7+ (Windows users need to install Python3 / on Linux is it allways installed)
  
See: https://bodo-schoenfeld.de/installation-von-python-unter-windows-10/
  
Missing libraries are automatically installed when the program is started for the first time.

Edit first this line in the code to EN

language = "DE"     # Hier Sprache wählen (DE)  -  Select language here (EN)
  
to
  
language = "EN"     # Hier Sprache wählen (DE)  -  Select language here (EN)
  
After the simulation click on the plot window and then on File / Export.
There you select the required voltages.
Export to the txt file.
  
Start time: Start of the considered time range in seconds, see plot window (preset: 0.0000)
  
Stop time: End of the considered time range in seconds (preset: 999.9999)
  
Sampl. interval: The exported txt file is "sampled" in this time interval in seconds. With a clock of 1 ms, for example, interval = 0.001 would make sense here. (default: 0.001)
  
Delay: Delay time for the display of successive samples, in seconds (preset: 0.2)
  
H/L threshold: H/L threshold for light/dark in V (preset: 2.5)
  
now the less important entries:
  
Colour light: RGB value for an activated digit, (V (<Segment>)> = <Threshold>). (preset: FF4000)
  
Colour dark: RGB value for a deactivated digit, (V (<Segment>) <<Threshold>). (preset: C0C0C0)
  
now enter the column names as in the txt .....if needed.

Desktop Icon: Linux users can create a starter (type: application, command: s7s >> the condition is that the s7s is stored in /usr/local/bin) and add this icon (7segment.png).

  
  Home of this source: https://www.ltspiceusers.ch/threads/visualisierung-von-7-segment-anzeige-aus-ltspice-plot-python3-programm.827/#post-2220
