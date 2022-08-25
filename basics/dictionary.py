# Dictionaries
student = {
  "name" : "Daniel",
  "lastname": "Cu",
  "age": 24,
  "location": {
    "lat": 109.39,
    "long": 848.42
  },
  "colors": ["blue", "black", "white"]
}

print(type(student))
# looping dictionary
print("Looping over keys in a dictionary")

# looping dictionary

for key in student:
  if(key=="location"):
    for e in  student[key]:
      print(student[key][e])
  else:
    print(student[key])

# looping just values
for value in student.values():
  print(value)

# looping just keys
for key in student.keys():
  print(key)

# using both key and values
for key, value in student.items():
  print(key, value)

print("---------------------")
print(student.items())
print("---------------------")

# dictionary methods

# gets the key value
print(student.get("name"))

# remove the key
print(student.pop("colors"))

# gets the key name
print(student.get("colors"))

# removes the last key
print(student.popitem())

# updates the key
print(student.update({"name" : "brandon"}))

# prints dictionary
print(student)