#include <stdio.h>

int main(int argc, char *argv[])
{
    int i;

    printf("���޵� ���ڿ��� �� : %d\n", argc);

    for (i = 0; i < argc; i++)
        printf("%d��° ���ڿ� : %s\n", i, argv[i]);
    
    return 0;
}
