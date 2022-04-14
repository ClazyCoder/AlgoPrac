// https://programmers.co.kr/learn/courses/30/lessons/76501?language=cpp

#include <string>
#include <vector>

using namespace std;

int solution(vector<int> absolutes, vector<bool> signs) {
    int answer = 0;
    int i = 0;
    for (vector<int>::iterator iter = absolutes.begin();
        iter != absolutes.end();
        ++iter
        )
    {
        if (signs[i])
            answer += *iter;
        else
            answer -= *iter;
        ++i;
    }
    return answer;
}