def main():
    n = int(input("Digite um valor: "))
    print(soma_hipotenusa_v2(n))


def soma_hipotenusa_v1(n):  # Não está funcionando.

    state_sum = True
    sum = 0

    while n:
        i = 1 
        j = 1
        hipotenusa = n

        while hipotenusa > i**2 + j**2:

            if state_sum:
                state_sum = False
                i += 1
                if hipotenusa == i**2 + j**2:
                    sum += hipotenusa
                    break

            else:
                state_sum = True
                j += 1
                if hipotenusa == i**2 + j**2:
                    sum += hipotenusa
                    break
        n -= 1
    
    return sum

    

    sum = 0

    while n > 0:
        i = 1
        found = False
        while i < n and not found:
            j = 1
            while j < n:
                if i**2 + j**2 == n**2:
                    sum += n
                    found = True 
                    break
                j += 1
            i += 1
        n -= 1
    
    return sum

def soma_hipotenusa_v2(n):

    sum = 0

    while n:

        i = 0
        found = False

        while i < n and not found:
            i +=1
            j = 1
            while j < n:

                if i**2 + j**2 == n**2:
                    sum += n
                    found = True
                    break

                j += 1
        n -= 1
    return sum


if __name__ == "__main__":
    main()