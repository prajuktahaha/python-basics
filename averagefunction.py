#avg of 3 numbers
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
def avg(a,b,c):
    average = (a+b+c)/3
    return average
print("Average of the 3 numbers is:" , avg(a,b,c))
