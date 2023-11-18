#Python – Convert List of Dictionaries to List of Lists
num_dicts = int(input("Enter the number of dictionaries: "))
list_of_dicts = []

for _ in range(num_dicts):
    key = input("Enter key: ")
    value= int(input("Enter value: "))
    key1 = input("Enter second key: ")
    value1= int(input("Enter second value: "))
    data = {'key': key, 'value': value, '2 key': key1, '2 value':value1}
    list_of_dicts.append(data)
for d in list_of_dicts:
    print(d)

list_of_lists = [list(d.values()) for d in list_of_dicts]
for item in list_of_lists:
    print(item)    