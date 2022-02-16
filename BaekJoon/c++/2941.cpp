#include<cstdio>
#include<string>

int main()
{
	char str[101];
	scanf("%s", str);
	int count = 0;
	int index;
	std::string s(str);
	std::string cro[8] = { "c=","c-","dz=","d-","lj","nj","s=","z=" };
	for (int i = 0; i < 8; i++)
	{
		index = -1;
		do
		{
			index = s.find(cro[i], index + 1);
			if (index != std::string::npos)
			{
				s.replace(index,cro[i].length()," ");
				count++;
			}
		} while (index != std::string::npos);
	}
	for (int i = 0; i < s.length(); i++)
	{
		if (s[i] != ' ')
			count++;
	}
	printf("%d\n", count);
	return 0;
}