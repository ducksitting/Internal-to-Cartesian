import re
from vectors import *
from functions import readZmat, getdist, createCSVstring
import sys

# Inputs
a = 0.5
b = 4.0
inc = 0.01
type = 0# 0 = bonds; 1 = angles; 2 = dihedrals
tidx = 0
icfile = 'inputexample.txt'
fnout = 'distances.dat'

# -------------------CODE----------------------
a1idx = [];idx = [];bl = [];ba = [];bdi = []
readZmat(bl, ba, bdi, idx, a1idx, icfile)

# Variables
N = int((b-a)/inc)

fout = open(fnout, "w")
for i in range(0, N):
    it = i * inc + a

    if type == 0:
        bl[tidx] = it
    elif type == 1:
        ba[tidx] = it
    elif type == 2:
        bdi[tidx] = it
    else:
        print "Run failed. Enter acceptable value for 'type'"
        sys.exit(0)

    dists = getdist(bl, a1idx, ba, idx, bdi)
    output = createCSVstring(dists)
    fout.write(output)

fout.close()
