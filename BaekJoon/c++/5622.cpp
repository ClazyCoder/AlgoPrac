#include<cstdio>

int main()
{
	char str[16];
	int table[26] = { 2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9 };
	char* ptr;
	int time = 0;
	scanf("%s", str);
	ptr = str;
	while (*ptr != '\0')
	{
		time += table[*ptr - 65] + 1;
		ptr++;
	}
	printf("%d\n", time);
	return 0;
}