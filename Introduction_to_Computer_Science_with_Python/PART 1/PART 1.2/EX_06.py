x1 = int(input("Cordenada x1: "))
y1 = int(input("Cordenada y1: "))
x2 = int(input("Cordenada x2: "))
y2 = int(input("Cordenada y2: "))

distancia = pow(pow((x2-x1), 2) + pow((y2-y1), 2), 1/2)

if distancia >= 10:
    print("longe")
else:
    print("perto")