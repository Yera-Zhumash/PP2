#loop through list 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#using the index'
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#use while to loop 
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#use for
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]