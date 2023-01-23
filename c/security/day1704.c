#include <stdio.h>

int main(int argc, char *argv[])
{
    FILE *stream;
    char ch[50] = {0};

    int i;
    for (i = 0; i < 50; i++)
        printf("%d", ch[i]);
    

    stream = fopen("c:\\test.txt", "r");

    if (stream) {
        fread(ch, 50, 1, stream);
        printf("%s\n", ch);
    }
    
    fclose(stream);
    
    return 0;
}
