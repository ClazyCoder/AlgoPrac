#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    map<string, string> phone_map;
    sort(phone_book.begin(),phone_book.end(),greater<>());
    for (
        vector<string>::iterator iter = phone_book.begin();
        iter != phone_book.end();
        ++iter
        )
    {
        string temp;
        for (
            string::iterator iter2 = iter->begin();
            iter2 != iter->end() - 1;
            ++iter2
            )
        {
            temp.push_back(*iter2);
            phone_map.insert(pair<string,string>(temp,*iter));
        }
    }
    for
        (
        vector<string>::iterator iter = phone_book.begin();
        iter != phone_book.end();
        ++iter
    )
    {
        auto ret = phone_map.insert(pair<string,string>(*iter,*iter));
        if(!ret.second)
        {
            answer = false;
            break;
        }
    }
    return answer;
}