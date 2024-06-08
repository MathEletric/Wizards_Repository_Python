"""
Exercício 8

Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto 
em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima LONGE na saída. 
Caso o contrário, quando a distância for menor que 10, imprima PERTO

"""
x1 = int(input("Digita um valor: "))
x2 = int(input("Digita um valor: "))
y1 = int(input("Digita um valor: "))
y2 = int(input("Digita um valor: "))
         
val = (x1-x2)**2 + (y1-y2)**2

if pow(val, 1/2) >= 10:
    print("LONGE.")
else:
    print("PERTO.")
print()