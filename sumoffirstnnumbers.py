#wap to find sum of first n numbers (usig for loop)
n = int(input("Enter the value:"))
sum  = 0
for i  in range(1 , n+1):
    sum += i
print("Sum of first" , n , "numbers is:", sum)
