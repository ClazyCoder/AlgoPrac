#include<cstdio>

int main()
{
	int num;
	int count = 0;
	scanf("%d", &num);
	for (int i = 1; i <= num; i++)
	{
		if (i < 100)
			count++;
		else
		{
			int a = i / 100;
			int b = (i % 100) / 10;
			int c = (i % 100) % 10;
			if (b - a == c - b)
				count++;
		}
	}
	printf("%d\n", count);
	return 0;
}