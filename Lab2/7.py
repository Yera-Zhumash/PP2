#remove 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#it removes the first 
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#removes the choosen one '
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#If not specify pop removes last 
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del does the same'
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# also delete the whole list 
thislist = ["apple", "banana", "cherry"]
del thislist

# does the same but not deleting the list itself
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

