//
// Created by conti on 5/14/2021.
//

#include <iostream>
#include "Fraction.h"

Fraction::Fraction() {
    num = 0;
    den = 1;
}

Fraction::Fraction(int num, int den) {
    if (num < 0 && den < 0) {
        num = num * -1;
        den = den * -1;
    }

    if (den < 0 && num > 0) {
        num = num * -1;
    }

    this -> num = num;
    this -> den = den;
}

int Fraction::comDiv(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        comDiv(b, a % b);
    }
}

void Fraction::reductFract() {
    int cdn;
    cdn = comDiv(num, den);
    num = num / cdn;
    den = den / cdn;
}

Fraction Fraction::sumFract(Fraction f1, Fraction f2) {
    Fraction ft = Fraction(f1.num*f2.den + f2.num*f1.den, f1.den*f2.den);
    ft.reductFract();
    return ft;
}

Fraction Fraction::multFract(Fraction f1, Fraction f2) {
    Fraction ft = Fraction(f1.num*f2.num, f1.den*f2.den);
    return ft;
}

void Fraction::printFract() {
    std::cout << "Numerador: " <<  num << std::endl;
    std::cout << "Denominador: " << den << std::endl;
    std::cout << std::endl;
}

 Fraction Fraction::createFraction(std::string s) {
    std::string delimiter = "/";
    size_t pos = 0;
    std::string token;

    while ((pos = s.find(delimiter)) != std::string::npos) {
        token = s.substr(0, pos);
        s.erase(0, pos + delimiter.length());
    }
    // numerador: token
    // denominador: s
    return Fraction(stoi(token), stoi(s));
}

