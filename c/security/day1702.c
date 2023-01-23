#include <stdio.h>

int main(int argc, char *argv[])
{
    FILE *stream_a, *stream_b;
    stream_a = fopen("c:\\testa.txt", "w");
    if (stream_a)
        printf("스트림 a 생성 성공!\n");
    
    stream_b = fopen("testb.txt", "w");
    if (stream_b)
        printf("스트림 b 생성 성공!\n");

    fclose(stream_a);
    fclose(stream_b);
    
    return 0;
}
