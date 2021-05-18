//
// Created by conti on 5/14/2021.
//

#ifndef EVALDIAG_MATFRAC_H
#define EVALDIAG_MATFRAC_H

#include "Fraction.h"

class MatFrac {

public:
    Fraction** matrix; // This is a pointer of an array of pointers
    int n; // Filas
    int m; // Columnas

    MatFrac();

    MatFrac(int, int);

    void getMatrix();

    void resizeMatrix(int, int);

    Fraction ** alloc(int, int);

    void addElement(int , int, Fraction);

    static void sumMatrix(MatFrac, MatFrac, std::string);

    Fraction getElement(int, int);
};


#endif //EVALDIAG_MATFRAC_H
