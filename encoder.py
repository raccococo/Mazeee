import time
import numpy as np
from gpiozero import RotaryEncoder
from serial_test import *

# Assigning parameter values
ppr = 300.8  # Pulses Per Revolution of the encoder
tstop = 20  # Loop execution duration (s)
tsample = 0.02  # Sampling period for code execution (s)
tdisp = 0.5  # Sampling period for values display (s)

# Creating encoder object using GPIO pins 24 and 25
encoder = RotaryEncoder(22, 27, max_steps=0)

# Initializing previous values and starting main clock
anglecurr = 0
tprev = 0
tcurr = 0
tstart = time.perf_counter()
#30 gradi sono 143
# 90 gradi reali sono 430 falsi
#360 reali == 1720 falsi
#1377 per farlo fermare esattamente a 360 gradi

while True:
    time.sleep(tsample)
    anglecurr = 360 / ppr * encoder.steps
    print("Angle = {:0.0f} deg".format(anglecurr))
    if(anglecurr<-1377*1.1): #serve 1.44 per arrivare a 30cm, cioè un giro completo più 0.44 giri
        q="q"
        sonoUnaFnCarinaCaruccia(q.encode('utf-8'))
        break
