// https://programmers.co.kr/learn/courses/30/lessons/12977?language=cpp

#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool isPrime(int number)
{
    for (int i = 2; i < number; ++i)
    {
        if (number % i == 0)
            return false;
    }
    return true;
}

int solution(vector<int> nums) {
    int answer = 0;
    vector<int> temp;
    for (int i = 0; i < nums.size(); ++i)
    {
        if (i < 3)
            temp.push_back(1);
        else
            temp.push_back(0);
    }
    do
    {
        int number = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (temp[i] == 1)
                number += nums[i];
        }
        if (isPrime(number))
            ++answer;
    } while (prev_permutation(temp.begin(), temp.end()));
    return answer;
}