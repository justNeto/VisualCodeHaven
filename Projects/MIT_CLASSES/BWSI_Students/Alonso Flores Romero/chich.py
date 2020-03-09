#Variables
dValue = 0;
switch = True;
checker = True;

#Auxiliary functions
def calc (a, b, dValue):
    root = dValue**0.5;
    result1 = (-b + root)/(2*a);
    result2 = (-b - root)/(2*a);
    
    if result1 == result2:
        print ("Solution: ", result1);
    else:
        print ("Solutions: ", result1, " and ", result2);

def isnotNumber(inputString):
    return any(char.isalpha() for char in inputString);

def contOrStop (para):
    para = para.lower();
    if para == "exit":
        mes = False;
    else:
        mes = True;
    return(mes);


#Main function/main algorithm

while switch:

    print("Second grade ecuations = a^2(x) +b(x) +c = 0")
 
    fa = input("Insert the value of a: ");

    checker = contOrStop(fa);

    if checker == False:
        print("End of program");
        switch = False;
        break;

    fb = input("Insert the value of b: ");

    checker = contOrStop(fa);

    if checker == False:
        print("End of program");
        switch = False;
        break;
    
    fc = input("Insert the value of c: ");

    checker = contOrStop(fa);

    if checker == False:
        print("End of program");
        switch = False;
        break;

    if isnotNumber(fa) or isnotNumber(fb) or isnotNumber(fc):
        print("Not a number");
        break;

    else:
        a = int(fa);
        b = int(fb);
        c = int(fc);
    
        if (b**2 - 4*a*c) < 0:
            print("Solution not in real numbers");
            continue;
        else:
            dValue = (b**2 -4*a*c);
    calc(a, b, dValue);
