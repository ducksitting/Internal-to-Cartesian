from vectors import Vec3
import re

def getdist(bl, a1idx, ba, idx, bdi):
    vecs = []
    vecs.append(Vec3(0.0, 0.0, 0.0))
    vecs.append(Vec3(bl[0], 0.0, 0.0))

    V3wk = vecs[a1idx[0][1]-1].sub(vecs[a1idx[0][0]-1]).unitvec()
    if vecs[1].x > 0:
        vecs.append(V3wk.rotate(Vec3(0.0, 0.0, 1.0), -ba[0]).scale(bl[1]).add(vecs[a1idx[0][0]-1]))
    else:
        vecs.append(V3wk.rotate(Vec3(0.0, 0.0, 1.0), -ba[0]).scale(bl[1]).add(vecs[a1idx[0][0]-1]))


    def printvecs(vector):
        for i in vector:
            i.printv()

    for i in range(3,len(bl)+1):
        # print idx[i-3][2]-1
        # print idx[i-3][0]-1
        # print ba[i-2]
        R10 = vecs[idx[i-3][2]-1].sub(vecs[idx[i-3][1]-1])  ##vec[0] - vec[1]
        R12 = vecs[idx[i-3][0]-1].sub(vecs[idx[i-3][1]-1])  ##vec[2] - vec[0]
        N = R10.crossprod(R12).unitvec().scale(1.0)
        # print "N: "
        # N.printv()
        Rw = R12.scale(-1.0).unitvec().rotate(N,ba[i-2])
        # Rw.printv()
        Rw = Rw.rotate(R12.unitvec(),bdi[i-3])
        # Rw.printv()
        Rw = Rw.scale(bl[i-1]).add(vecs[idx[i-3][0]-1])
        vecs.append(Rw)

    #print "Results:"
    #printvecs(vecs)
    dists = []
    for i in range(0,len(bl)+1):
        for j in range(i+1,len(bl)+1):
            d = vecs[i].sub(vecs[j]).len()
            dists.append(d)

    return dists

def readZmat(bl, ba, bdi, idx, a1idx, filename):
    with open(filename) as f:
        for i, line in enumerate(f):
            l = re.search('[a-zA-Z]{1,2}\s+(\d+)\s+(\d+\.+\d+)', line)
            a = re.search('[a-zA-Z]{1,2}\s+(\d+)\s+\d+\.+\d+\s+(\d+)\s+(\d+\.+\d+)', line)
            d = re.search('[a-zA-Z]{1,2}\s+(\d+)\s+\d+\.+\d+\s+(\d+)\s+\d+\.+\d+\s+(\d+)\s+(\-?\d+\.+\d+)', line)
            if l:
                bl.append(float(l.group(2)))
                # print bl
            if a:
                ba.append(float(a.group(3)))
                a1idx.append([int(a.group(1)), int(a.group(2))])
                # print ba
            if d:
                bdi.append(float(d.group(4)))
                idx.append([int(d.group(1)), int(d.group(2)), int(d.group(3))])
                # print bdi

def createCSVstring(dists):
    out = ""
    for i in dists:
        out += str(i)+","
    out += "\n"

    return out



