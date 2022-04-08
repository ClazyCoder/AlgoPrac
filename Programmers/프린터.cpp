#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    queue<pair<int,int>> printer_queue;
    priority_queue<int> pr_queue;
    int i = 0;
    for (vector<int>::iterator iter = priorities.begin();
                                iter != priorities.end();
                                ++iter
        )
    {
        printer_queue.push({ i , *iter});
        pr_queue.push(*iter);
        ++i;
    }
    while (!printer_queue.empty())
    {
        int number = printer_queue.front().first;
        int p = printer_queue.front().second;
        if (p == pr_queue.top())
        {
            ++answer;
            pr_queue.pop();
            printer_queue.pop();
            if (number == location)
                break;
        }
        else
        {
            printer_queue.pop();
            printer_queue.push({ number, p });
        }
    }
    return answer;
}