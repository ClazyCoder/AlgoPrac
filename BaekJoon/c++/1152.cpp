#include<cstdio>

char str[1000005];

int main()
{
	fgets(str,1000005,stdin);
	char* ptr = str;
	int count = 0;
	bool flag = false;
	while (*ptr != '\0')
	{
		if (*ptr != 32 && !flag)
		{
			flag = true;
			count++;
		}
		else if (*ptr == 32)
		{
			flag = false;
		}
		ptr++;
	}
	if (str[0] == 0)
		count -= 1;
	if (*(ptr - 2) == 32)
		count -= 1;
	printf("%d",count);
	return 0;
}