#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, int> cloth_map;
    for (
        vector<vector<string>>::iterator iter = clothes.begin();
        iter != clothes.end();
        ++iter
        )
    {
        auto ret = cloth_map.insert({ (*iter)[1] , 1 });
        if (!ret.second)
        {
            cloth_map[(*iter)[1]] += 1;
        }
    }
    for (
        map<string, int>::iterator iter = cloth_map.begin();
        iter != cloth_map.end();
        ++iter
        )
    {
        answer *= ((*iter).second + 1);
    }
    return answer - 1;
}