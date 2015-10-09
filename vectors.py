import math
import sys
import numpy as np


class Vec3:
    def __init__(self, ix=0.0, iy=0.0, iz=0.0):
            self.x = ix
            self.y = iy
            self.z = iz

    def add(self, vi):
        vr = Vec3()
        vr.x = self.x + vi.x
        vr.y = self.y + vi.y
        vr.z = self.z + vi.z
        return vr

    def sub(self, vi):
        vr = Vec3()
        vr.x = self.x - vi.x
        vr.y = self.y - vi.y
        vr.z = self.z - vi.z
        return vr

    def len(self):
        return ((self.x)**2 + (self.y)**2 + (self.z)**2)**0.5

    def printv(self):
        print self.x,self.y,self.z

    def crossprod(self, vi):
        vr = Vec3()
        vr.x = (self.y * vi.z) - (self.z * vi.y)
        vr.y = (self.z * vi.x) - (self.x * vi.z)
        vr.z = (self.x * vi.y) - (self.y * vi.x)
        return vr

    def dotprod(self, vi):
        a = (self.x * vi.x) + (self.y * vi.y) + (self.z * vi.z)
        return a

    def unitvec(self):
        v = self.len()
        if (v == 0.0):
            print "Div by 0"
            sys.exit(1)
        else:
            return Vec3(self.x/v, self.y/v, self.z/v)

    def scale(self, s):
        vr = Vec3()
        vr.x = self.x * float(s)
        vr.y = self.y * float(s)
        vr.z = self.z * float(s)
        return vr

    def rotate(self,R,ad):     ##R = rotation axis, ad=angle(deg)
        Ru = R

        ar = math.radians(ad)

        R11 = math.cos(ar) + Ru.x**2 * (float(1.0) - math.cos(ar))
        R12 = Ru.x * Ru.y * (float(1.0) - math.cos(ar)) - Ru.z * math.sin(ar)
        R13 = Ru.x * Ru.z * (float(1.0) - math.cos(ar)) + Ru.y * math.sin(ar)

        R21 = Ru.y * Ru.x * (float(1.0) - math.cos(ar)) + Ru.z * math.sin(ar)
        R22 = math.cos(ar) + Ru.y**2 * (float(1.0) - math.cos(ar))
        R23 = Ru.y * Ru.z * (float(1.0) - math.cos(ar)) - Ru.x * math.sin(ar)

        R31 = Ru.z * Ru.x * (float(1.0) - math.cos(ar)) - Ru.y * math.sin(ar)
        R32 = Ru.z * Ru.y * (float(1.0) - math.cos(ar)) + Ru.x * math.sin(ar)
        R33 = math.cos(ar) + Ru.z**2 * (float(1.0) - math.cos(ar))

        nv = Vec3()
        nv.x = self.x * R11 + self.y * R12 + self.z * R13
        nv.y = self.x * R21 + self.y * R22 + self.z * R23
        nv.z = self.x * R31 + self.y * R32 + self.z * R33

        return nv.unitvec()
