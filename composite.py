##### CLASSICAL LAMINATION THEORY - Composite #####

##### FUNCTIONS
# This section includes commonly used functions

def print_matrix(matrix, dim):
    """Print the given list, matrix, as a square matrix whose dimension is dim"""
    for j in range(len(matrix)):
        # Use 4 decimals
        print("{0:.4f}".format(matrix[j]), end=' ')
        # when the division (j+1)/dim has no remainder, add new line
        if (j+1) >= dim and (j+1)%dim == 0:
            print("\n", end='')
    print("\n")

##### MAIN PROGRAM
print("""
CLASSICAL LAMINATION THEORY - Composite elements
This tool computes the Hooke's Law matrix of a composite given the elements of the fiber and the matrix.
 - Please insert only numbers in the following rows to build the laminate.
""")

Exxf = float(input("Exx fib [GPa]: "))
Eyyf = float(input("Eyy fib [GPa]: "))
Gxyf = float(input("Gxy fib [GPa]: "))
nyxf = float(input("Nuyx fibra   : "))
Em   = float(input("E matri [GPa]: "))
nm   = float(input("Nu matrix    : "))
Vf   = float(input("V fiber      : "))

# Compute the missing elements
Vm = 1-Vf
Gm = Em/(2*(1+nm))

# Compute the micromechanical elements
Exx = Vf*Exxf + Vm*Em
Eyy = Eyyf*Em/(Vm*Eyyf + Vf*Em)
Gxy = Gxyf*Gm/(Vm*Gxyf + Vf*Gm)
nyx = Vf*nyxf + Vm*nm
nxy = Eyy/Exx*nyx

# Display them
print("\nExx: {0:.4f} GPa\nEyy: {1:.4f} GPa\nGxy = {2:.4f} GPa\nnxy = {3:.4f}\nnyx = {4:.4f}\n".format(Exx, Eyy, Gxy, nxy, nyx))

# Compute the matrix and display it.
Q = [Exx/(1-nxy*nyx), nyx*Eyy/(1-nyx*nxy), 0, nxy*Exx/(1-nyx*nxy), Eyy/(1-nxy*nyx), 0, 0, 0, Gxy]
print_matrix(Q, 3)