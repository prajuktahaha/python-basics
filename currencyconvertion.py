#wap to convert usd to inr
usd = int(input("Enter the value in USD:"))
def convert(usd):
    inr = usd*82.74
    print(inr)
    return inr
print("Value in INR is:", convert(usd))
