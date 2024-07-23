#Exercise 8

c = 5
d = 10
from module import adder # Copy out an attribute 
result = adder(c, d) # No need go through the module name “module” to fetch
# its attribute “adder”
print(result)
from module import a, b, multiplier # Copy out multiple attributes
result = multiplier(a, b)
print(result)