#include<cstdio>

int d(int N)
{
	int res;
	if (N < 10)
		res = N + N;
	else if (N < 100)
		res = N + N / 10 + N % 10;
	else if (N < 1000)
		res = N + N / 100 + N % 100 / 10 + N % 100 % 10;
	else
		res = N + N / 1000 + N % 1000 / 100 + N % 1000 % 100 / 10 + N % 1000 % 100 % 10;
	return res;
}

int list[10000] = { 0, };

int main()
{
	for (int i = 1; i < 10000; i++)
	{
		list[d(i)] = 1;
	}
	for (int i = 1; i < 10000; i++)
	{
		if(!list[i])
		printf("%d\n", i);
	}
	return 0;
}