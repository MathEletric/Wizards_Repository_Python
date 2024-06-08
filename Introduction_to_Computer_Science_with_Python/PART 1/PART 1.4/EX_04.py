def fizzbuzz(num):
    if num % 3 == 0 and num % 5 != 0:
        #print("Fizz")
        return "Fizz"
    if num % 3 != 0 and num % 5 == 0:
        #print("Buzz")
        return "Buzz"
    if num % 3 == 0 and num % 5 == 0:
        #print("FizzBuzz")
        return "FizzBuzz"
    if num % 3 != 0 and num % 5 != 0:
        #print(num)
        return num
