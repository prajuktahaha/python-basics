#calculate sum of first n natural numbers
n = int(input("Enter the value of n:"))
def sum(n):
    if (n == 0):
        return 0
    return n + sum(n-1)
print("Sum of first" , n , "natural no is:" , sum(n)) 
