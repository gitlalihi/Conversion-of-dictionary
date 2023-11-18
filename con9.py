#Python – Convert dictionary to K sized dictionaries
user_dict={}
num=int(input("Enter your nunber you want for dictionaries:"))
for i in range(num):
    key=input("Enter your key:")
    value= input("Enter your value:")
    user_dict[key]=value

print("User dictionary is:",user_dict)
k=input("Enter the size you want to didvide your dictionary")
res = [dict(list(user_dict.items())[i:i+k]) for i in range(0, len(user_dict), k)]
print("Your sized dictionary is ",res)
 