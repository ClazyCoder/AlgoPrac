// https://programmers.co.kr/learn/courses/30/lessons/81301

#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    string number_strings[] = {
        "zero", "one", "two",
        "three", "four", "five",
        "six", "seven", "eight", "nine"
    };
    string numbers[] = {
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    };

    int answer = 0;
    for (int i = 0; i < 10; i++)
    {
        while (s.find((number_strings[i])) != string::npos)
        {
            int pos = s.find(number_strings[i]);
            s.replace(pos, number_strings[i].length(), numbers[i]);
        }
    }
    answer = stoi(s);
    return answer;
}