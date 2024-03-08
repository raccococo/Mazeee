from tof import *
from serial_test import *
import time
from percorso import *

complete=000000.000000
complete=str(complete).encode('utf-8')

while True:
    messaggio_da_inviare = input("Inserisci il messaggio da inviare: ")
    if messaggio_da_inviare == "a":
        calcolo_posizione("a")
        sonoUnaFnCarinaCaruccia(messaggio_da_inviare.encode('utf-8'))
    elif messaggio_da_inviare == "w":
        sonoUnaFnCarinaCaruccia(messaggio_da_inviare.encode('utf-8'))
    elif messaggio_da_inviare == "q":
        sonoUnaFnCarinaCaruccia(messaggio_da_inviare.encode('utf-8'))