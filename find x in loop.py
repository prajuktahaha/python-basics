#search a number x in this tuple loop
list = [1,4,9,16,25,36,49,64,81,100]
x = int(input("enter a number to search :"))
i = 0
while i < len(list):
    print(list[i])
    if(list[i] == x):
        print("Found" , x , "at" , i)
        break
    else:
        print("finding")
    i+=1
