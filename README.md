Variables and calculations
==========================

## Python Arithmetic Operators

|Operator|Description|
|-|-|
|`+` Addition|Adds values on either side of the operator.|
|`-` Subtraction|Subtracts right hand operand from left hand operand.|
|`*` Multiplication|Multiplies values on either side of the operator|
|`/` Division|Divides left hand operand by right hand operand|
|`%` Modulus|Divides left hand operand by right hand operand and returns remainder|
|`**` Exponent|Performs exponential (power) calculation on operators|

```python
>>> 10 + 20
# 30
>>> 25 - 7
# 18
>>> 7 * 3
# 21
>>> 45 / 9
# 5
>>> 8 % 3
# 2
>>> 2 ** 3
# 8
```

### The Order of Operations

We use parentheses in a programming language to control the order of operations. An operation is anything that uses an operator. Multiplication and division have a higher order than addition and subtraction, which means that they’re performed first. In other words, if you enter an equation in Python, multiplication or divi- sion is performed before addition or subtraction.

```python
>>> 5 + 30 * 20
# 605
>>> (5 + 30) * 20
# 700
>>> ((5 + 30) * 20) / 10
# 70.0
>>> 5 + 30 * 20 / 10
# 65.0
```

### String Special Operators

|Operator|Description|
|-|-|
|`+` Concatenation|Adds values on either side of the operator|
|`*` Repetition|Creates new strings, concatenating multiple copies of the same string|
|`[]` Slice|Gives the character from the given index|
|`[ : ]` Range Slice|Gives the characters from the given range|
|`in` Membership|Returns true if a character exists in the given string|
|`not in` Membership|Returns true if a character does not exist in the given string|
|`%` Format|Performs String formatting|

```python
>>> a, b = 'Hello', 'Python'
>>> a + b
# 'HelloPython'
>>> a * 2
# 'HelloHello'
>>> a[1]
# 'e'
>>> a[1:4]
# 'ell'
>>> 'H' in a
# True
>>> 'M' not in a
# True
>>> '%s %s' % (a, b)
# 'Hello Python'
```

## Asking Questons with if ad else

In programming, we often ask yes or no questions, and decide to do something based on the answer. For example, we might ask, "Are you older than 20?" and if the answer is yes, respond with "You are too old!"

These sorts of questions are called conditions, and we combine these conditions and the responses into if statements. Conditions can be more complicated than a single question, and if statements can also be combined with multiple questions and different responses based on the answer to each question.

### If Statements

An if statement is made up of the `if` keyword, followed by a condition and a colon (`:`), as in `if age > 20:`. The lines following the colon must be in a block, and if the answer to the question is yes (or true, as we say in Python programming), the commands in the block will be run.

```python
>>> age = 13
>>> if age > 20:
...   print('You are too old!')
...
```

```python
>>> age = 25
>>> if age > 20:
...   print('You are too old')
...   print('Why are you here')
...   print("Why aren't you mowing a lawn or sorting papers")
...
# You are too old
# Why are you here
# Why aren't you mowing a lawn or sorting papers
```

In addition to using if statements to do something when a condition is met (`True`), we can also use if statements to do something when a condition is not true. For example, we might print one message to the screen if your age is 12 and another if it’s not 12 (`False`).

```python
>>> age = 12
>>> if age == 12:
...   print("A pig fell in the mud!")
... else:
...   print("Shh. It's a secret.")
...
# A pig fell in the mud!
```

We can extend an if statement even further with elif (which is short for else-if). For example, we can check if a person’s age is 10, 11, or 12 (and so on) and have our program do something different based on the answer. These statements are different from `if-then-else` statements in that there can be more than one elif in the same statement:

```python
>>> age = 12
>>> if age == 10:
...   print("What do you call an unhappy cranberry")
...   print("A blueberry!")
... elif age == 11:
...   print("What did the green grape say to the blue grape")
...   print("Breathe! Breathe!")
... elif age == 12:
...   print("What did 0 say to 8")
...   print("Hi guys!")
... elif age == 13:
...   print("Why wasn't 10 afraid of 7")
...   print("Because rather than eating 9, 7 8 pi.")
... else:
...   print("Huh?")
...
# What did 0 say to 8
# Hi guys!
```

### Programming Statement Groups

In Python, whitespace, such as a tab (inserted when you press the tab key) or a space (inserted when you press the spacebar), is meaningful. Code that is at the same position (indented the same number of spaces from the left margin) is grouped into a block, and whenever you start a new line with more spaces than the previous one, you are starting a new block that is part of the previous one, like this:

```
line of code
line of code
line of code
    line of code
    line of code
    line of code
        line of code
        line of code
        line of code
    line of code
    line of code
```

We group statements together into blocks because they are related. The statements need to be run together.

### Python Comparison Operators

|Operator|Description|
|-|-|
|`==`|If the values of two operands are equal, then the condition becomes true.
|`!=`|If values of two operands are not equal, then condition becomes true.
|`>`|If the value of left operand is greater than the value of right operand, then condition becomes true.|
|`<`|If the value of left operand is less than the value of right operand, then condition becomes true.|
|`>=`|If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.|
|`<=`|If the value of left operand is less than or equal to the value of right operand, then condition becomes true.|

```python
>>> 10 == 20
# False
>>> 10 != 20
# True
>>> 10 > 20
# False
>>> 10 < 20
# True
>>> 5 >= 5
# True
>>> 10 <= 20
# True
```

### Combining Conditions

|Operator|Description|
|-|-|
|`and` Logical AND|If both the operands are true then condition becomes true.|
|`or` Logical OR|If any of the two operands are non-zero then condition becomes true.|
|`not` Logical NOT|Used to reverse the logical state of its operand.|

```python
>>> True and False
# False
>>> False or True
# True
>>> not True
# False
```

You can combine conditions by using the keywords and and or, which produces shorter and simpler code. Here's an example of using or:

```python
>>> age = 12
>>> if age == 10 or age == 11 or age == 12 or age == 13:
...   print('What is 13 + 49 + 84 + 155 + 97. A headache!')
... else:
...   print('Huh?')
...
# What is 13 + 49 + 84 + 155 + 97. A headache!
```

To shrink this example even further, we could use the and keyword, along with the greater than or equal-to operator (`>=`) and less-than-or-equal-to operator (`<=`), as follows:

```python
>>> if age >= 10 and age <= 13:
...   print('What is 13 + 49 + 84 + 155 + 97. A headache!')
... else:
...   print('Huh?')
...
# What is 13 + 49 + 84 + 155 + 97. A headache!
```
