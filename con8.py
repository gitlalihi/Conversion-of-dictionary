#Ways to convert string to dictionary
s1=input("Enter your string:")
s2=input("Enter your second string:")
key=s1.split(", ")
value=s2.split("|")
dictionary = {}
 

for i in range(len(key)):
    dictionary[key[i]] = value[i]
 

print(" Your dictionary is",dictionary)