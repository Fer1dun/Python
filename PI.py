from cmath import pi
import math 

class cal():
    def __init__(self,count):
        newpi=math.pi*(10**count)
        newpi2=int(newpi)/(10**count)
        print(newpi2)
        print("\n",math.pi)
a=int(input("enter the count"))
cal(a)
