## Conditional Tests

A conditional test is an expression that can be evaluated as _True_ or _False_. Python uses the values True and False to decide whether the code in an if statement should be executed.

You can check multiple conditions at the same time. The *and* operator returns _True_ if all the conditions listed are _True_. The *or* operator returns _True_ if any condition is _True_.

```Python
city_lnd = 'London'

# A single equal sign assigns a value to a variable. A double equal sign `==` checks whether two values are equal.
print(city_lnd == 'London')
print(city_lnd == 'Birmingham')

# Checking for inequality
print(city_lnd != 'Newcastle')

# Testing numerical values is similar to testing string values.
# Testing equality and inequality
population = 9750500
print(population == 9750500)
print(population is 9750500)
print(population != 2453700)
print(population is not 2453700)

# Comparison operators
# Strictly less than
print(population < 10000000)
# Less than or equal
print(population <= 9750500)
# Strictly greater than
print(population > 9750500)
# Greater than or equal
print(population >= 8000000)

# Checking multiple conditions
print(population > 90000000 and population < 10000000)
print(population > 20000000 or population < 1000000)
```
