#include<cstdio>


bool isGroup(char* string)
{
	bool f;
	bool a;
	char* ptr;
	for (int i = 0; i < 26; i++)
	{
		ptr = string;
		f = false;
		a = false;
		while (*ptr != '\0')
		{
			if (*ptr == 'a' + i)
			{
				f = true;
			}
			if (*ptr != 'a' + i && f)
				a = true;
			if (*ptr == 'a' + i && f && a)
			{
				return false;
			}
			ptr++;
		}
	}
	return true;
}

int main()
{
	int T;
	char str[101];
	scanf("%d", &T);
	int count = 0;
	for (int i = 0; i < T; i++)
	{
		scanf(" %s", str);
		if (isGroup(str))
			count++;
	}
	printf("%d\n", count);
}