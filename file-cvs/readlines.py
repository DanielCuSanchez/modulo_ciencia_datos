with open('grades.csv') as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
print(content)
print("----------------------------------")
print(header)
print(rows)