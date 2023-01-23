#include <stdio.h>

int main(int argc, char *argv[])
{
    int arr[5] = {10, 20, 30, 40, 50};
    int *ptr = &arr[2];

    printf("%d\n", *arr);
    printf("%d\n", *ptr++);
    printf("%d\n", *ptr);
    //printf("%d\n", arr++);
    printf("%d\n", ++(*arr));
    
    return 0;
}
