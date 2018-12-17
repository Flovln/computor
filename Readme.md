# Computor

The goal of this project was to code a program resolving simple first and second degree polynomial equations.

## Equation format

The input always has to be well formatted, there is no advanced parsing.  
All the terms must be of the either forms :
 - Degree 0: **a * X^0** or **a**  
 - Degree 1: **a * X^1** or **a * X** or **X**  
 - Degree 2: **a * X^2** or **X^2**

eg.
> monome <+/-> monome = 0  
> monome <+/-> monome = monome <+/-> monome  
> monome <+/-> monome <+/-> monome = monome <+/-> monome

## How to use the program

2 options:

Formula directly passed as program's argument
> python3.7 computor.py formula
```bash
$> python3.7 computor.py "4 * X^0 - 9.3 * X^2 + 6 * X^1 = 0"
```

Formulas are stored in a file, using the *-f* option, read that file

> python3.7 computor.py -f file

```bash
$> cat -e formulas.txt
5 * X^0 + 4 * X^1 = 4 * X^0$
27 * X^1 - 471 * X^0 = 31 * X^1 + 101 * X^0$
X + 42 - 4 * X^2 + X^1 + 2 = -3 * X^1 + X - 0.2 * X^2 - 3 * X$
$> python3.7 computor.py -f formulas.txt
```

## Output format

```bash
$> python3.7 computor.py "4 * X^0 - 9.3 * X^2 + 6 * X^1 = 0"
Formula: [4 * X^0 - 9.3 * X^2 + 6 * X^1 = 0] # formula passed as parameter
Reduced form: 4.0 * X^0 + 6.0 * X^1 - 9.3 * X^2 = 0 # reduced formula's form
Natural form: 4.0 + 6.0X - 9.3X^2 = 0 # natural formula's form
Polynomial degree: 2 # equation's polynomial degree
D = 184.8 # discriminant's value
a = -9.3
b = 6.0
c = 4.0
Discriminant is strictly positive, the two solutions are: # result with number of solutions and their values
x1 = 1.0534471169017818
x2 = -0.40828582657920126
```

```bash
$> python3.7 computor.py "5 + 4 * X + X^2= X^2"
Formula: [5 + 4 * X + X^2= X^2]
Reduced form: 5 * X^0 + 4.0 * X^1 = 0
Natural form: 5 + 4.0X = 0
Polynomial degree: 1
a = 4.0
b = 5.0
The solution is: -1.25
```

## Conclusion  

This project was a good way to dive back into polynomial equations, even though not over complicated it was a good algorithmic exercice when equations needed to be parsed then reduced so it could be computed easily by applying the desired mathematical methods.  
I chose *python*, even though I never used it before, it was a good way to learn a bit of its syntax and methods, it also made the logical implementation easier from parsing to reducing and executing.