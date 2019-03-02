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

### Programming with Python

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

### Functions

```
def print_greeting():
	print ("Hello!")
```
<!--s-->

### Functions

```
def print_personalised_greeting(name):
	print ("Hello "+name)
```

<!--s-->


<div align="LEFT">

### Task


Fill in the blanks to create a function that takes a list of numbers as an argument and returns the first negative value in the list. What does your function do if the list has only positive numbers?

```
def first_negative(values):
	for v in ____:
		if ____:
			return ____
```
<!--s-->

### Variable Scope

```
pressure = 103.9

def adjust(t):
    temperature = t*1.43/pressure
    return temperature
    
```
<!--s-->
### Python scientific libraries

<img src="./scipy.png"  class="plain" width="600"/>

<!--s-->

<img src="./functionmethodpackage.png"  class="plain" width="400"/>
<!--s-->
<div align="LEFT">
### Task

You want to select a random character from a string. ` "base = ATCHAGHRASG" `

1. which standard library module could help you?
2. which function could you select from that module? 
3. try to write a program that uses that function

Feel free to look online (search for "Python standard library")
<!--s-->

### Outline

<small>

1. **functions**: function syntax, return statement, parameters and arguments
2. **variable scope**: local and global variables
3. **libraries**: modules, packages, libraries, import statements, aliases
4. **cleaning data with pandas**:
5. **analysing data with numpy**:
6. **plotting data with matplotlib**: 
7. **running code as a Python script**:
8. **programming good practice**:

</small>

<!--s-->

### Indexing arrays
<img src="./python-zero-index.png"  class="plain" width="1000"/>

<!--s-->

<div align="LEFT">
### Task

Crack the code

```
letters = np.array([[g,y,c,t],
					[v,o,x,e],
					[d,p,i,n]])

letters[2,1] letters[1,0] - letters[0,2] letters[2,0] letters[0,3]
```


<!--s-->

## Operations across axes

<img src="./python-operations-across-axes.png"  class="plain" width="1000"/>


<!--s-->

### Putting it all together

[bit.ly/plot_example](http://bit.ly/plot_example)


<!--s-->

### Programming good practice

**Follow standard Python style**

- focus on readability (consistency is key!)
- maximum line length of 79 characters
- whitespace:  
	 `spam(ham[1], {eggs: 2})`   
	 `spam( ham[ 1 ], { eggs: 2} )`
- clear, meaningful variable names
<!--s-->

### Programming good practice

**Use assertions to check for errors**

~~~python
def calc_bulk_density(mass,volume):
     assert volume > 0
     return mass / volume
~~~

<!--s-->

### Programming good practice

**Document your code with docstrings**

```
 def calc_bulk_density(mass,volume):
     "Return dry bulk density = powder mass / powder volume."
     assert volume > 0
     return mass / volume
```
<!--s-->

### Programming good practice

**Use version control** - attend a git SWC

<img src="./past-workshops.png"  class="plain" width="500"/>

<!--s-->

### Scientific good practice

**Aim for reproducibility** - example: [github.com/lucydot/effmass](https://github.com/lucydot/effmass)

<img src="./effmass.png"  class="plain" width="600"/>



<!--s-->

### Summary

<small>

1. **functions**: function syntax, return statement, parameters and arguments
2. **variable scope**: local and global variables
3. **libraries**: modules, packages, libraries, import statements, aliases
4. **cleaning data with pandas**: `pandas.read_csv`, DataFrames, `pandas.to_csv`
5. **analysing data with numpy**: `numpy.loadtxt`, N-dimensional arrays, attributes
6. **plotting data with matplotlib**: `%matplotlib inline`, `plot()`, `xlabel()`, `ylabel()`, `show()`, `savefig()`
7. **running code as a Python script**: `%%writefile filename.py`, `python3 filename.py`
8. **programming good practice**: Python style, `assert` statements, docstring

</small>

<!--s-->
<small>

1. **running python code:** Jupyter Notebooks, markdown basics  
2. **variables:** variable names, variable assignment, `print()`, execution order   
3. **data types:** integer, float, string, list, `len()`, string operations/indexing/slicing, type conversion: `int()`, `str()`, `float()` 
4. **functions, help and errors:** `min()`, `max()`, `round()`, `help()`, runtime errors (exceptions), syntax errors  
5. **lists:** sequence type, immutable vs mutable, list method append, del  
6. **for loops:** dummy variable, loop syntax, index from 0  
7. **if statements:** if, elif, else, ordering  	
8. **functions**: function syntax, return statement, parameters and arguments
9. **variable scope**: local and global variables
10. **libraries**: modules, packages, libraries, import statements, aliases
11. **cleaning data with pandas**: `pandas.read_csv`, DataFrames, `pandas.to_csv`
12. **analysing data with numpy**: `numpy.loadtxt`, N-dimensional arrays, attributes
13. **plotting data with matplotlib**: `%matplotlib inline`, `plot()`, `xlabel()`, `ylabel()`, `show()`, `savefig()`
14. **running code as a Python script**: `%%writefile filename.py`, `python3 filename.py`
15. **programming good practice**: Python style, `assert` statements, docstring

</small>

<!--s-->

Well done!...keep going...


====*Thank-you*====

