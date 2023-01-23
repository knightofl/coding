#include <stdio.h>

int main(int argc, char *argv[])
{
    int arr[5] = {10, 20, 30, 40, 50};
    int *ptr = &arr[4];

    //printf("%d\n", arr--); // 배열명은 상수
    printf("%d\n", *ptr--);
    printf("%d\n", arr[4]);
    printf("%d\n", ptr--);
    printf("%d\n", *ptr);
    
    return 0;
}
