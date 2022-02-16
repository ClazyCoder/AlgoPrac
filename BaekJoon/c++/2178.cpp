#include<cstdio>
#include<vector>
#include<queue>

int BFS(int);

int N, M;
std::vector<int> grp[10000];
std::vector<int> dist(10000, -1);
int visited[10000];
int map[100][100];
int main()
{
	int r, c;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			scanf("%1d", &map[i][j]);
		}
	}
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			r = i + 1;
			c = j + 1;
			if (r < N)
			{
				if (map[r][j] && map[i][j])
				{
					grp[r * M + j].push_back(i * M + j);
					grp[i * M + j].push_back(r * M + j);
				}
			}
			if (c < M)
			{
				if (map[i][c] && map[i][j])
				{
					grp[i * M + c].push_back(i * M + j);
					grp[i * M + j].push_back(i * M + c);
				}
			}
		}
	}
	printf("%d\n", BFS(0));
	return 0;
}

int BFS(int start)
{
	std::queue<int> Q;
	Q.push(start);
	visited[start] = 1;
	dist[start] = 1;
	while (!Q.empty())
	{
		int v = Q.front();
		Q.pop();
		int before = Q.size();
		for (int i = 0; i < grp[v].size(); ++i)
		{
			if (visited[grp[v][i]] == 0)
			{
				visited[grp[v][i]] = 1;
				Q.push(grp[v][i]);
				dist[grp[v][i]] = dist[v] + 1;
			}
		}
	}
	return dist[N*M-1];
}