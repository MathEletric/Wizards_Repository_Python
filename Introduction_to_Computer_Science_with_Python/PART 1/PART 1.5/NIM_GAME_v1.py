def main():
    partida()


def menu_inicial():

    print("Bem vindo ao jogo NIM! Escolha:\n")
    op_menu = 0

    while op_menu != 1 and op_menu != 2:
        op_menu = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
    
    print()
    if op_menu == 1:
        print("Voce escolheu uma partida isolada!\n")

    else:
        print("Voce escolheu um campeonato!\n")

    return op_menu

def computador_escolhe_jogada(n, m):
    
    i = 1
    while i <= m:
            if (n - i) % (m + 1) == 0:
                return i
            i += 1

    return min(n, m)
       
def usuario_escolhe_jogada(n, m):

    jogada = 0

    while jogada > m or jogada > n or jogada < 1:

        jogada = int(input("\nQuantas peças voce vai tirar? "))
        print()
        
        if jogada > m or jogada > n or jogada < 1:
            
            print("Oops! Jogada inválida! Tente de novo.")

    return jogada

def rodada():

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m+1) == 0:
        print("\nVocê começa!\n")
        computador_começa = False

    else:
        print("\nComputador começa!\n")
        computador_começa = True
    
    while n:

        if computador_começa:

            decremento = computador_escolhe_jogada(n, m)
            n -= decremento
            computador_começa = False
            print(f"O computador tirou {decremento} peças")
            print(f"Agora resta apenas {n} peças.")

            if n == 0:

                print("Fim de jogo! O computador ganhou!")

        else:

            decremento = usuario_escolhe_jogada(n, m)
            n -= decremento
            computador_começa = True
            print(f"Você tirou {decremento} peças\n")
            print(f"Agora resta apenas {n} peças.")


            if n == 0:

                print("Você ganhou!") #Nunca acontece.

def partida():

    op_menu = menu_inicial()
    
    if op_menu == 1:
        rodada()

    else:
        rodadas = 0

        while rodadas < 3:
            rodada()
     
if __name__ == "__main__":
    main()







