#include <stdio.h>

int main(int argc, char *argv[])
{
    int arr[4] = {1, 2, 3, 4};

    int *ptr[] = {&arr[0], &arr[1], &arr[2], &arr[3]};
    
    printf("int size = %d\n", sizeof(int));
    printf("ptr = %p\n", ptr);
    
    printf("ptr[1] = %p\n", ptr[1]);
    printf("ptr[2] = %p\n", ptr[2]);

    printf("ptr[1] = %d\n", *ptr[1]);
    printf("ptr[2] = %d\n", *ptr[2]);    	


    return 0;
}
