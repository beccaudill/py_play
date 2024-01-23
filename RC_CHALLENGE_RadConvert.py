#PYTHON CHALLENGE #1
#CONVERT RADIANS INTO DEGREES

import math

def radian_conversion(radval):
    degrees = radval * 180
    degrees = degrees / math.pi
    return degrees

print(radian_conversion(2))