# -*- coding: utf-8 -*-

import sys
import timer
import alerter

from timer import temporizar
from alerter import alertar

if __name__ == "__main__":
    mins = 0
    if len(sys.argv) > 1:
        mins = int(sys.argv[1])
    mensaje = "Ejecutando temporizador de {0} minutos"
    if mins is not None and mins > 0:
        print mensaje.format(mins)
        temporizar(mins)
        alertar(5)
    else:
        print mensaje.format(10)
        temporizar(10)
        alertar(5)
