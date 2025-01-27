#End of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#specified place
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Add up the lists
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#mix with tuple
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
