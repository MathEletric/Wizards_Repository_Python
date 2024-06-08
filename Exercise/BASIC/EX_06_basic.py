"""
Exercício 6

Calcule as raízes de um polinômio, através dos dados de entrada que são os valores de a, b e c de P(x) = a*x^2 + b*x + c.

"""
print("Entre com os valores de a, b e c da expressão a*x^2+b*x+c.")
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

delta = b**2 - 4*a*c


if delta >= 0:
    raiz_1 = ((-1)*b + pow(delta, 1/2))/2*a
    raiz_2 = ((-1)*b - pow(delta, 1/2))/2*a
    print(f"raiz 1: {raiz_1}\nraiz 2: {raiz_2}")
else:
    print("Raizes imaginárias")














