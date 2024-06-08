def maior_primo(num):
    if num >= 2:

        i = num
        counter = 0 
    
        while num:
            while i:
                if num % i == 0 and num != i and i != 1:
                    counter += 1
                i -= 1  

            if not counter:
                #print(num)
                break
            
            counter = 0
            num -= 1
            i = num

    return num



