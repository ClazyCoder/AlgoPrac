#include<cstdio>

int f(int num)
{
    if (num <= 1)
        return 1;
    return num * f(num-1);
}

int main()
{
    int num;
    scanf("%d",&num);
    printf("%d\n",f(num));
    return 0;
}