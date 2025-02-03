#Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)


#To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)


#Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)


#The escape character allows you to use double quotes when you normally would not be allowed:

#txt = "We are the so-called \"Vikings\" from the north."