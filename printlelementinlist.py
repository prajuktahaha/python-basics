#wrt a recursive function to print all elements of a list
friends = ["prajukta" , "Divye" , "kiki" , "riki"]
def printlist(friends , i=0):
    if (i == len(friends)):
        return 
    print(friends[i])
    printlist(friends , i+1)
printlist(friends)
