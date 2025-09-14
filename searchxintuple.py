#search a number x inn the tuple using for loop
tuple = (1 , 4 , 9 ,16 , 25 , 36 , 49 , 64 , 81 , 100)
x = int(input("Enter the number to be searched:"))
idx = 0
for i in tuple:
    if(i == x):
        print("bingo ! x found at index", idx)
        break
    idx += 1
else:
    print("x not found")    
