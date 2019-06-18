## Decision Making

An `if` statement consists of a boolean expression followed by one or more statements. If the condition is true, then do the indented statements. If the condition is not true, then skip the indented statements.

Often there is a choice of two possibilities, only one of which will be done, depending on the truth of a condition. In the `if-else` form if statement is followed by an `else`: line, followed by another indented block that is only executed when the original condition is false. In an if-else statement exactly one of two possible indented blocks is executed.

There can be any number of `elif` lines, each followed by an indented block. With this construction exactly one of the indented blocks is executed. It is the one corresponding to the first _True_ condition, or, if all conditions are _False_, it is the block after the final `else` line.

```Python
population =  9750500

# if statement
if population > 10000000:
  print('Population is greater that 10 million')

# if-else statement
if population > 10000000:
  print('Population is greater that 10 million')
else:
  print('Population is smaller or equal to 10 million')

if population > 10000000:
  print('Population is greater that 10 million')
else:
  if population > 5000000:
    print('Population is between 10 and 5 million')
  else:
    print('Population is smaller or equal to 5 million')

# if-elif
if population > 10000000:
  print('Population is greater that 10 million')
elif  population > 5000000:
  print('Population is between 10 and 5 million')
else:
  print('Population is smaller or equal to 5 million')
```
