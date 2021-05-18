//
// Created by conti on 5/14/2021.
//
#include <iostream>
#include <fstream>
#include "MatFrac.h"

MatFrac::MatFrac() {
    matrix = alloc(0, 0);
}

MatFrac::MatFrac(int row, int col) {
    matrix = alloc(row, col);
}

void MatFrac::addElement(int row, int col, Fraction f) {
    matrix[row][col] = f;
}

void MatFrac::getMatrix() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            std::cout << "Fila: " << i+1 << " ; Columna: " << j+1 << std::endl;
            matrix[i][j].printFract();
        }
    }
}

void MatFrac::resizeMatrix(int n, int m) {
    matrix = alloc(n, m);
}

Fraction ** MatFrac::alloc(int row, int col) {
    n = row;
    m = col;

    Fraction ** auxMatrix = new Fraction*[row];
    for (int i = 0; i < row; i++) {
        auxMatrix[i] = new Fraction[col]; // in each of the positions in the array pointer a Fraction array of length col is added
    }

    return auxMatrix;
}

void MatFrac::sumMatrix(MatFrac matrix1, MatFrac matrix2, std::string fileName) {
    MatFrac resMatrix = MatFrac(matrix1.n, matrix1.m);
    if ((matrix1.n == matrix2.n) && (matrix1.m == matrix2.m)) {
        for (int i = 0; i < matrix1.n; i++) {
            for (int j = 0; j < matrix1.m; j++) {
                resMatrix.addElement(i, j, Fraction::sumFract(matrix1.getElement(i, j), matrix2.getElement(i, j)));
            }
        }

        std::ofstream file;
        file.open(fileName);
        for (int i = 0; i < matrix1.n; i++) {
            for (int j = 0; j < matrix2.m; j++) {
                file << "|" << matrix1.getElement(i, j).num << "/" << matrix1.getElement(i, j).den;
            }
            file << "|\n";
        }

        file << "\n+\n\n";

        for (int i = 0; i < matrix1.n; i++) {
            for (int j = 0; j < matrix2.m; j++) {
                file << "|" << matrix2.getElement(i, j).num << "/" << matrix2.getElement(i, j).den;
            }
            file << "|\n";
        }

        file << "\n=\n\n";

        for (int i = 0; i < matrix1.n; i++) {
            for (int j = 0; j < matrix2.m; j++) {
                file << "|" << resMatrix.getElement(i, j).num << "/" << resMatrix.getElement(i, j).den;
            }
            file << "|\n";
        }
        file.close();

    } else {
        std::cout << "Error: different matrix dimensions. No sum available." << std::endl;
    }
}

Fraction MatFrac::getElement(int row, int col) {
    return matrix[row][col];
}