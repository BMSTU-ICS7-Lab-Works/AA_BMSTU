#include "lab4.h"


int vinogradOPT(const vector<vector<int>>& A, const vector<vector<int>>& B,
    const int m, const int n, const int q, vector<vector<int>>& C)
{
    vector<int> mulH(m, 0);
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n - 1; j += 2)
        {
            mulH[i] -= A[i][j] * A[i][j + 1];
        }
    }

    vector<int> mulV(q, 0);
    for (int i = 0; i < q; i++)
    {
        for (int j = 0; j < n - 1; j += 2)
        {
            mulV[i] -= B[j][i] * B[j + 1][i];
        }
    }

    int last = n - 1;
    bool flag = n % 2 == 1;
    C = vector<vector<int>>(m, vector<int>(q, 0));
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < q; j++)
        {
            int tmp = mulH[i] + mulV[j];
            for (int k = 0; k < n - 1; k += 2)
            {
                tmp += (A[i][k] + B[k + 1][j]) * (A[i][k + 1] + B[k][j]);
            }
            if (flag)
            {
                tmp += A[i][last] * B[last][j];
            }
            C[i][j] = tmp;
        }
    }
    return OK;
}

void computeMulH(vector<int>& mulH, vector<vector<int>> A, int startRow, int endRow)
{
    int n = A[0].size();
    for (int i = startRow; i < endRow; i++)
    {
        for (int j = 0; j < n - 1; j += 2)
        {
            mulH[i] -= A[i][j] * A[i][j + 1];
        }
    }
}

void computeMulV(vector<int>& mulV, vector<vector<int>> B, int startCol, int endCol)
{
    int n = B.size();
    for (int i = startCol; i < endCol; i++)
    {
        for (int j = 0; j < n - 1; j += 2)
        {
            mulV[i] -= B[j][i] * B[j + 1][i];
        }
    }
}

void computeResult(vector<vector<int>>& C, vector<vector<int>> A,
    vector<vector<int>> B, vector<int> mulH,
    vector<int> mulV, int startRow, int endRow)
{
    int n = B.size();
    int q = B[0].size();
    int last = n - 1;
    bool flag = n % 2 == 1;
    for (int i = startRow; i < endRow; i++)
    {
        for (int j = 0; j < q; j++)
        {
            int tmp = mulH[i] + mulV[j];
            for (int k = 0; k < n - 1; k += 2)
            {
                tmp += (A[i][k] + B[k + 1][j]) * (A[i][k + 1] + B[k][j]);
            }
            if (flag)
            {
                tmp += A[i][last] * B[last][j];
            }
            C[i][j] = tmp;
        }
    }
}

void computeResult1(vector<vector<int>>& C, vector<vector<int>> A,
    vector<vector<int>> B, vector<int> mulH,
    vector<int> mulV, queue<int> &que)
{
    int n = B.size();
    int q = B[0].size();
    int last = n - 1;
    bool flag = n % 2 == 1;
    mutex m;
    while (true) 
    {
        m.lock();
        if (que.empty()) 
        {
            m.unlock();
            break;
        }
        int i = que.front();
        que.pop();
        m.unlock();
        for (int j = 0; j < q; j++)
        {
            int tmp = mulH[i] + mulV[j];
            for (int k = 0; k < n - 1; k += 2)
            {
                tmp += (A[i][k] + B[k + 1][j]) * (A[i][k + 1] + B[k][j]);
            }
            if (flag)
            {
                tmp += A[i][last] * B[last][j];
            }
            C[i][j] = tmp;
        }
    } 
}

int threadedVinogradOPT(const vector<vector<int>>& A, const vector<vector<int>>& B,
    const int m, const int n, const int q, vector<vector<int>>& C,
    const int& nThreads)
{
    vector<thread> threads;
    vector<int> mulH(m, 0);
    double start = 0;
    double del = m / static_cast<double>(nThreads);
    for (int i = 0; i < nThreads; i++)
    {
        threads.push_back(thread(computeMulH, ref(mulH), A, round(start),
            round(start + del)));
        start += del;
    }
    for (auto& thread : threads)
    {
        thread.join();
    }
    start = 0;
    del = q / static_cast<double>(nThreads);
    vector<int> mulV(q, 0);
    for (int i = 0; i < nThreads; i++)
    {
        threads[i] = thread(computeMulV, ref(mulV), B, round(start),
            round(start + del));
        start += del;
    }
    for (auto& thread : threads)
    {
        thread.join();
    }

    C = vector<vector<int>>(m, vector<int>(q, 0));
    start = 0;
    del = m / static_cast<double>(nThreads);
    for (int i = 0; i < nThreads; i++)
    {
        threads[i] = thread(computeResult, ref(C), A, B, 
            mulH, mulV, round(start), round(start + del));
        start += del;
    }
    for (auto& thread : threads)
    {
        thread.join();
    }
    return OK;
}

int threadedVinogradOPTs1(const vector<vector<int>>& A, const vector<vector<int>>& B,
    const int m, const int n, const int q, vector<vector<int>>& C,
    const int& nThreads)
{
    vector<thread> threads;
    vector<int> mulH(m, 0);
    double start = 0;
    double del = m / static_cast<double>(nThreads);
    for (int i = 0; i < nThreads; i++)
    {
        threads.push_back(thread(computeMulH, ref(mulH), A, round(start),
            round(start + del)));
        start += del;
    }
    for (auto& thread : threads)
    {
        thread.join();
    }
    start = 0;
    del = q / static_cast<double>(nThreads);
    vector<int> mulV(q, 0);
    for (int i = 0; i < nThreads; i++)
    {
        threads[i] = thread(computeMulV, ref(mulV), B, round(start),
            round(start + del));
        start += del;
    }
    for (auto& thread : threads)
    {
        thread.join();
    }

    C = vector<vector<int>>(m, vector<int>(q, 0));
    queue<int> que;

    for (int i = 0; i < m; i++)
        que.push(i);
    for (int i = 0; i < nThreads; i++)
    {
        threads[i] = thread(computeResult1, ref(C), A, B,
            mulH, mulV, ref(que));
    }
    for (auto& thread : threads)
    {
        thread.join();
    }
    return OK;
}

void printMatrix(const vector<vector<int>>& matrix)
{
    for (const auto& i : matrix)
    {
        for (int j : i)
        {
            cout << j << ' ';
        }
        cout << endl;
    }
}

void generateMatrix(vector<vector<int>>& matrix, const int& size)
{
    matrix = vector<vector<int>>(size, vector<int>(size));
    auto randomNumberBetween = [](int low, int high)
    {
        auto randomFunc = [distribution_ = uniform_int_distribution<int>(low, high),
            random_engine_ = mt19937{ random_device{}() }]() mutable
        {
            return distribution_(random_engine_);
        };
        return randomFunc;
    };
    for (auto& i : matrix)
    {
        generate(begin(i), end(i), randomNumberBetween(1, 100));
    }
}

void time()
{
    vector<vector<int>> A;
    vector<vector<int>> B;
    vector<vector<int>> C;
    double vinogradTime = 0;
    double threadedVinogradTime2 = 0;
    double threadedVinogradTime4 = 0;
    double threadedVinogradTime8 = 0;
    /*
    generateMatrix(A, 9);
    generateMatrix(B, 9);
    std::cout << "Matrix size: " << 9 << endl;  
    auto time1 = chrono::high_resolution_clock::now();
    for (int j = 0; j < 1000; j++)
    {
        vinogradOPT(A, B, A.size(), B.size(), B[0].size(), C);

    }
    auto time2 = chrono::high_resolution_clock::now();
    vinogradTime = chrono::duration_cast<chrono::milliseconds>(time2 - time1).count();
    std::cout << "Vinograd time: " << vinogradTime / 1000 << endl;

    for (int j = 0; j < 1000; j++)
    {
        threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 2);
    }
    auto time3 = chrono::high_resolution_clock::now();
    threadedVinogradTime2 = chrono::duration_cast<chrono::milliseconds>(time3 - time2).count();
    std::cout << "2 Threaded vinograd time: " << threadedVinogradTime2 / 1000 << endl;

    for (int j = 0; j < 1000; j++)
    {
        threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 4);
    }
    auto time4 = chrono::high_resolution_clock::now();
    threadedVinogradTime4 = chrono::duration_cast<chrono::milliseconds>(time4 - time3).count();
    std::cout << "4 Threaded vinograd time: " << threadedVinogradTime4 / 1000 << endl;

    for (int j = 0; j < 1000; j++)
    {
        threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 8);
    }
    auto time5 = chrono::high_resolution_clock::now();
    threadedVinogradTime8 = chrono::duration_cast<chrono::milliseconds>(time5 - time4).count();
    std::cout << "8 Threaded vinograd time: " << threadedVinogradTime8 / 1000 << endl;
    std::cout << endl;

    vinogradTime = 0;
    threadedVinogradTime2 = 0;
    threadedVinogradTime4 = 0;
    threadedVinogradTime8 = 0;
    generateMatrix(A, 10);
    generateMatrix(B, 10);
    std::cout << "Matrix size: " << 10 << endl;

    time1 = chrono::high_resolution_clock::now();
    for (int j = 0; j < 1000; j++)
    {
        vinogradOPT(A, B, A.size(), B.size(), B[0].size(), C);

    }
    time2 = chrono::high_resolution_clock::now();
    vinogradTime = chrono::duration_cast<chrono::milliseconds>(time2 - time1).count();
    std::cout << "Vinograd time: " << vinogradTime / 1000 << endl;

    for (int j = 0; j < 1000; j++)
    {
        threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 2);
    }
    time3 = chrono::high_resolution_clock::now();
    threadedVinogradTime2 = chrono::duration_cast<chrono::milliseconds>(time3 - time2).count();
    std::cout << "2 Threaded vinograd time: " << threadedVinogradTime2 / 1000 << endl;

    for (int j = 0; j < 1000; j++)
    {
        threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 4);
    }
    time4 = chrono::high_resolution_clock::now();
    threadedVinogradTime4 = chrono::duration_cast<chrono::milliseconds>(time4 - time3).count();
    std::cout << "4 Threaded vinograd time: " << threadedVinogradTime4 / 1000 << endl;

    for (int j = 0; j < 1000; j++)
    {
        threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 8);
    }
    time5 = chrono::high_resolution_clock::now();
    threadedVinogradTime8 = chrono::duration_cast<chrono::milliseconds>(time5 - time4).count();
    std::cout << "8 Threaded vinograd time: " << threadedVinogradTime8 / 1000 << endl;
    std::cout << endl;
    */
}


void MENU()
{
    printf("MENU:\n");
    printf("1. Vinograd OPT\n");
    printf("2. Vinograd OPT threaded string groups\n");
    printf("3. Vinograd OPT threaded string\n");
    printf("4. testing\n");
    printf("5. time\n");
    printf("0. exit\n");
}

int main()
{
    while (1)
    {
        vector<vector<int>> A;
        vector<vector<int>> B;
        vector<vector<int>> C;
        int ent = 0;
        MENU();
        printf("Enter your choice: ");
        scanf_s("%d", &ent);
        if (ent == 1)
        {
            printf("Enter matr size = ");
            int size;
            scanf_s("%d", &size);
            printf("Matrix A \n");
            generateMatrix(A, size);
            printMatrix(A);
            printf("\n");
            printf("Matrix B \n");
            generateMatrix(B, size);
            printMatrix(B);
            printf("\n");
            printf("Result matrix OPT Vinograd: \n");
            vinogradOPT(A, B, A.size(), B.size(), B[0].size(), C);
            printMatrix(C);
            printf("\n");
        }
        else if (ent == 2)
        {
            printf("Enter matr size = ");
            int size;
            scanf_s("%d", &size);
            printf("Matrix A \n");
            generateMatrix(A, size);
            printMatrix(A);
            printf("\n");
            printf("Matrix B \n");
            generateMatrix(B, size);
            printMatrix(B);
            printf("\n");
            printf("Result matrix OPT Vinograd thread 2 string groups: \n");
            threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 2);
            printMatrix(C);
            printf("\n");
        }
        else if (ent == 3)
        {
            printf("Enter matr size = ");
            int size;
            vector<vector<int>> A = { {1, 3, 6},
                             {2, 8, 2},
                             {7, 7, 7} };
            vector<vector<int>> B = { {1, 0, 0},
                                     {0, 1, 0},
                                     {0, 0, 1} };

            printf("Matrix A\n");
            printMatrix(A);
            printf("Matrix B\n");
            printMatrix(B);

            vinogradOPT(A, B, A.size(), B.size(), B[0].size(), C);
            printf("AXB result (Vinograd Opt)");
            printMatrix(C);

            threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 8);
            printf("AXB result (Vinograd Opt threaded 1)");
            printMatrix(C);

            threadedVinogradOPTs1(A, B, A.size(), B.size(), B[0].size(), C, 8);
            printf("AXB result (Vinograd Opt threaded 2)");
            printMatrix(C); ("%d", &size);
            printf("Matrix A \n");
            generateMatrix(A, size);
            printMatrix(A);
            printf("\n");
            printf("Matrix B \n");
            generateMatrix(B, size);
            printMatrix(B);
            printf("\n");
            printf("Result matrix OPT Vinograd thread 2 string: \n");
            threadedVinogradOPTs1(A, B, A.size(), B.size(), B[0].size(), C, 2);
            printMatrix(C);
            printf("\n");
            printf("Test time analyse: \n");
        }
        else if (ent == 4)
        {
            testing();
        }
        else if (ent == 5)
        {
            time();
        }
        else if (ent == 0)
        {
            printf("Finishing...");
            break;
        }
    }

    return OK;
}