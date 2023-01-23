#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *stream;
    char ch[50] = "sample test";
    char cp[50] = {0};
    
    stream = fopen("test.txt", "w");
    if (stream)
        fwrite(ch, sizeof(char), strlen(ch), stream);
    else printf("can't open file1");
    fclose(stream);

    stream = fopen("test.txt", "r");
    if (stream)
        fread(cp, sizeof(char), sizeof(cp), stream);
    else printf("can't open file2");
    fclose(stream);

    stream = fopen("copy.txt", "w");
    if (stream)
        fwrite(cp, sizeof(char), strlen(cp), stream);
    else printf("can't open file3");
    fclose(stream);
    
    return 0;
}
