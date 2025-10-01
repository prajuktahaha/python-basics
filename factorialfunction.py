#waf to find fatorial of a number
n = int(input("Enter the value of the number:"))
def factorial(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
        print(fact)
    return fact
print("Factorial of" , n , "is:" , factorial(n))
