#include <stdio.h>
#include <string.h>

void copy(FILE *, FILE *);

int main(int argc, char *argv[])
{
    FILE *fstream_a, *fstream_b;
    char *org = "a.txt";
    char *des = "b.txt";

    fstream_a = fopen(org, "r");
    fstream_b = fopen(des, "w");

    if (!fstream_a)
        printf("a.txt �� �о�� �� �����ϴ�.\n");
    else if (!fstream_b)
        printf("b.txt �� �� �� �����ϴ�.\n");
    else {
        copy(fstream_a, fstream_b);
        printf("���� ���翡 �����߽��ϴ�.");
    }    

    fclose(fstream_b);
    fclose(fstream_a);
    
    return 0;
}

void copy(FILE *fstream_a, FILE *fstream_b)
{
    char buf[1000];

    fread(buf, sizeof(char), sizeof(buf), fstream_a);
    fwrite(buf, sizeof(char), strlen(buf), fstream_b);
}
