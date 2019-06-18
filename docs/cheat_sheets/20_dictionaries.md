## Dictionaries

Python's dictionaries allow you to connect pieces of related information. Each piece of information in a dictionary is stored as a key-value pair. When you provide a key, Python returns the value associated with that key. You can loop through all the key-value pairs, all the keys, or all the values.

Use curly braces to define a dictionary. Use colons to connect keys and values, and use commas to separate individual key-value pairs.

To access the value associated with an individual key give the name of the dictionary and then place the key in a set of square brackets. If the key you're asking for is not in the dictionary, an error will occur.

You can store as many key-value pairs as you want in a dictionary. To add a new key-value pair to an existing dictionary give the name of the dictionary and the new key in square brackets, and set it equal to the new value.

```Python
# Making a dictionary
population = {'London': 9750500, 'Birmingham': 2453700}

# Getting the value associated with a key
population_lnd = population['London']
print(population_lnd)

# Adding a key-value pair
population['Manchester'] = 1903100

# Modifying values in a dictionary
population['Birmingham'] = 2500000

# Deleting a key-value pair
del population['London']

# Looping through all key-value pairs
for city, num_people in population.items():
  print(str(num_people) + ' people live in ' + city)

# Looping through all the keys
for city in population.keys():
  print(city)

# Looping through all the values
for num_people in population.values():
    print(num_people)
```
