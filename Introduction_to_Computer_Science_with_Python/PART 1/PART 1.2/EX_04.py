x = int(input("Divisível por 3 e 5? "))
if x % 5 == 0:
    FizzBuzz = "Fizz"
if x % 3 == 0:
    FizzBuzz = FizzBuzz + "Buzz"
if "FizzBuzz" == FizzBuzz:
    print(FizzBuzz)
else:
    print(x)