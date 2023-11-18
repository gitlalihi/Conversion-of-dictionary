#Python – Convert Matrix to dictionary
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)

for r in matrix:
    print(r)   

res = {z + 1 : matrix[z] for z in range(len(matrix))}
print("Your resultant dictionary is :",res)
  