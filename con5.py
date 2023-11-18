#Python – Convert key-values list to flat dictionary
num_pairs = int(input("Enter the number of key-value pairs: "))
key_value_dict = {}
for _ in range(num_pairs):
    key = input("Enter key: ")
    value = list(input("Enter value: "))
    key_value_dict[key] = value
print("Input key-value dictionary:")
print(key_value_dict)
flat_dict = dict(key_value_dict)


print("Flat Dictionary:")
print(flat_dict)
