

def main():

    p = coef_input()

    while p > 0:

        if primo(p):

            print("É primo.\n")

        else:

            print("Não é primo.\n")
        
        p = coef_input()




def coef_input():

    coef = int(input("Digite o valor: "))
    return coef


def primo(x):

    fator = 2

    while x % fator != 0 and fator <= x / 2: # Por quê  fator <= x / 2
        fator += 1

    if x % fator == 0:

        return False
    
    else:

        return True






    

if __name__ == "__main__":
    main()