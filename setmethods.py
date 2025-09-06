collection = set()
collection.add(1)
collection.add(2)
collection.remove(1)
collection.add((1,2,3))
collection.clear()

#2 separate things
collection = {"prajukta" , "hi" , "hello" , "preeti"}

print(collection.pop())

#abt union and intersection

set1 = {1,2,3}
set2 = {2,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
