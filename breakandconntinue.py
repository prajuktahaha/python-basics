#continuestatement
i = 0
while i <=5:
    if(i ==4):
        i+=1
        continue
    print(i)
    i+=1

#breakstatement
i = 1
while i <= 5:
    print (i)
    if(i ==3):
        break
    i+=1
    print("end of loop")
