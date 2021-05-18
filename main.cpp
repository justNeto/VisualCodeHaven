#include <iostream>
#include "Fraction.h"
#include "MatFrac.h"
#include "MatFracFromDoc.h"


int main() {
    Fraction F1 = Fraction(1, 2);
    Fraction F2 = Fraction(3, 2);
    Fraction F3 = Fraction::sumFract(F1, F2);
    F3.printFract();
    Fraction F4;
    F4 = Fraction::sumFract(F2, F3);
    F4.printFract();

    MatFracFromDoc M1 = MatFracFromDoc("Matriz1.txt");
    MatFracFromDoc M2 = MatFracFromDoc("Matriz2.txt");
    MatFrac::sumMatrix(M1, M2, "QuePex.txt");
}