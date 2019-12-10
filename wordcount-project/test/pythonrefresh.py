## Test Code Udemy Python Refresher

age = 14
name = "darius"

sentence = "Hey there, my name is {} and I am {} years old!".format(name, age)
print (sentence)


if age > 18:
	print("You are older than 18")
else:
	print ("You ain't old enough palooka!")

def hello(var1):
	print ("Good onya {} !! You are {} years ".format(name, age) + var1)

hello("young")