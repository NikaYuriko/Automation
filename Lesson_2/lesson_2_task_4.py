number = int(input())
def fizz_buzz(number):
    for number in range(1, number+1):
        if ( number % 3 == 0) and (number % 5 == 0):
             print("FizzBuzz")
        elif number % 5 == 0:
             print("Buzz")
        elif number % 3 == 0:
             print("Fizz")
        else:
             print(number)
fizz_buzz(number)

    

    
   
