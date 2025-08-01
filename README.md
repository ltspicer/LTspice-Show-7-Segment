![Screenshot](https://github.com/ltspicer/LTspice-Show-7-Segment/blob/main/screenshot.png)

Deutsch:

Visualisierung von 7-Segment Anzeige aus LTspice-Plot (Python3 Programm)

Benötigt: Python3.7+ (Windows User müssen Python3.7 oder höher installieren / In Linux ist das bereits vorinstalliert, wobei da ev pip installiert werden muss >> sudo apt install python3-pip)

Siehe: https://bodo-schoenfeld.de/installation-von-python-unter-windows-10/

Fehlende Bibliotheken werden automatisch beim Erststart installiert.
Falls tkinter fehlt, wird im Terminal darauf hingewiesen und die notwendigen Befehle angezeigt.

Die s7s_DE.exe benötigt keine Installationen/Einstellungen!

Jede der Segmentspannungen V(a) .. V(g), steuern dabei ein Segment an; die Spannungen V(RBO) und V(Carryout) steuern zwei "LEDs" auf der rechten Seite an. Diese Spannungen entnimmt das Programm der (exportierten) Text-Datei, die die Simulationsergebnisse enthält. Die Text-Datei exportiert man folgendermaßen:

Nach der Simulation klicke auf das Plot-Fenster und dann auf File / "Export data as text". Dort wählst Du die oben benannten Spannungen aus. Als Dateiname wird der Name der Simulation mit der Endung .txt vorgeschlagen. Das Programm sucht später in der Kopfzeile der Text-Datei nach diesen Spannungen, merkt sich die jeweilige Spalte und zeigt sie an. Die Spalten-Bezeichnungen können ggf in den Einstellungen im ersten Fenster angepasst werden. Es können auf Wunsch noch 2 weitere Signale verarbeitet werden (x1 und x2).

Dann starte das Programm s7s.py (oder s7s_DE.exe).

Nach dem Aufruf, dem Öffnen der txt Datei und ev weiteren Anpassungen, auf "Fertig" drücken. Meistens passen die Voreinstellungen. Sonst ggf anpassen. Nun wird die 7-Segment-Anzeige und die 4 zusätzlichen LEDs animiert.

Startzeit: Anfang des betrachteten Zeitbereichs in Sekunden (voreingestellt: 0.0000)

Stopzeit: Ende des betrachteten Zeitbereichs in Sekunden (voreingestellt: 999.9999)

Abtastintervall: In diesem Zeitintervall in Sekunden wird die exportierte txt Datei "abgetastet". Bei einem Clock von 1 ms wäre hier z.B. Intervall=0.001 sinnvoll. (voreingestellt: 0.001)

Verzögerung: Verzögerungszeit für die Anzeige aufeinanderfolgender Abtastungen, in Sekunden (voreingestellt: 0.2)

H/L Schwelle: Höhe der Hell/Dunkel-Schwelle in V (voreingestellt: 2.5)

nun die weniger wichtigen Eintragungen:

Farbe hell: RGB-Wert für ein eingeschaltetes Digit, (V(x) >= Schwelle). (voreingestellt: FF4000)
  
Farbe dunkel: RGB-Wert für ein ausgeschaltetes Digit, (V(x) < Schwelle).(voreingestellt: C0C0C0)
  
nun noch die Spalten-Bezeichnungen wie in der txt eintragen.....wenn überhaupt nötig. Normalerweise passen diese "Labels", wenn die in LTspice so angegeben wurden ( V(a), V(b)....).

Wenn Du die Segmente/LEDs nur zu einem bestimmten Zeitpunkt betrachten willst - z.B. bei 1.45 ms - , dann gib zBsp Startzeit=0.00141 Stopzeit=0.00149 an....eine kleine Zeitspanne nach gesundem Menschenverstand einberechnen.

Desktop Icon: Linux-User können einen Starter anlegen (Typ: Anwendung, Befehl: s7s >> Bedingung ist, dass die s7s in /usr/local/bin ohne Endung .py gespeichert ist) und dieses Icon (7segment.png) dazu einpflegen.  

Datei zum testen: CD4033_test_9.10.21.txt 

-----------------------------------------
  
English:  

Visualization of 7-segment display from LTspice plots (Python3 program)

Requirements: Python3.7+ (Windows users need to install Python3.7 or higher / on Linux is it allways installed, where pip may have to be installed >> sudo apt install python3-pip)

See: https://bodo-schoenfeld.de/installation-von-python-unter-windows-10/
  
Missing libraries are automatically installed when the program is started for the first time.
If tkinter is missing, this will be pointed out in the terminal and the necessary commands will be displayed.

Edit first this line in the code to EN

language = "DE"     # Hier Sprache wählen (DE)  -  Select language here (EN)
  
to
  
language = "EN"     # Hier Sprache wählen (DE)  -  Select language here (EN)

The s7s_EN.exe does not require any installations/settings!

Each of the segment voltages V(a) .. V(g) control a segment; the voltages V(RBO) and V(carryout) control the two LEDs on the right side. The program takes these voltages from the exported text file that contains the simulation results. The text file is exported as follows: 

After the simulation click on the plot window and then on File / "Export data as text".
There you select the required voltages. The name of the simulation with the extension .txt is suggested as the file name. The program later searches for these voltages in the header of the text file, notes the respective column and displays it. If necessary, the column names can be adjusted in the settings in the first window. If desired, 2 further signals can be processed (x1 and x2).

Execute s7s.py now (or s7s_EN.exe).

After calling, open the desired txt file and making further adjustments. Then press "Complete". Most of the time the defaults are fine. Otherwise adjust if necessary. Now the 7-segment and the 4 additional LEDs are animated.

Start time: Start of the considered time range in seconds (preset: 0.0000)
  
Stop time: End of the considered time range in seconds (preset: 999.9999)
  
Sampl. interval: The exported txt file is "sampled" in this time interval in seconds. With a clock of 1 ms, for example, interval = 0.001 would make sense here. (default: 0.001)
  
Delay: Delay time for the display of successive samples, in seconds (preset: 0.2)
  
H/L threshold: H/L threshold for light/dark in V (preset: 2.5)
  
Now the less important entries:
  
Colour light: RGB value for an activated digit, (V(x) >= Threshold). (preset: FF4000)
  
Colour dark: RGB value for a deactivated digit, (V(x) < Threshold). (preset: C0C0C0)
  
Now enter the column names as in the txt .....if needed. Normally these "labels" are suitable if they have been specified in LTspice like this (V(a), V(b), ...).

Desktop Icon: Linux users can create a starter (type: application, command: s7s >> the condition is that the s7s is stored in /usr/local/bin (without .py)) and add this icon (7segment.png).

File for testing: CD4033_test_9.10.21.txt

-----------------------------------------

  Home of this source: https://www.ltspiceusers.ch/threads/visualisierung-von-7-segment-anzeige-aus-ltspice-plot-python3-programm.827/#post-2220
