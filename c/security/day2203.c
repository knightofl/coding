#include <stdio.h>

int main(int argc, char *argv[])
{
    char cArray[4] = {'a', 'b', 'c'};
    int nArray[4] = {0, 1, 2, 3};
    int i;

    printf("&cArray = 0x%x\n", &cArray);
    printf("&nArray = 0x%x\n", &nArray);

    for (i = 0; i < 4; i++)
        printf("&cArray[%d] : 0x%x : %d\n", i, &cArray[i], cArray[i]);
    
    for (i = 0; i < 4; i++)
        printf("&nArray[%d] : 0x%x : %d\n", i, &nArray[i], nArray[i]);
    
    return 0;
}
