def main():
    
    n = coef_input()
    k = coef_input()
    
    print(bin_newton(n, k))
    
def coef_input():
    coef = int(input("Digite o valor: "))
    return coef

def fatorial(k):
    fat = k
    while k > 1:
        k -= 1
        fat = fat*(k)
    return fat

def bin_newton(n, k):
    if k != n:
        res = fatorial(n)/(fatorial(k)*fatorial(n-k))
    else:
        res = 1
    return res
    
if __name__ == '__main__':
    main()
