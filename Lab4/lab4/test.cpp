#include "lab4.h"

bool compare_matrix(const vector<vector<int>>& A, const vector<vector<int>>& B)
{
	if (A.size() != B.size())
		return false;
	if (A[0].size() != B[0].size())
		return false;
	for (int i = 0; i < (int)A.size(); i++)
	{
		for (int j = 0; j < (int)A[0].size(); j++)
		{
			if (A[i][j] != B[i][j])
			{
				return false;
			}
		}
	}
	return true;
}

void testing()
{
	vector<vector<int>> C;
	vector<vector<int>> A = {{1, 3, 6},
							{2, 8, 2},
							{7, 7, 7}};
	vector<vector<int>> B = {{0, 0, 0},
							{0, 0, 0},
							{0, 0, 0}};
	printf("Matrix A\n");
	printMatrix(A);
	printf("Matrix B\n");
	printMatrix(B);

	vinogradOPT(A, B, A.size(), B.size(), B[0].size(), C);
	printf("AXB result (Vinograd Opt)\n");
	printMatrix(C);

	threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 8);
	printf("AXB result (Vinograd Opt threaded 1)\n");
	printMatrix(C);

	threadedVinogradOPTs1(A, B, A.size(), B.size(), B[0].size(), C, 8);
	printf("AXB result (Vinograd Opt threaded 2)\n");
	printMatrix(C);

	A = {{1, 3, 6},
		{2, 8, 2},
		{7, 7, 7}};
	B = {{1, 0, 0},
		{0, 1, 0},
		{0, 0, 1}};

	printf("Matrix A\n");
	printMatrix(A);
	printf("Matrix B\n");
	printMatrix(B);

	vinogradOPT(A, B, A.size(), B.size(), B[0].size(), C);
	printf("AXB result (Vinograd Opt)\n");
	printMatrix(C);

	threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 8);
	printf("AXB result (Vinograd Opt threaded 1)\n");
	printMatrix(C);

	threadedVinogradOPTs1(A, B, A.size(), B.size(), B[0].size(), C, 8);
	printf("AXB result (Vinograd Opt threaded 2)\n");
	printMatrix(C);

	A = { {1, -3, 6},
		{-2, 8, -2},
		{7, -7, 7} };
	B = { {4, 3, 5},
		{2, 1, -3},
		{1, -1, -1} };

	printf("Matrix A\n");
	printMatrix(A);
	printf("Matrix B\n");
	printMatrix(B);

	vinogradOPT(A, B, A.size(), B.size(), B[0].size(), C);
	printf("AXB result (Vinograd Opt)\n");
	printMatrix(C);

	threadedVinogradOPT(A, B, A.size(), B.size(), B[0].size(), C, 8);
	printf("AXB result (Vinograd Opt threaded 1)\n");
	printMatrix(C);

	threadedVinogradOPTs1(A, B, A.size(), B.size(), B[0].size(), C, 8);
	printf("AXB result (Vinograd Opt threaded 2)\n");
	printMatrix(C);
}