""
while True:
    a = input("Please, enter a in ax\u00b2 \n")
    b = input("Enter b in bx \n")
    c = input("Enter c \n")
    if str(a) == "exit" or str(b) == "exit"  or str(c) == "exit":
        print("You just exited the code")
        break
    a = float(a)
    b = float(b)
    c = float(c)

    discriminant = ( (b**2) - 4*a*c )**( 1/2 )
    root1 = (-b + discriminant ) / (2*a)
    root2 = (-b - discriminant ) / (2*a)

    print("The roots from the equation ", a, "x\u00b2 + ", b, "x + ", c, "are:")
    print("x\u2081 = ", root1)
    print("x\u2082 = ", root2)
