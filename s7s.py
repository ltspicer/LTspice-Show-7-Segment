#!/usr/bin/python3

################################
# Show 7 Segment V2.3          #
# von Daniel Luginbuehl        #
# (C) 2025 www.ltspiceusers.ch #
# webmaster@ltspiceusers.ch    #
################################

# Sprache/Language DE/EN

LANGUAGE = "DE"     # Hier Sprache wählen (DE)  -  Select language here (EN)

####
#### Folgend keine Änderungen mehr machen!
####


# Ist pandas installiert? Sonst installieren

try:
    import pandas as pd
except ImportError as e:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas', '--break-system-packages'])

try:
    import tkinter as tk
except ImportError as e:
    print("Install tkinter first!")
    print("Debian: sudo apt-get install python3-tk")
    print("Fedora: sudo dnf install python3-tkinter")
    print("CentOS: sudo yum install python3-tkinter")
    print("MacOS: brew install python-tk@3.10  << enter correct Python version!")
    print("Windows: See https://www.activestate.com/products/python/")
    exit()

import os
import tkinter as tk
import pandas as pd
import time
from tkinter.ttk import Frame, Label, Button
from tkinter.filedialog import askopenfile
#from tkinter import Canvas, Button


if LANGUAGE == "DE":

    # Deutsche Phrasen

    TEXTDATEIEN = "Text Dateien"
    KEINE_DATEI = "Keine Datei ausgewählt"
    TITEL       = "Show 7 Segment"
    FERTIG_PH   = "Fertig"
    OEFFNEN     = "Öffnen"
    BEENDE      = "Beenden"
    SETTINGS    = "Einstellungen"
    FEHLER      = "Fehler"
    SEG_FEHLER  = ' Es fehlt ein oder mehrere Segment(e) oder ist/sind falsch gelabelt! \n Prüfe die Felder "Segment A" bis "Segment G"'
    PH_PAUSE    = "Pause/Weiter"
    PH_ZURUCK   = "Zu Einstellungen zurück"
    PH_RICHTUNG = "Richtung ändern"

    fields = 'Startzeit (s)', 'Stopzeit (s)', 'Abtastintervall (s)', 'Verzögerung (s)', 'H/L Schwelle (V)', 'Segment A', 'Segment B', 'Segment C', 'Segment D', 'Segment E', 'Segment F', 'Segment G', 'CarryOut', 'RBO', 'Farbe dunkel', 'Farbe hell', 'x1', 'x2', 'Zeit'

else:

    # English phrases

    TEXTDATEIEN = "Text files"
    KEINE_DATEI  = "No file selected"
    TITEL       = "Show 7 Segment"
    FERTIG_PH   = "Complete"
    OEFFNEN     = "Open"
    BEENDE      = "Exit"
    SETTINGS    = "Settings"
    FEHLER      = "Error"
    SEG_FEHLER  = ' One or more segments are missing or incorrectly labeled! \n Check the fields "Segment A" to "Segment G"'
    PH_PAUSE    = "Pause/Continue"
    PH_ZURUCK   = "Back to settings"
    PH_RICHTUNG = "Change direction"

    fields = 'Start time (s)', 'Stop time (s)', 'Sampl. interval (s)', 'Delay (s)', 'H/L threshold (V)', 'Segment A', 'Segment B', 'Segment C', 'Segment D', 'Segment E', 'Segment F', 'Segment G', 'CarryOut', 'RBO', 'Colour dark', 'Color light', 'x1', 'x2', 'Time'


# Vorgabewerte

fields_content = '0.0000', '999.9999', '0.001', '0.200', '2.5', 'V(a)', 'V(b)', 'V(c)', 'V(d)', 'V(e)', 'V(f)', 'V(g)', 'V(carryout)', 'V(rbo)', 'C0C0C0', 'FF4000', 'x1', 'x2', 'time'
FILENAME = " "
CONTENT = ""
FILE = ""

def open_file():
    global CONTENT
    global FILE
    global FILENAME
    FILE = askopenfile(mode ='r', filetypes =[(TEXTDATEIEN, '*.txt')])
    if FILE is not None:
        CONTENT = FILE.read()

        FILENAME = os.path.basename(str(FILE))
        file_name = FILENAME
        index = file_name.index("'")
        FILENAME = file_name[:index]
        textausgabe = tk.Label(fenster, text=FILENAME, bg="yellow", height=1, width=30)
        textausgabe.grid(row=11, column=0)

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()

def makeform(fenster, fields, standard):
    entries = []
    row1=1
    row2=1
    columns=len(fields)
    for field in fields:
        if row1<=(columns/2):
            column1=0
            row2=row1
        else:
            column1=3
            row2=row1+1-(int((columns+1)/2)+1)
        row = Frame(fenster)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        ent.insert(10, standard[row1-1])
        row.grid(row=row2, column=column1, padx='5', pady='5')
        lab.grid(row=row2, column=column1)
        ent.grid(row=row2, column=column1+1)
        entries.append((field, ent))
        row1=row1+1
    return entries

def default(fields2):
    entries = []
    for field in fields2:
        entries.append((field))
    return entries

def fertig(entries):
    global fields_content
    fields_content = []
    for entry in entries:
        text  = entry[1].get()
        fields_content.append((text))
    if len(FILENAME)<4:
        textausgabe = tk.Label(fenster, text=KEINE_DATEI, bg="yellow", height=1, width=30)
        textausgabe.grid(row=11, column=0)
        return
    fenster.destroy()

def digA(screen,hell,dunkel,on):
    screen.itemconfigure(id_sa, fill= hell if on else dunkel)

def digB(screen,hell,dunkel,on):
    screen.itemconfigure(id_sb, fill= hell if on else dunkel)

def digC(screen,hell,dunkel,on):
    screen.itemconfigure(id_sc, fill= hell if on else dunkel)

def digD(screen,hell,dunkel,on):
    screen.itemconfigure(id_sd, fill= hell if on else dunkel)

def digE(screen,hell,dunkel,on):
    screen.itemconfigure(id_se, fill= hell if on else dunkel)

def digF(screen,hell,dunkel,on):
    screen.itemconfigure(id_sf, fill= hell if on else dunkel)

def digG(screen,hell,dunkel,on):
    screen.itemconfigure(id_sg, fill= hell if on else dunkel)

def digCO(screen,hell,dunkel,on):
    screen.itemconfigure(id_sco, fill= hell if on else dunkel)

def digRBO(screen,hell,dunkel,on):
    screen.itemconfigure(id_srbo, fill= hell if on else dunkel)

def digX1(screen,hell,dunkel,on):
    screen.itemconfigure(id_sx1, fill= hell if on else dunkel)

def digX2(screen,hell,dunkel,on):
    screen.itemconfigure(id_sx2, fill= hell if on else dunkel)

def zeitanzeige(screen,on,akt_zeit):
    akt_zeit = str(akt_zeit)+" ms"
    screen.itemconfigure(id_zeitanzeige, text=akt_zeit, fill= "black", state = 'normal' if on else 'hidden')

def ausgabe(tabellen_index):

    if tabelle[sa].values[tabellen_index] >= schwelle:
        digA(screen,hell,dunkel,1)
    else:
        digA(screen,hell,dunkel,0)

    if tabelle[sb].values[tabellen_index] >= schwelle:
        digB(screen,hell,dunkel,1)
    else:
        digB(screen,hell,dunkel,0)

    if tabelle[sc].values[tabellen_index] >= schwelle:
        digC(screen,hell,dunkel,1)
    else:
        digC(screen,hell,dunkel,0)

    if tabelle[sd].values[tabellen_index] >= schwelle:
        digD(screen,hell,dunkel,1)
    else:
        digD(screen,hell,dunkel,0)

    if tabelle[se].values[tabellen_index] >= schwelle:
        digE(screen,hell,dunkel,1)
    else:
        digE(screen,hell,dunkel,0)

    if tabelle[sf].values[tabellen_index] >= schwelle:
        digF(screen,hell,dunkel,1)
    else:
        digF(screen,hell,dunkel,0)

    if tabelle[sg].values[tabellen_index] >= schwelle:
        digG(screen,hell,dunkel,1)
    else:
        digG(screen,hell,dunkel,0)

    if tabelle[sco].values[tabellen_index] >= schwelle:
        digCO(screen,hell,dunkel,1)
    else:
        digCO(screen,hell,dunkel,0)

    if tabelle[srbo].values[tabellen_index] >= schwelle:
        digRBO(screen,hell,dunkel,1)
    else:
        digRBO(screen,hell,dunkel,0)

    if tabelle[sx1].values[tabellen_index] >= schwelle:
        digX1(screen,hell,dunkel,1)
    else:
        digX1(screen,hell,dunkel,0)

    if tabelle[sx2].values[tabellen_index] >= schwelle:
        digX2(screen,hell,dunkel,1)
    else:
        digX2(screen,hell,dunkel,0)


    #Zeitanzeige ausgeben

    akt_zeit = float(int(float(tabelle[stime].values[tabellen_index]) * 1000000000)) / 1000000
    akt_zeit = "{:.6f}".format(akt_zeit)
    zeitanzeige(screen,1,akt_zeit)

    fenster2.update()

def stop():
    global RUNNING
    if RUNNING == 1:
        RUNNING = 0
    else:
        RUNNING = 1

def richtung():
    global DIRECTION
    if DIRECTION == 1:
        DIRECTION = -1
    else:
        DIRECTION = 1

def zuruck():
    global ZURUCK_STATUS
    ZURUCK_STATUS=1

def zuruck2():
    global ZURUCK_STATUS
    fenster2.destroy()
    ZURUCK_STATUS=1

def beenden():
    fenster.destroy()
    exit()

def beenden2():
    fenster2.destroy()
    exit()

def eingabefenster():
    global fenster
    fenster = tk.Tk()
    fenster.title(TITEL)
    fenster.geometry('600x410')
    ents = makeform(fenster, fields, standard)
    fenster.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b2 = Button(fenster, text=FERTIG_PH, command=lambda e=ents: fertig(e))
    b2.grid(column=3, row=10, padx='5', pady='5')
    br = Button(fenster, text =OEFFNEN, command=lambda e=ents: open_file())
    br.grid(column=0, row=10, padx='5', pady='5')
    beenden_button = Button(fenster, text =BEENDE, command = beenden)
    beenden_button.grid(column=3, row=11)
    textausgabe_titel = tk.Label(fenster, text=SETTINGS,height=1, width=30)
    textausgabe_titel.grid(row=0, column=0)
    textausgabe_filename = tk.Label(fenster, text=FILENAME, bg="yellow", height=1, width=30)
    textausgabe_filename.grid(row=11, column=0)
    fenster.mainloop()


standard = default(fields_content)


#### Hauptschleife

while True:

    #### Einstellungs-Fenster

    eingabefenster()
    standard = default(fields_content)


    #### Benennung der Spalten holen und speichern

    start=standard[0]
    ende=standard[1]
    intervall=standard[2]
    delay=standard[3]
    schwelle=standard[4]
    sa=standard[5]
    sb=standard[6]
    sc=standard[7]
    sd=standard[8]
    se=standard[9]
    sf=standard[10]
    sg=standard[11]
    sco=standard[12]
    srbo=standard[13]
    dunkel="#" + standard[14]
    hell="#" + standard[15]
    sx1=standard[16]
    sx2=standard[17]
    stime=standard[18]
    DIRECTION=1


    #### Tabelle lesen und aufbereiten

    tabelle = pd.read_csv(FILE.name, sep="\t")
    ZURUCK_STATUS=0
    N=1
    END=2
    if sx1 not in tabelle.columns :
        tabelle[sx1] = float(0)

    if sx2 not in tabelle.columns :
        tabelle[sx2] = float(0)

    if sco not in tabelle.columns :
        tabelle[sco] = float(0)

    if srbo not in tabelle.columns :
        tabelle[srbo] = float(0)

    if not {sa, sb, sc, sd, se, sf, sg, sco, srbo, sx1, sx2, stime}.issubset(tabelle.columns):
        fenster = tk.Tk()
        fenster.title(FEHLER)
        error = Label(fenster, text=SEG_FEHLER)
        error.grid()
        fenster.mainloop()
        zuruck()

    if ZURUCK_STATUS==0:
        anzahl_zeilen=tabelle.shape[0]
        start=float(start)
        ende=float(ende)
        schwelle=float(schwelle)
        delay=float(delay)*1000


        # Benennung der Spalten  in Variable standard[array]
        # Tabellen inhalt        in Variable tabelle

        # Start-Index holen
        df_mask=tabelle[stime] > start
        filtered_df2 = tabelle[df_mask].head(1)
        filtered_df = filtered_df2.index[0]
        start_index = filtered_df

        # End-Index holen
        df_mask=tabelle[stime] < ende
        filtered_df2 = tabelle[df_mask]
        filtered_df = filtered_df2.index[-1]
        end_index = filtered_df

        # Zeit am Tabellenende holen
        letzter_index = tabelle[stime].index[-1]
        zeit_letzter_index = tabelle[stime].values[letzter_index]

        # Intervall berechnen
        schrittweite = int(float(letzter_index) * float(intervall) / float(zeit_letzter_index) + 0.5)

        N=start_index
        END = end_index


        #### Grafische Ausgabe

        fenster2 = tk.Tk()
        fenster2.title(TITEL)
        fenster2.geometry('350x395')

        screen = tk.Canvas(fenster2)
        screen.grid()

        # Linke obere Ecke der Linien/Symbolen im Fenster
        X=8
        Y=4

        # Texte erstellen
        screen.create_text(X +250, Y + 30, text=sco, fill=hell)
        screen.create_text(X +250, Y + 90, text=srbo, fill=hell)
        screen.create_text(X +250, Y + 150, text=sx1, fill=hell)
        screen.create_text(X +250, Y + 210, text=sx2, fill=hell)

        # Segmente erstellen
        LENGHT=20
        WIDTH=6
        x0, y0, x1, y1 = 0, 0, 6, 0
        L = LENGHT
        id_sa = screen.create_line(
            X + x0*L, Y + y0*L, X + x1*L, Y + y1*L,
            width=WIDTH, fill = dunkel)

        LENGHT=20
        WIDTH=6
        x0, y0, x1, y1 = 6, 0, 6, 6
        L = LENGHT
        id_sb = screen.create_line(
            X + x0*L, Y + y0*L, X + x1*L, Y + y1*L,
            width=WIDTH, fill = dunkel)

        LENGHT=20
        WIDTH=6
        x0, y0, x1, y1 = 6, 6, 6, 12
        L = LENGHT
        id_sc = screen.create_line(
            X + x0*L, Y + y0*L, X + x1*L, Y + y1*L,
            width=WIDTH, fill = dunkel)

        LENGHT=20
        WIDTH=6
        x0, y0, x1, y1 = 0, 12, 6, 12
        L = LENGHT
        id_sd = screen.create_line(
            X + x0*L, Y + y0*L, X + x1*L, Y + y1*L,
            width=WIDTH, fill = dunkel)

        LENGHT=20
        WIDTH=6
        x0, y0, x1, y1 = 0, 6, 0, 12
        L = LENGHT
        id_se = screen.create_line(
            X + x0*L, Y + y0*L, X + x1*L, Y + y1*L,
            width=WIDTH, fill = dunkel)

        LENGHT=20
        WIDTH=6
        x0, y0, x1, y1 = 0, 0, 0, 6
        L = LENGHT
        id_sf = screen.create_line(
            X + x0*L, Y + y0*L, X + x1*L, Y + y1*L,
            width=WIDTH, fill = dunkel)

        LENGHT=20
        WIDTH=6
        x0, y0, x1, y1 = 0, 6, 6, 6
        L = LENGHT
        id_sg = screen.create_line(
            X + x0*L, Y + y0*L, X + x1*L, Y + y1*L,
            width=WIDTH, fill = dunkel)

        id_sco = screen.create_rectangle(X + 126, Y + 0, X + 182, Y + 56, fill = dunkel)

        id_srbo = screen.create_rectangle(X + 126, Y + 60, X + 182, Y + 116, fill = dunkel)

        id_sx1 = screen.create_rectangle(X + 126, Y + 120, X + 182, Y + 176, fill = dunkel)

        id_sx2 = screen.create_rectangle(X + 126, Y + 180, X + 182, Y + 236, fill = dunkel)


        #Buttons erstellen

        RUNNING = 1
        stopButton = Button(fenster2, text = PH_PAUSE, command = stop)
        stopButton.grid(column=0, row=3)

        richtungButton = Button(fenster2, text = PH_RICHTUNG, command = richtung)
        richtungButton.grid(column=0, row=4)

        zuruckButton = Button(fenster2, text = PH_ZURUCK, command = zuruck2)
        zuruckButton.grid(column=0, row=5)

        beendenButton = Button(fenster2, text = BEENDE, command = beenden2)
        beendenButton.grid(column=0, row=6)


        #Zeitanzeige erstellen

        aktuelle_zeit = start
        id_zeitanzeige = screen.create_text(X +250, Y + 235, text=aktuelle_zeit, fill="black")


        # Live Verarbeitung Anzeigen/Ausgeben. n = Tabellenindex (Tabellen-Zeilen)

        while True:
            if ZURUCK_STATUS==1:
                break
            ausgabe(N)
            if RUNNING == 1:
                N=N + schrittweite*DIRECTION
                if N <= 0:
                    N=0
                if N >= END:
                    N=END
            time.sleep(delay/1000)

        fenster2.mainloop()
