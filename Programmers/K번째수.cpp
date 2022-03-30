#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for (vector<vector<int>>::iterator iter = commands.begin();
        iter != commands.end();
        ++iter
        )
    {
        vector<int> temp_vec = vector<int>(array.begin()+(*iter)[0]-1, array.begin()+(*iter)[1]);
        sort(temp_vec.begin(), temp_vec.end());
        answer.push_back(temp_vec[(*iter)[2]-1]);
    }
    return answer;
}