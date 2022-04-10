#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> scoville_heap;
    for (
        vector<int>::iterator iter = scoville.begin();
        iter != scoville.end();
        ++iter
        )
    {
        scoville_heap.push(*iter);
    }
    while (scoville_heap.top() < K )
    {
        int value = scoville_heap.top();
        scoville_heap.pop();
        int value2 = scoville_heap.top();
        scoville_heap.pop();
        int mixture = value + value2 * 2;
        ++answer;
        scoville_heap.push(mixture);
        if (scoville_heap.top() >= K)
        {
            break;
        }

        if (scoville_heap.size() == 1 && scoville_heap.top() < K)
        {
            answer = -1;
            break;
        }
    }
    return answer;
}