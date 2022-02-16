#include<cstdio>
#include<cstdlib>

int *arr;
int N, M;

int compare(const void* a, const void* b);
void Combination(int start, int C, int flag);

int main()
{
	scanf("%d %d", &N, &M);
	arr = new int[N];
	for (int i = 0; i < N; i++)
	{
		scanf(" %d", &arr[i]);
	}
	qsort(arr, N, sizeof(int), compare);
	Combination(0, M, 0);
	delete[] arr;
	return 0;
}

void Combination(int start, int C , int flag)
{
	if (C == 0)
	{
		for (int i = 0; i < N; i++)
		{
			if (flag & (1 << i))
			{
				printf("%d ", arr[i]);
			}
		}
		printf("\n");
		return;
	}
	for (int i = start; i < N; i++)
	{
		if (!(flag & (1 << i)))
		{
			flag |= (1 << i);
			Combination(i, C - 1, flag);
			flag &= ~(1 << i);
		}
	}
}

int compare(const void* a, const void* b)
{
	return (*(int*)a - *(int*)b);
}