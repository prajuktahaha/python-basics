#wap to find sum of first n numbers (usig while loop)
n = int (input("Enter the value of the number:"))
sum = 0
i = 1
while i <=n:
    sum += i
    i += 1
print("Sum of first" , n , "numbers is:", sum)
