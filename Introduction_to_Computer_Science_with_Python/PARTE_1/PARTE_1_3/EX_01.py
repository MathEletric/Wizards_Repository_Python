n = int(input("Digite o valor de n: "))
res = n
if res:
    while n > 1:
        res = res*(n-1)
        n -= 1
    print(res)
else:
    print(res+1)


