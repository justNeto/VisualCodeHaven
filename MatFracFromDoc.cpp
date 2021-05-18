//
// Created by conti on 5/15/2021.
//

#include "MatFracFromDoc.h"
#include <fstream>
#include <algorithm>
#include <iostream>

MatFracFromDoc::MatFracFromDoc(std::string path) {
    std::string st;
    std::string line;
    std::ifstream file;
    file.open(path);
    int aux = 0; // Number of rows
    int aux4 = 0; // Number of columns
    bool first = true;

    while (getline(file, line)) {
        int aux1 = 0; // Number of times '/' is found
        int aux2 = 0;

        line.erase(remove_if(line.begin(), line.end(), ::isspace),
                   line.end()); // Erases the current spaces found in the matriz file into lines of strings
        for (int i = 0; i < line.length(); i++) {
            if (line[i] == '|') { // finds a limit
                aux1++;
            }

            if (aux1 == 2) { // checks if two '|' have been found
                // create fraction object from string and add it to matrix
                aux1 = 1; // resets the number of found | to one; this is because at the middle of a line it should have already found one before so it only has to check for the next one.
                aux2++; // saves the number of columns
            }
        }
        aux++;
        if (first) {
            aux4 = aux2;
            first = false;
        }
    }  // First iteration finds the length of matrix.
    this-> n = aux; // Rows
    this-> m = aux4; // Columns
    Fraction ** auxMatrix = new Fraction*[n];

    file.close();
    file.open(path);
    line = "";

    for (int i = 0; i < n; i++) { //
        int aux1 = 0; // Checks how many '|' have been found
        int aux2 = 0; // Current column
        auxMatrix[i] = new Fraction[m];
        getline(file, line);
        line.erase(remove_if(line.begin(), line.end(), ::isspace), line.end()); // Erases the current spaces found in the matriz file into lines of strings

        for (int j = 0; j < line.length(); j++) {
            if (line[j] == '|') {
                aux1++;
            } else {
                st += line[j];
            }
            if (aux1 == 2) {
                auxMatrix[i][aux2] = Fraction::createFraction(st);
                st = "";
                aux1 = 1;
                aux2++;
            }
        }
    }
    matrix = auxMatrix;
}