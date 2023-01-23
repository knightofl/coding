#include <stdio.h>
#include <string.h>

int copy(char *, char *);

int main(int argc, char *argv[])
{
    
    char *org = "a.txt";
    char *des = "b.txt";

    if (copy(org, des))
        printf("파일 복제에 성공했습니다.");
    
    return 0;
}

int copy(char *org, char *des)
{
    FILE *fstream_a, *fstream_b;
    char buf[1000];
     
    fstream_a = fopen(org, "r");
    if (fstream_a)
        fread(buf, sizeof(char), sizeof(buf), fstream_a);
    else {
        printf("a.txt 를 열 수 없습니다.");
        return 0;
    }
    
    fstream_b = fopen(des, "w");
    if (fstream_b)
        fwrite(buf, sizeof(char), strlen(buf), fstream_b);
    else {
        printf("b.txt 를 쓸 수 없습니다.");
        return 0;
    }

    fclose(fstream_b);
    fclose(fstream_a);

    return 1;
}
