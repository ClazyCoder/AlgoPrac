#include<cstdio>

int main()
{
	int N;
	int V = 1;
	scanf("%d", &N);
	if (N == 1)
		printf("%d\n",N);
	else
	{
		for (int i = 1;; i++)
		{
			V += i * 6;
			if (N <= V)
			{
				printf("%d\n", i+1);
				break;
			}
		}
	}
	return 0;
}