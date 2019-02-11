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

### Why Python?

<img src="./scipy.png"  class="plain" width="600"/>


<!--s-->


### Outline
<small>
1. running python code  
2. variables   
3. data types  
4. functions, help and errors  
5. lists  
6. for loops  
7. if statements                     

lunch @ 1


>Aim: To learn the basics of programming, with some examples using Python

</small>


<!--s-->

### Plain text vs. Jupyter Notebook

- *Plain text approach:*
	- write code in a text editor
	- save with a `.py` extension
	- run code using a terminal

- *Jupyter notebook approach:*
	- write code in a `jupyter notebook`
	- run code in a `jupyter notebook`
	- save with a `.ipynb` extension

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


Fill the table showing the values of the variables after each statement is executed.

```
| Command  | Value of x   | Value of y   | Value of swap |
|----------|--------------|--------------|---------------|
|x = 1.0   |              |              |               |
|y = 3.0   |              |              |               |
|swap = x  |              |              |               |
|x = y     |              |              |               |
|y = swap  |              |              |               |
|----------|--------------|--------------|---------------|
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

What do you think the following code will print?

```
first = 1
second = 5*first
first=2
print('first is', first, 'and second is', second)
```


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

I want to sum the first 10 integers. What is wrong with this code? How can I fix it?

```
total = o
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

if 2 <= mass <= 3:  (check this allowed!)
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


Workshop materials are available at: [imperialcollegelondon.github.io/python-novice-mix/](https://imperialcollegelondon.github.io/python-novice-mix/)  
These slides available at: [lucydot.github.io/slides](lucydot.github.io/slides)  

Back at 2pm for Python part two

</small>
<!--s-->

### Closing comments

- Comment your code
- Use version control
- Aim for reproducibility
- Keep going


====*Thank-you*====

