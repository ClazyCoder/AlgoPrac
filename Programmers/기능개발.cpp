#include <string>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> works;
    for (
        vector<int>::iterator iter = progresses.begin(), iter2 = speeds.begin();
        iter != progresses.end() && iter2 != speeds.end();
        ++iter, ++iter2
        )
    {
        double value = (double)(100 - *iter) / *iter2;
        works.push(ceil(value));
    }
    works.push(1000);
    int num = works.front();
    works.pop();
    int count = 1;
    while (!works.empty())
    {
        int num2 = works.front();
        works.pop();
        if (num >= num2)
        {
            count++;
        }
        else
        {
            answer.push_back(count);
            count = 1;
            num = num2;
        }
    }
    return answer;
}