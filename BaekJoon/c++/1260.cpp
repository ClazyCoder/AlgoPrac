#include<cstdio>
#include<queue>
#include<vector>
#include<algorithm>

void DFS(int);
void BFS(int);

std::vector<int> grp[1001];
int visited[1001];
int N, M, S;

int main()
{
	scanf("%d %d %d", &N, &M, &S);

	for (int i = 0; i < M; ++i)
	{
		int node, edge;
		scanf("%d %d", &node, &edge);
		grp[node].push_back(edge);
		grp[edge].push_back(node);
	}
	for (int i = 0; i < N+1; ++i)
	{
		std::sort(grp[i].begin(), grp[i].end());
	}

	DFS(S);
	printf("\n");
	for (int i = 0; i < 1001; ++i)
		visited[i] = 0;
	BFS(S);
	printf("\n");

	return 0;
}

void DFS(int start)
{
	visited[start] = 1;
	printf("%d ", start);
	for (int i=0; i<grp[start].size();++i)
	{
		if (visited[grp[start][i]] == 0)
		{	
			visited[start] = 1;
			DFS(grp[start][i]);
		}
	}
}
void BFS(int start)
{
	std::queue<int> Q;
	Q.push(start);
	visited[start] = 1;
	while (!Q.empty())
	{
		int v = Q.front();
		Q.pop();
		printf("%d ", v);
		for (int i=0; i<grp[v].size(); ++i)
		{
			if (visited[grp[v][i]] == 0)
			{
				visited[grp[v][i]] = 1;
				Q.push(grp[v][i]);
			}
		}
	}
}