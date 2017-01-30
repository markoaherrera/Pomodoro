# -*- coding: utf-8 -*-

import time
import sys

def temporizar(tiempo):
    t = 0
    while (t < tiempo):
        print "Minuto {}".format(t)
        time.sleep(60)
        t = t + 1

if __name__ == "__main__":
    mins = 0
    if len(sys.argv) > 1:
        mins = int(sys.argv[1])
    mensaje = "Ejecutando temporizador de {0} minutos"
    if mins is not None and mins > 0:
        print mensaje.format(mins)
        temporizar(mins)
    else:
        print mensaje.format(10)
        temporizar(10)
