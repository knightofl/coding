#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *stream;
    char cp[50] = {0};
    
    stream = fopen("c:\\test.txt", "r");
    if (stream)
        fread(cp, sizeof(char), sizeof(cp), stream);
    else printf("can't open file2");
    fclose(stream);

    stream = fopen("c:\\copy.txt", "w");
    if (stream)
        fwrite(cp, sizeof(char), strlen(cp), stream);
    else printf("can't open file3");
    fclose(stream);
    
    return 0;
}
