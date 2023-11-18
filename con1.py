#Python – Convert Key-Value list Dictionary to List of Lists
user_dict={}
num=int(input("Enter your nunber you want for dictionaries:"))
for i in range(num):
    key=input("Enter your key:")
    value= input("Enter your value:")
    user_dict[key]=value

print("User dictionary is:",user_dict)

res=[]
for key,value in user_dict.items():
    res.append(key+value)
print("Your resultant dictionary to lists of lists is :",res)    
