---
title: Slides Template
separator: <!--s-->
verticalSeparator: <!--v-->
theme: white
revealOptions:
    transition: 'none'
---


<img src="./carpentries_logo.png"  class="plain" width="300"/>

## Software Carpentry

### Python Part 1

</br>

Lucy Whalley  
[lucydot.github.io/slides](https://lucydot.github.io/slides)
[lucydot.github.io/python_novice](https://lucydot.github.io/python_novice)

<!--s-->


### The trade-off

<img src="./costbalance.png"  class="plain" width="400"/>


<!--s-->

### Why Python?

- readable  
- free to use
- cross-platform
- well documented
- widely used


<!--s-->
### Outline


1. running python code  
2. variables   
3. data types  
4. functions, help and errors  
5. lists  
6. for loops  
7. if statements      
             


<!--s-->

### Plain text vs. Jupyter Notebook

- *Jupyter notebook approach:*
	- write code in a `jupyter notebook`
	- run code in a `jupyter notebook`
	- save with a `.ipynb` extension

- *Plain text approach:*
	- write code in a text editor
	- save with a `.py` extension
	- run code using a terminal

<!--s-->

<div align="LEFT">

### Task


Use your Jupyter notebook to...

* link to the Imperial webpage
* calculate 3624357/325
* make a bullet pointed shopping list with heading "shopping list"

[Green sticky when you're done please]

<!--s-->

### Variables

<img src="./valuevariable.png"  class="plain" width="400"/>

<!--s-->

<div align="LEFT">

### Task


What is the final value of `position` in the program below? (Try to predict the value without running the program, then check your prediction.)

```
initial = 'left'
position = initial
initial = 'right'
```

<!--s-->

<div align="LEFT">

### Task

What do you think the following code will print?

```
first = 1
second = 5*first
first=2
print('first is', first, 'and second is', second)
```

<!--s-->

### Data types


<div align="LEFT">

<small>

| Data type  | Python name   | Definition   | Example |
|----------|--------------|--------------|---------------|
|integer   |       int       |  positive or negative whole numbers            |       `-256`        |
|float  |            float  |   real number           |         `-3.16436`      |
|string  |           str   |        character string      |    `"20 pence." `          |
|list     |            list  |   a sequence of values          |     `['frog',2,8]`          |


\+ boolean, dict, tuple, complex, None, set

</small>

<!--s-->

<div align="LEFT">

### Task

Which of the following will print 2.0? Note there may be more than one correct answer.


```
first = 1.0
second = "1"
third = "1.1"
```

<small>
1. `first + float(second)`
2. `float(second) + float(third)`
3. `first + int(third)`
4. `first + int(float(third))`
5. `int(first) + int(float(third))`
6. `2.0 * second`

</small>

<!--s-->

### Outline

<small>
1. **running python code:** Jupyter Notebooks, markdown basics  
2. **variables:** variable names, variable assignment, `print()`, execution order   
3. **data types:** integer, float, string, list, `len()`, string operations/indexing/slicing, type conversion: `int()`, `str()`, `float()` 
4. **functions, help and errors:** `min()`, `max()`, `round()`, `help()`, runtime errors (exceptions), syntax errors  
5. **lists**  
6. **for loops**  
7. **if statements**  

</small>
<!--s-->

### Lists

<small>

| Data type  | Python name   | Definition   | Example |
|----------|--------------|--------------|---------------|
|integer   |       int       |  positive or negative whole numbers            |       `-256`        |
|float  |            float  |   real number           |         `-3.16436`      |
|string  |           str   |        character string      |    `"20 pence." `          |
|list     |            list  |   a sequence of values          |     `['frog',2,8]`          |


</small>

<!--s-->

### For Loops

<img src="./forloopa.png"  class="plain" width="800"/>

<!--s-->

### For Loops

<img src="./forloopb.png"  class="plain" width="800"/>


<!--s-->

<div align="LEFT">

### Task

I want to sum the integers from 1 to 10. What is wrong with this code? How can I fix it?

```
total = 0
for number in range(10):
	total = total + number
print(total)
```

<!--s-->
### Conditionals

```
mass = 4.2

if mass > 3:
	print(mass, ' is large')

if mass < 2:
	print(mass, ' is small')

if 2 <= mass <= 3:  
	print(mass, ' is just right')
```

<!--s-->


<div align="LEFT">

### Task

What is wrong with the code? Fix the code so that it works as intented.

```
grade = 95

if grade >= 70:
	print("grade is C")
elif grade >= 80:
	print("grade is B")
elif grade >= 90:
	print("grade is A")
```
<!--s-->

### Summary

<small>
1. **running python code:** Jupyter Notebooks, markdown basics  
2. **variables:** variable names, variable assignment, `print()`, execution order   
3. **data types:** integer, float, string, list, `len()`, string operations/indexing/slicing, type conversion: `int()`, `str()`, `float()` 
4. **functions, help and errors:** `min()`, `max()`, `round()`, `help()`, runtime errors (exceptions), syntax errors  
5. **lists:** sequence type, immutable vs mutable, list method append, del  
6. **for loops:** dummy variable, loop syntax, index from 0  
7. **if statements:** if, elif, else, ordering  

These slides available at: [lucydot.github.io/slides](https://lucydot.github.io/slides)  
Workshop materials are available at: [lucydot.github.io/python_novice](https://lucydot.github.io/python_novice)  
 
Back tomorrow at 10.15am for Python Part Two

</small>
<!--s-->

### Outline


1. functions
2. variable scope  
3. libraries 
4. cleaning data with pandas 
5. analysing data with numpy
6. plotting data with matplotlib 
7. running code as a Python script
8. Programming good practice     

<!--s-->

### Why Python?

<img src="./scipy.png"  class="plain" width="600"/>

<!--s-->

### Closing comments

- Comment your code
- Use version control
- Aim for reproducibility
- Keep going


====*Thank-you*====

