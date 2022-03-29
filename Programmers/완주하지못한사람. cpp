#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    map<string, int> hashTable;
    for (
        vector<string>::iterator iter = participant.begin();
         iter != participant.end(); ++iter
    )
    {
        auto ret = hashTable.insert({ *iter, 1 });
        if (ret.second)
            ret.first->second = 1;
        else
            ret.first->second += 1;
    }
    for (
        vector<string>::iterator iter = completion.begin();
         iter != completion.end(); ++iter
    )
    {
        hashTable[*iter] -= 1;
        if(hashTable[*iter] == 0)
            hashTable.erase(*iter);
    }
    answer = hashTable.begin()->first;
    return answer;
}