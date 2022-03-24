import random
v1=random.randint(2,10)
v2=random.randint(2,10)
v3=int(input("Multiplicame "+str(v1)+"X"+str(v2)))

if (v1*v2==v3):
    print("Correcto!")
else:
    print("No. Es "+str(v1*v2))