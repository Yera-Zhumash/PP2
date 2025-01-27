#list comprehension 

#without
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#with
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#not apple
newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in fruits]

#create iterable
newlist = [x for x in range(10)]

#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]

#uppercase
newlist = [x.upper() for x in fruits]

# set all hello 
newlist = ['hello' for x in fruits]

#Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]

