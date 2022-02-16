#include<cstdio>

int main()
{
	char str[21];
	int T;
	int R;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d", &R);
		scanf(" %s", str);
		char* ptr = str;
		while (*ptr != '\0')
		{
			if (*ptr != '\n')
			{
				for (int j = 0; j < R; j++)
				{
					printf("%c", *ptr);
				}
			}
			ptr++;
		}
		printf("\n");
	}
	return 0;
}