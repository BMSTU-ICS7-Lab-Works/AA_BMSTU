#include <iostream>
#include <string>
#include <iomanip>
#include <chrono>
#include <fstream>

#include "travellingsalesman.h"

struct Parameters
{
    int t;
    double alpha;
    double rho;
    double diff;
};

static vector<Parameters> comparison;

void writeComparison(const string &name)
{
    ofstream file;
    file.open(name, std::ios_base::app);
    if (!file)
    {
        cout << "Can't open file" << std::endl;
    }
    else
    {
        for (const auto &elem: comparison)
        {
            file << elem.rho << "," << elem.alpha << "," << elem.t << "," << elem.diff << '\n';
        }
        cout << "Comparison was written successfully" << std::endl;
        file.close();
    }
}

void sortComparison()
{
    bool flag;
    for (size_t i = 0; i < comparison.size(); i++)
    {
        flag = false;
        for (size_t j = 1; j < comparison.size() - i; j ++)
        {
            if (comparison[j].diff < comparison[j - 1].diff)
            {
                Parameters tmp = comparison[j];
                comparison[j] = comparison[j - 1];
                comparison[j - 1] = tmp;
                flag = true;
            }
        }
        if (!flag) return;
    }
}

void writeTime(const std::string &name, int &n, double &bruteTime, double &antTime)
{
    ofstream file;
    file.open(name, std::ios_base::app);
    if (!file)
    {
        cout << "Can't open file" << std::endl;
    }
    else
    {
        file << n << "," << bruteTime << "," << antTime << '\n';
        file.close();
        cout << "Time was written successfully" << std::endl;
    }
}

void print_res(Path_info route){
    cout << "result:\n D = " << route.length << "\n path: ";
    for (int i = 0; i < (int) route.path.size(); i++) {
        cout << route.path[i] << " ";
    }
    cout <<"\n";
}

int main()
{
    srand(time(nullptr));

    Matrix<double> matrix = {
    { 0, 3, 4, 2, 6, 6, 7, 1, 1, 3, 9},
    { 3, 0, 3, 3, 2, 1, 5, 6, 7, 8, 1},
    { 4, 3, 0, 4, 5, 4, 3, 2, 9, 2, 3} ,
    { 2, 3, 4, 0, 9, 2, 3, 7, 8, 8, 6},
    { 6, 2, 5, 9, 0, 6, 7, 2, 2, 3, 7},
    { 6, 1, 4, 2, 6, 0, 6, 3, 10, 9, 8},
    { 7, 5, 3, 3, 7, 6, 0, 6, 3, 2, 7},
    { 1, 6, 2, 7, 2, 3, 6, 0, 4, 1, 3 },
    { 1, 7, 9, 8, 2, 10, 3, 4, 0, 9,6 },
    { 3, 8, 2, 8, 3, 9, 2, 1, 9, 0, 2 },
    { 9, 1, 3, 6, 7, 8, 7, 3, 6, 2, 0}};
    /*
    Matrix<double> matrix = {
        { 0, 3, 7},
        { 3, 0, 3},
        { 7, 3, 0}};
        */
    matrix.print();
    Path_info result = bruteForce(matrix);
    printf("Bruteforce algorythm ");
    print_res(result);
    double t = 350;
    double alpha = 0.75;
    double rho = 0.25;
    printf("Ant algorythm ");
    result = ant(matrix, t, alpha, rho);
    print_res(result);
    /*
    double diff;
    double ideal = result.length;

    for (double rho = 0; rho <= 1; rho += 0.25)
    {
        for (double alpha = 0; alpha <= 1; alpha += 0.25)
        {
            for (int t = 10; t <= 310; t += 50)
            {
                diff = 0;
                printf("0\n");
                for (auto i = 0; i < 100; i++)
                {
                    result = ant(matrix, t, alpha, rho);
                    diff += result.length - ideal;
                }
                printf("1\n");
                diff /= 100.0;
                comparison.push_back({t, alpha, rho, diff});
            }
            printf("2\n");
        }
        printf("klas");
    }
    sortComparison();
    writeComparison("D://3qrs1sem//AA//Lab6//difference.txt");
*/
    Matrix<double> matrix_test;
    double t1, t2;
    for (int n = 5; n <= 15; n+= 2)
    {
        matrix_test = Matrix<double>(n);
        matrix_test.fillRandom();
        auto start = chrono::high_resolution_clock::now();
        for (auto i = 0; i < 100; i++)
            bruteForce(matrix_test);
        auto end = chrono::high_resolution_clock::now();
        t1 = chrono::duration_cast<chrono::microseconds>(end - start).count() / 1000.0;
        auto start1 = chrono::high_resolution_clock::now();
        for (auto i = 0; i < 100; i++)
            ant(matrix_test, 290, 0.75, 0.25);
        auto end1 = chrono::high_resolution_clock::now();
        t2 = chrono::duration_cast<std::chrono::microseconds>(end1 - start1).count() / 1000.0;
        printf("\nMatrix size : %d\nBruteForce time: %f\nAnt algorythm time: %f", n, t1, t2);
        //writeTime("time.txt", n, t1, t2);
    }
    return 0;
}
