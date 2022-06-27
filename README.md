# Simple-CLT
This simple tool computes variables of interest in the study of the classical lamination, such as the Hooke's law in matrix form (that link stresses and strains) for orthotropic materials under plain stress conditions and the three matrices that links the three membrane forces (for unit of length) and the three bending moments (for unit of length) to the generalized strains.
## Usage
Simply run the two given scripts in a terminal window and follows the instructions. The first file, `Composite.py`, allows you compute the micromechanical elements of a single ply, that later are needed to creates the matrices of the entire laminate in `CLT.py`.<br>
```
python3 Composite.py
python3 CLT.py
```
## Example
If you'd like to compute the elements of a single ply given the following:
| Name | Value |
| --- | --- |
| Exx fiber | 50 GPa |
| Eyy fiber | 10 GPa |
| nu yx fiber | 0.25 |
| Gxy fiber | 5 GPa |
| E matrix | 5 GPa |
| nu matrix | 0.3 |
| V fiber | 0.55 |

Where V is the volumetric fraction of the fiver, you can run `Composite.py` and follow the instructions (bold text is user-written; press enter after each number):
<pre>
CLASSICAL LAMINATION THEORY - Composite elements
This tool computes the Hooke's Law matrix of a composite given the elements of the fiber and the matrix.
 - Please insert only numbers in the following rows to build the laminate.

Exx fib [GPa]: <b>50</b>
Eyy fib [GPa]: <b>10</b>
Gxy fib [GPa]: <b>5</b>
Nuyx fibra   : <b>0.25</b>
E matri [GPa]: <b>5</b>
Nu matrix    : <b>0.3</b>
V fiber      : <b>0.55</b>
</pre>

Then, the program will output the elements[^1] and the matrix Q:

| UD1 | Value |
| --- | --- |
| Exx | 30 GPa |
| Eyy | 7 GPa |
| nu yx | 0.3 |
| nu xy | 0.05 |
| Gxy | 3 GPa |

[^1] Values here have been approximated.

$$
 [Q] = \begin{bmatrix}
  E_{xx} \over {1-\nu_{xy}*\nu_{yx}} & {\nu_{yx}*E_{yy}} \over {1-\nu_{xy}*\nu_{yx}} & 0 \\
  {\nu_xy*E_{xx}} \over {1-\nu_{xy}*\nu_{yx}} & {E_{yy}} \over {1-\nu_{xy}*\nu_{yx}} & 0 \\
  0 & 0 & 1 \over G_{xy}
 \end{bmatrix}
$$

Now, if you want to consider a laminate, suppose we have the following structure:

| Sequence | Angle[°] | Type | Thickness [mm] |
| --- | --- | --- | --- |
| 1 | 0 | UD1 | 0.2 |
| 2 | 45 | UD2 | 0.6 |
| 3 | -45 | UD2 | 0.6 |
| 4 | 0 | UD2 | 0.2 |

where UD1 is the previous ply and UD2 is:

| UD2 | Value |
| --- | --- |
| Exx | 50 GPa |
| Eyy | 3 GPa |
| nu yx | 0.3 |
| nu xy | 0.05 |
| Gxy | 8 GPa |

we can use `CLT.py` and follow the instructions (bold text is user-written; press enter after each number):

<pre>
CLASSICAL LAMINATION THEORY
This tool computes the [A], [B] and [C] matrices of a give sequence of plies.
 - Please insert only numbers in the following rows to build the laminate; 
 - If you reach the last ply, please leave void the next field;
 - Write S to create a symmetric insertion;
 - The first ply is the top one.

Ply 1
Exx [GPa]: <b>30</b>
Eyy [GPa]: <b>7</b>
Gxy [GPa]: <b>3</b>
Nu yx:     <b>0.3</b>
thic [mm]: <b>0.2</b>
Angle [°]: <b>0</b>
Rotated [Q] matrix:
30643513789.5812 2145045965.2707 0.0000 
2145045965.2707 7150153217.5689 0.0000 
0.0000 0.0000 3000000000.0000 


Ply 2
Exx [GPa]: <b>50</b>
Eyy [GPa]: <b>3</b>
Gxy [GPa]: <b>8</b>
Nu yx:     <b>0.3</b>
thic [mm]: <b>0.6</b>
Angle [°]: <b>45</b>
Rotated [Q] matrix:
21774381660.9692 5774381660.9692 11813794490.2473 
5774381660.9692 21774381660.9692 11813794490.2473 
11813794490.2473 11813794490.2473 12869495274.4822 


Ply 3
Exx [GPa]: <b>50</b>
Eyy [GPa]: <b>3</b>
Gxy [GPa]: <b>8</b>
Nu yx:     <b>0.3</b>
thic [mm]: <b>0.6</b>
Angle [°]: <b>-45</b>
Rotated [Q] matrix:
21774381660.9692 5774381660.9692 -11813794490.2473 
5774381660.9692 21774381660.9692 -11813794490.2473 
-11813794490.2473 -11813794490.2473 12869495274.4822 


Ply 4
Exx [GPa]: <b>30</b>
Eyy [GPa]: <b>7</b>
Gxy [GPa]: <b>3</b>
Nu yx:     <b>0.3</b>
thic [mm]: <b>0.2</b>
Angle [°]: <b>0</b>
Rotated [Q] matrix:
30643513789.5812 2145045965.2707 0.0000 
2145045965.2707 7150153217.5689 0.0000 
0.0000 0.0000 3000000000.0000 


Ply 5
Exx [GPa]:
</pre>
This is the bottom of the laminate; press enter leaving the field void; the last two lines shall disappear and a reference of the z coordinates should appears. Press enter three times to see the three matrices, [A], [B] and [D].
