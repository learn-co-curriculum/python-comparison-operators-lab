
# Comparison Operators Lab

## Introduction
We've learned about comparison operators, what they do and how to use them. We've also looked at logical and identity operators to compare elements. So, in this lab, let's practice our new skills by using these operators to get the result we would like out of each comparison.

## Objectives
* Practice using comparison operators 
* Practice using logical and identity operators 

## Instructions

Use the correct comparison operator to get the desired output, which you will find in a comment. Replace the `[COMPARISON]`, with the correct operator. See the example below.

```python
boolean_compare = False [COMPARISON] True # True
# becomes
boolean_compare = False != True # True
```

> **Remember** the comparison operators are: `==`, `!=`, `<`, `>`, `<=`, `>=`


```python
boolean_compare = True [COMPARISON] True # False
boolean_compare2 = False [COMPARISON] True # False
```


```python
number_compare = 10 [COMPARISON] 10 # True
number_compare2 = -20 [COMPARISON] 30 # True
number_compare3 = 4 [COMPARISON] 5 # False
```


```python
string_compare = "stacy" [COMPARISON] "STACY" # True
string_compare2 = "hey i love python!" [COMPARISON] "hi love python" # False
string_compare3 = "this string is bigger than the other" [COMPARISON] "that is true" # True
```


```python
# In this section, do not use either == or != operators
list_compare = [0,0,0,0] [COMPARISON] [0,0,0] # True
list_compare2 = [1,0,0] [COMPARISON] [0,0,0] # True
list_compare3 = [0,0,0] [COMPARISON] [0,0,3] # False
list_compare4 = [0,0,3,0] [COMPARISON] [0,0,3] # True
list_compare5 = [0,0,4,0] [COMPARISON] [0,0,3] # False
```

### Practicing Identity and Logical Operators

In this next section, use the identity and logical operators to get the desired output as you did in the examples above using the comparison operators.

> **Remember:**
the **logcial operators** are: `and`, `or`, & `not` and
the **identity operators** are: `is` & `is not`


```python
# Use logical opertors for this section
logical_compare = 2 [COMPARISON] [] # []
logical_compare2 = [COMPARISON] [] # True
logical_compare3 = 0 [COMPARISON] [] # 0
logical_compare4 = True [COMPARISON] 2 # 2
logical_compare5 = 2 [COMPARISON] 3 # 2
logical_compare6 = [COMPARISON] True # False
logical_compare7 = False [COMPARISON] 2 # False
```


```python
# Use identity operators for this section
a = []
b = a
identity_compare = {} [COMPARISON] {}) # False
identity_compare2 = a [COMPARISON] b) # True
identity_compare3 = b [COMPARISON] []) # True
identity_compare4 = 9 [COMPARISON] 10) # True
identity_compare5 = "Same" [COMPARISON] "Same") # False
identity_compare6 = [1,3,4] [COMPARISON] [1,2,3]) # False
```

# Summary
Great work! After all that, there's nothing we can't compare, well I guess apples and oranges might still off the table. We practiced using comparison, logical, and identity operators in Python to compare elements of the same and different datatypes and or values. Going forward, there will be plenty of instances where we will need to compare elements. So, it is important to have a good understanding of how each of these operators works. Don't worry, as with all concepts in programming, the more we work with something the better we understand it. 
