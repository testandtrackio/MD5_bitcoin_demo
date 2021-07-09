import hashlib #importing hash library

#This function takes a string that the user inputs and returns a hash value
def hasho(mystring):
    hash_object=hashlib.md5(mystring.encode())
    return hash_object.hexdigest()

#this asks the user to input a string e.g. "bitcoin"
#(this could be transaction details etc)
mystring=input("Enter your transaction details (to hash:")

#Here we are trying to find a hash value that starts with a 00

print(hasho(mystring)) #this hashes the string 'bitcoin' but doesn't return a 0
print(hasho(mystring+"!")) #here we add a ! to the string which changes the return hash value - still no 0
print(hasho(mystring+"!!")) #and so on ....
print(hasho(mystring+"!!!"))

"""
CHALLENGE

Have a look at the following code, understand how it works
and test it.

Your challenge is to "mine" a hash value using the input "bitcoin".
The first person to find a returning hash value that has two
leading 00s wins.

e.g. 00xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx (should be returned as a hash value)
If you get two 0s at the start of the hash value returned, you have
won!!!!!!!!

"""

