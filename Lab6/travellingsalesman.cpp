#include "travellingsalesman.h"
#define MAX_NUM 999999999999

inline double tossCoin(void)
{
    return (rand() % 100) / 100.0;
}

vector<int> getUnvisited(vector<int> &visited, const size_t &count)
{
    vector<int> unvisited;
    for (int i = 0; i < count; i++)
    {
        if (find(visited.begin(), visited.end(), i) == visited.end())
        {
            unvisited.push_back(i);
        }
    }
    return unvisited;
}

int getIndex(vector<int> &vec, const int& value)
{
    auto pos = find(vec.begin(), vec.end(), value);
    if (pos != vec.end())
    {
        return distance(vec.begin(), pos);
    }
    return 0;
}

Path_info ant(const Matrix<double> &distances, const int &tMax, const double &alpha, const double &p)
{
    const size_t size = distances.size();

    const double q = distances.average() * size;
    const double betta = 1 - alpha;

    Matrix <double> attractions(distances);
    attractions.inverse();

    Matrix<double> teta(size, START_TETA);

    Matrix<double> deltaTeta(size);

    Path_info minRoute;
    minRoute.length = -1;
    std::vector<double> probabilities(size, 0.0);

    for (int t = 0; t < tMax; t++)
    {

        deltaTeta.zero();

        for (int k = 0; k < (int) size; k++)
        {
            std::vector<int> curPath = {k};
            double curLength = 0;
            int curTown = k;

            std::vector<int> unvisited = getUnvisited(curPath, size);
            while (curPath.size() != size)
            {
                fill(probabilities.begin(), probabilities.end(), 0.0);

                for (const auto &town : unvisited)
                {
                    int index = getIndex(unvisited, town);
                    if (fabs(distances[curTown][town]) > EPS)
                    {
                        double sum = 0;
                        for (auto n : unvisited)
                            sum += pow(teta[curTown][n], alpha) * pow(attractions[curTown][n], betta);
                        probabilities[index] = pow(teta[curTown][town], alpha) * pow(attractions[curTown][town], betta) / sum;
                    }
                    else
                        probabilities[index] = 0;
                }

                double coin = tossCoin();
                size_t townIndex = 0;
                double curProbability = 0;
                for (size_t j = 0; j < size; j++)
                {
                    curProbability += probabilities[j];
                    if (coin < curProbability)
                    {
                        townIndex = j;
                        break;
                    }
                }
                int chosenTown = unvisited[townIndex];
                curPath.push_back(chosenTown);
                curLength += distances[curTown][chosenTown];
                deltaTeta[curTown][chosenTown] += q / curLength;
                curTown = chosenTown;
                unvisited.erase(unvisited.begin() + townIndex);
            }

            curLength += distances[curPath[curPath.size() - 1]][curPath[0]];
            if (minRoute.length < -EPS || (curLength < minRoute.length))
            {
                minRoute.length = curLength;
                minRoute.path = curPath;
            }
        }

        teta *= (1.0 - p);
        teta += deltaTeta;
        teta.replaceZero(MIN_TETA);
    }
    return minRoute;
}

void Hamilton(const Matrix<double> &distances, Path_info &Respath, vector<int> &curr_path, vector<bool> &visited, double &curLen)
{
    if (curr_path.size() == distances.size())
    {
        double tmp = distances[curr_path.back()][curr_path[0]];
        if (curLen + tmp < Respath.length)
        {
            Respath.path = curr_path;
            Respath.length = curLen + tmp;
        }
        return;
    }
    for (int i = 0; i < (int) distances.size(); i++)
    {
        if (!visited[i])
        {
            double tmp = distances[curr_path.back()][i];
            if (curLen + tmp > Respath.length)
                continue;
            curLen += tmp;
            curr_path.push_back(i);
            visited[i] = true;
            Hamilton(distances, Respath, curr_path, visited, curLen);
            visited[i] = false;
            curr_path.pop_back();
            curLen -= tmp;
        }
    }
}

Path_info bruteForce(const Matrix<double> &distances)
{
    int size = distances.size();
    vector<bool> visited(size, false);
    vector<int> curr_path;
    Path_info Respath;
    Respath.length = MAX_NUM;
    double curLen = 0;
    for (int i = 0; i < size; i++)
    {
        visited[i] = true;
        curr_path.clear();
        curr_path.push_back(i);
        curLen = 0;
        Hamilton(distances, Respath, curr_path, visited, curLen);
    }
    return Respath;
}
