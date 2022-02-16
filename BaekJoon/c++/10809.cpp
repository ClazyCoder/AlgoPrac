#include<cstdio>

int main()
{
	char str[101];
	int freq[26];
	for (int i = 0; i < 26; i++)
		freq[i] = -1;
	fgets(str, 101, stdin);
	char* ptr = str;
	int index = 0;
	while (*ptr != '\0')
	{
		if (*ptr >= 97 && *ptr <= 122)
		{
			if (freq[*ptr - 97] < 0)
				freq[*ptr - 97] = index;

		}
		ptr++;
		index++;
	}
	for (int i = 0; i < 26; i++)
		printf("%d ", freq[i]);
	return 0;
}