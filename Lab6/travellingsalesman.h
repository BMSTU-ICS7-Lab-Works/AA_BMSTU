#ifndef TRAVELLINGSALESMAN_H
#define TRAVELLINGSALESMAN_H

#include <cmath>
#include <cfloat>
#include <algorithm>
#include "matrix.hpp"

#define START_TETA 10
#define MIN_TETA 5

using namespace std;

struct Path_info
{
    vector<int> path;
    double length;
};

Path_info ant(const Matrix<double> &distances, const int &tMax, const double &alpha, const double &p);
Path_info bruteForce(const Matrix<double> &distances);

#endif // TRAVELLINGSALESMAN_H
