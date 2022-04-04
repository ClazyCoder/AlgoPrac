#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> p1({1,2,3,4,5});
    vector<int> p2({2,1,2,3,2,4,2,5});
    vector<int> p3({3,3,1,1,2,2,4,4,5,5});
    vector<int>::iterator iter1 = p1.begin(), iter2 = p2.begin(), iter3 = p3.begin();
    int score1 = 0, score2 = 0, score3 = 0;
    for(vector<int>::iterator iter = answers.begin();
       iter != answers.end();
       ++iter)
    {
        if(*iter == *iter1)
            ++score1;
        if(*iter == *iter2)
            ++score2;
        if(*iter == *iter3)
            ++score3;
        ++iter1;
        ++iter2;
        ++iter3;
        if(iter1 == p1.end())
            iter1 = p1.begin();
        if(iter2 == p2.end())
            iter2 = p2.begin();
        if(iter3 == p3.end())
            iter3 = p3.begin();
    }
    int max = score1 > score2 ? (score1 > score3 ? score1 : score3) : (score2 > score3 ? score2 : score3);
    if(score1 == max)
        answer.push_back(1);
    if(score2 == max)
        answer.push_back(2);
    if(score3 == max)
        answer.push_back(3);
    return answer;
}