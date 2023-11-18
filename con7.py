#Python – Convert Nested dictionary to Mapped Tuple
nested_dict = {}
for x in range(2):  
    key = input("Enter a key for the dictionary: ")
    value = input("Enter the value type (dict, int, float, str): ")
    if value == 'dict':
        nested_dict[key] = {}
        for y in range(2):  
            inner_key = input("Enter a key for the inner dictionary: ")
            inner_value = input("Enter the value type (int, float, str) for the inner dictionary: ")

            if inner_value == 'int':
                nested_dict[key][inner_key] = int(input(f"Enter the integer value for '{inner_key}': "))
            elif inner_value == 'float':
                nested_dict[key][inner_key] = float(input(f"Enter the float value for '{inner_key}': "))
            elif inner_value == 'str':
                nested_dict[key][inner_key] = input(f"Enter the string value for '{inner_key}': ")
            else:
                print("Invalid value type. Please enter 'int', 'float', or 'str'.")
    else:
        nested_dict[key] = input(f"Enter the value for '{key}': ")

print("Resulting nested dictionary:", nested_dict)
res = [(key, tuple(j[key] for j in nested_dict.values())) 
                               for key in nested_dict[0]]
 
 
print("The grouped dictionary : " + str(res)) 