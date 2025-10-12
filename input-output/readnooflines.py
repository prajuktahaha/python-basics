#to read the first two lines
f=open("demo.txt" , "r")
data = f.readlines()
print(data[0])
print(data[1])
f.close()
