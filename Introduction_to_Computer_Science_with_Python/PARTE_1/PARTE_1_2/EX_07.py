a = int(input("Coef a: "))
b = int(input("Coef b: "))
c = int(input("Coef c: "))

delta = (b**2 - 4*a*c)

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    raiz1 = (-b + pow(delta, 1/2))/2*a
    raiz2 = (-b - pow(delta, 1/2))/2*a
    if raiz1 == raiz2:
        print(f"a raiz desta equação é {raiz1}")
    else:
        if raiz1 > raiz2:
            raiz_primeiro = raiz2
            raiz_segundo = raiz1
        print(f"as raízes da equação são {raiz_primeiro} e {raiz_segundo}")
