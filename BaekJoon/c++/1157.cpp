#include<cstdio>

char str[1000001];

int main()
{
	scanf("%s",str);
	char* ptr = str;
	int table[26] = { 0, };
	int max = 0;
	int maxA = 0;
	int count = 0;
	while (*ptr != '\0')
	{
		if (*ptr >= 97)
		{
			table[*ptr - 97]++;
		}
		else
		{
			table[*ptr - 65]++;
		}
		ptr++;
	}
	for (int i = 0; i < 26; i++)
	{
		if (table[i] > max)
		{
			max = table[i];
			maxA = i;
		}
	}
	for (int i = 0; i < 26; i++)
	{
		if (table[i] == max)
		{
			count++;
		}
	}
	if (count == 1)
		printf("%c\n", maxA + 65);
	else
		printf("?\n");
	return 0;
}