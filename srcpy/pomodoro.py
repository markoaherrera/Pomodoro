# -*- coding: utf-8 -*-

import timer
import alerter

from timer import temporizar
from alerter import alertar

if __name__ == "__main__":
    cont = "Y"
    while (cont == "Y"):
        print "Starting work of 25 mins"
        temporizar(25)
        alertar(5)
        want = raw_input("Want to stop? y/n")
        if want.upper == "Y":
            break
        want = raw_input("Want a long break? y/n")
        if (want.upper == "Y"):
            print "Starting long break of 15 mins"
            temporizar(15)
            alertar(10)
        else:
            print "Starting break of 5 mins"
            temporizar(5)
            alertar(5)
