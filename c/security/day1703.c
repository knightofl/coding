#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *stream;
    stream = fopen("c:\\test.txt", "w");
    if (stream)
        fwrite("test sample", strlen("test sample"), 1, stream); 
    
     fclose(stream);
     
    return 0;
}
