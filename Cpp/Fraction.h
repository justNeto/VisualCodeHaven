//
// Created by conti on 5/14/2021.
//

#ifndef EVALDIAG_FRACTION_H
#define EVALDIAG_FRACTION_H


#include <string>

class Fraction {

public:
    Fraction();

    Fraction(int, int);

    static int comDiv(int, int);

    void reductFract();

    static Fraction sumFract(Fraction, Fraction);

    static Fraction multFract(Fraction, Fraction);

    void printFract();

    static Fraction createFraction(std::string); // create fraction from string

    int num;
    int den;
};


#endif //EVALDIAG_FRACTION_H
