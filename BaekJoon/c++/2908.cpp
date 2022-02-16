#include<cstdio>

int reverse(int N)
{
	int res = 0;
	while (N != 0)
	{
		res *= 10;
		res += N % 10;
		N /= 10;
	}
	return res;
}

int main()
{
	int A, B;
	int RA, RB;
	scanf("%d %d", &A, &B);
	RA = reverse(A);
	RB = reverse(B);
	printf("%d\n", RA > RB ? RA : RB);
	return 0;
}