a = float(input("a?"))
b = float(input("b?"))
c = float(input("c?"))

d = b**2-4*a*c

if d<0:
    print("no _roots")
elif d==0:
    print("one root")
else:
    print ("two roots")
