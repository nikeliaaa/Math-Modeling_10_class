import math
from const import h
from const import k
from const import ee
n=(2/math.sqrt(math.pi))*(h/k*(200**1.5))*ee**(-300/(k*200))*300**100
print(n)