# Lambda functions

def sum (n1, n2):
  return n1 + n2

sum_lambda = lambda n1, n2: n1 + n2


print(sum(1,2))
print(sum_lambda(1,2))


# lambda in highorderfunction

def outsideFunction(name):
  return lambda n1,n2: f'{name} su salario es {n1 + n2}'

# lambda pattern
insideFunctionDaniel = outsideFunction("Daniel")
insideFunctionPau = outsideFunction("Pau")

print(insideFunctionDaniel(1200,1400))
print(insideFunctionPau(1200,2000))