cars = ["Mazda 3", "Toyota Prius", "Honda Civic", "Jetta"]

# Creating list comprehension

print("List comprehension with variable")

lst_cpr = [ element for element in cars if "Jetta" not in element ]

print(lst_cpr)

print("List comprehension")

[ print(type(element)) for element in cars if "Jetta" not in element ]


# Comparison with a loop

newCars = []
for e in cars:
  if "Jetta" not in e:
    newCars.append(e)
print(newCars)