#search a number x inn the tuple using for loop
tuple = (1 , 4 , 9 ,16 , 25 , 36 , 49 , 64 , 81 , 100)
x = int(input("Enter the number to be searched:"))
for i in tuple:
    if(i == x):
        print("bingo ! x found")
        break
else:
    print("x not found")    
