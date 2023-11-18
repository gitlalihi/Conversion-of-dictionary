#Python – Convert List to List of dictionaries
list=[]
num=int(input("Enter your number for list:"))
for i in range(num):
    ele=input("Enter your element:")
    list.append(ele)
print("Your list is :",list)
key_list=['key','value']
n=len(list)
res=[]
for x in range(0,n):
    res.append({key_list[0]:list[x],key_list[1]:list[x+1]})
print("Resultant list of dictionary is :",res)        