# -*- coding: utf-8 -*-

import sys
import winsound

def alertar(reps):
    t = 0
    print "playing {} reps".format(reps)
    while (t < reps):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        t = t + 1

if __name__ == "__main__":
    times = 0
    if len(sys.argv) > 1:
        times = int(sys.argv[1])
    if times is not None and times > 0:
        alertar(times)
    else:
        alertar(5)
