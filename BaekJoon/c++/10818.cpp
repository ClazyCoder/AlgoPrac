#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    int min = 1000001;
    int max = -1000001;
    int x;
    int arr[1000001];
    scanf("%d",&x);
    for(int i=0;i<x;i++)
    {
        scanf("%d",&arr[i]);
        if(min > arr[i])
            min = arr[i];
        if (max < arr[i])
            max = arr[i];
    }
    printf("%d %d",min , max);
    return 0;
}