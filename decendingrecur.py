#print n to 1 backwrd
n = int(input("Enter the value of n:"))
def show(n):
    if (n == 0):
        return
    print(n)
show(n-1)
show(n-2)
show(n-3)
