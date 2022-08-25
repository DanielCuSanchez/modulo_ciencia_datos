# Sets

# They are unindexed
# They are unordered
# They NOT allow duplicated values

exampleSet = {"blue", "yellow", "red", 'pink', "pink"}
exampleSet2 = set({"blue", "yellow", "red", 'pink', "purple"})

print(type(exampleSet))
print(exampleSet)
print(exampleSet2)

for element in exampleSet:
  print(element)

exampleSet.add('orange')
exampleSet.add('DARK')
exampleSet.add('Orange')
print(exampleSet)