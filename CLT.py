##### CLASSICAL LAMINATION THEORY #####

# Modules neeeded
from math import floor, pi, cos, sin, pow

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

def p2(x):
    """Compute the square of the given number"""
    return pow(x, 2)

def p3(x):
    """Compute the cube of the given number"""
    return pow(x, 3)

def matscal(mat, scal):
    """Return the product of a list, matrix, and a scalar, scal"""
    mat2 = []
    for i in range(len(mat)):
        mat2.append(mat[i]*scal)
    return mat2

def matsum(mat1, mat2):
    """Return the sum of two given lists, element by element"""
    mat3 = []
    for i in range(len(mat1)):
        mat3.append(mat1[i] + mat2[i])
    return mat3

##### MAIN PROGRAM
print("""
CLASSICAL LAMINATION THEORY
This tool computes the [A], [B] and [C] matrices of a give sequence of plies.
 - Please insert only numbers in the following rows to build the laminate; 
 - If you reach the last ply, please leave void the next field;
 - Write S to create a symmetric insertion;
 - The first ply is the top one.
""")

plies = []              # List of the plies
TH = 0                  # Thickness of the laminate

# This cycle defines the laminate
while True:
    print("Ply {}".format(len(plies)+1))
    Exx = input("Exx [GPa]: ")

    # Check for void or "S" 
    if not Exx:
        # Clear the last two lines
        print("\033[A\033[A")
        print("\033[A\033[A")
        break
    elif Exx == "S" or Exx == "s":
        # Clear the last two lines and add an explanation
        print("\033[A\033[A")
        print("\033[A\033[A")
        print("-- The laminate is symmetric --\n")
        TH *= 2
        plies.extend(reversed(plies))
        break

    plies.append({
        "Exx": float(Exx)*1e9,
        "Eyy": float(input("Eyy [GPa]: "))*1e9,
        "Gxy": float(input("Gxy [GPa]: "))*1e9,
        "nyx": float(input("Nu yx:     ")),
        "th":  float(input("thic [mm]: "))*1e-3,
        "a":     int(input("Angle [°]: "))*pi/180,
    })

    TH += plies[-1]["th"]

    # Computes the nu xy element and the [Q] matrix in the frame of reference of the ply
    plies[-1]["nxy"] = plies[-1]["Eyy"]/plies[-1]["Exx"]*plies[-1]["nyx"]
    plies[-1]["Q"] = [
        plies[-1]["Exx"]/(1-plies[-1]["nxy"]*plies[-1]["nyx"]), 
        plies[-1]["nyx"]*plies[-1]["Eyy"]/(1-plies[-1]["nyx"]*plies[-1]["nxy"]), 
        0, 
        plies[-1]["nxy"]*plies[-1]["Exx"]/(1-plies[-1]["nyx"]*plies[-1]["nxy"]), 
        plies[-1]["Eyy"]/(1-plies[-1]["nxy"]*plies[-1]["nyx"]), 
        0, 
        0, 
        0, 
        plies[-1]["Gxy"]
    ]

    # Auxiliary variables to simplify the next expression
    a = plies[-1]["a"]
    Q = plies[-1]["Q"]

    # Compute the [Q] matrix in the frame of reference of the laminate
    plies[-1]["Qr"] = [
        p2(cos(a))*(Q[0]*p2(cos(a)) + Q[1]*p2(sin(a))) + p2(sin(a))*(Q[1]*p2(cos(a)) + Q[4]*p2(sin(a))) + 4*Q[-1]*p2(sin(a))*p2(cos(a)),
        p2(sin(a))*(Q[0]*p2(cos(a)) + Q[1]*p2(sin(a))) + p2(cos(a))*(Q[1]*p2(cos(a)) + Q[4]*p2(sin(a))) - 4*Q[-1]*p2(sin(a))*p2(cos(a)),
        sin(a)*cos(a)*(Q[0]*p2(cos(a)) + Q[1]*p2(sin(a))) - sin(a)*cos(a)*(Q[1]*p2(cos(a)) + Q[4]*p2(sin(a))) -2*Q[-1]*sin(a)*cos(a)*(p2(cos(a))-p2(sin(a))),

        p2(cos(a))*(Q[1]*p2(cos(a)) + Q[0]*p2(sin(a))) + p2(sin(a))*(Q[4]*p2(cos(a)) + Q[1]*p2(sin(a))) - 2*Q[-1]*sin(a)*sin(2*a)*cos(a),
        p2(sin(a))*(Q[1]*p2(cos(a)) + Q[0]*p2(sin(a))) + p2(cos(a))*(Q[4]*p2(cos(a)) + Q[1]*p2(sin(a))) + 2*Q[-1]*sin(a)*sin(2*a)*cos(a),
        sin(a)*cos(a)*(Q[1]*p2(cos(a)) + Q[0]*p2(sin(a))) - sin(a)*cos(a)*(Q[4]*p2(cos(a)) + Q[1]*p2(sin(a))) + Q[-1]*sin(2*a)*(p2(cos(a))-p2(sin(a))),

        p2(cos(a))*(Q[0]*sin(a)*cos(a) - Q[1]*sin(a)*cos(a)) + p2(sin(a))*(Q[1]*sin(a)*cos(a) - Q[4]*sin(a)*cos(a)) - 2*Q[-1]*sin(a)*cos(2*a)*cos(a),
        p2(sin(a))*(Q[0]*sin(a)*cos(a) - Q[1]*sin(a)*cos(a)) + p2(cos(a))*(Q[1]*sin(a)*cos(a) - Q[4]*sin(a)*cos(a)) + 2*Q[-1]*sin(a)*cos(2*a)*cos(a),
        sin(a)*cos(a)*(Q[0]*sin(a)*cos(a) - Q[1]*sin(a)*cos(a)) - sin(a)*cos(a)*(Q[1]*sin(a)*cos(a) - Q[4]*sin(a)*cos(a)) + Q[-1]*cos(2*a)*(p2(cos(a))-p2(sin(a)))
    ]

    print("Rotated [Q] matrix:")
    print_matrix(plies[-1]["Qr"], 3)

shift = TH/2
A = [0, 0, 0, 0, 0, 0, 0, 0, 0]
B = [0, 0, 0, 0, 0, 0, 0, 0, 0]
D = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Compute the coordinates of the plies
for i in range(len(plies)):
    if i == 0:
        plies[i]["zi-1"] = -shift
        plies[i]["zi"] = -shift + plies[i]["th"]
    else:
        plies[i]["zi-1"] = plies[i-1]["zi"]
        plies[i]["zi"] = plies[i-1]["zi"] + plies[i]["th"]
    
    print("{0}. {1:.4f}, {2:.4f}". format(i+1, plies[i]["zi-1"]*1e3, plies[i]["zi"]*1e3))

    # Computes the three matrices
    A = matsum(A, matscal(plies[i]["Qr"], plies[i]["zi"] - plies[i]["zi-1"]))
    B = matsum(B, matscal(plies[i]["Qr"], 0.5*(p2(plies[i]["zi"]) - p2(plies[i]["zi-1"]))))
    D = matsum(D, matscal(plies[i]["Qr"], 1/3*(p3(plies[i]["zi"]) - p3(plies[i]["zi-1"]))))

# Display them
input("Press Enter to visualize [A]... ")
print_matrix(A, 3)
input("Press Enter to visualize [B]... ")
print_matrix(B, 3)
input("Press Enter to visualize [D]... ")
print_matrix(D, 3)