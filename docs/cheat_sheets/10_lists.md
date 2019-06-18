## Lists

A list stores a series of items in a particular order. Lists allow you to store sets of information in one place, whether you have just a few items or millions of items.

Use square brackets to define a list, and use commas to separate individual items in the list. Use plural names for lists, to make your code easier to read.

Individual elements in a list are accessed according to their position, called the _index_. The index of the first element is 0, the index of the second element is 1, and so forth. Negative indices refer to items at the end of the list. To get a particular element, write the name of the list and then the index of the element in square brackets.

```Python
# Making a list
cities = ['London', 'Birmingham', 'Manchester', 'Glasgow']

# Get the first item of the list
first_city = cities[0]
print(first_city)

# Get the last item of the list
last_city = cities[-1]
print(last_city)

# Find the length of a list
num_cities = len(cities)
print('cities has ' + str(num_cities) + ' items')

# Changing an element
cities[3] = 'Newcastle'

# Adding an element to the end of the list
cities.append('Sheffield')

# Inserting elements at a particular position
cities.insert(3, 'Liverpool')

# Deleting an element by its position
del cities[2]

# Removing an item by its value
cities.remove('Birmingham')

# Sorting a list
cities.sort()

# Sorting a list in reverse order
cities.sort(reverse = True)

# Printing a message for each item
for city in cities:
  print('Have you visited ' + city + '?')

# The range() function starts at 0 by default, and stops one number below the number passed to it.
# Printing the numbers 0 to 1000
for number in range(1001):
  print(number)

# Printing the numbers 5 to 995
for number in range(5, 996):
  print(number)

# Printing all items in a list
for i in range(len(cities)):
  print(cities[i])
```
