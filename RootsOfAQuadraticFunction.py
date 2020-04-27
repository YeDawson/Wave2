import math
print("Please enter value a:")
a = int(input())
print("Please enter value b:")
b = int(input())
print("Please enter value c:")
c = int(input())

d = b**2 - (4*a*c)
if d < 0:
    print("There are no roots")
else:
    r1 = float((-b + math.sqrt(b**2 - (4*a*c)))/2*a)
    r2 = float((-b - math.sqrt(b**2 - (4*a*c)))/2*a)
    if d == 0 :
        print("There is one root: (" + str(r1) + ",0)")
    else:
        print("There are two roots: (" + str(r1) + ",0), ("+ str(r2) + ",0)")