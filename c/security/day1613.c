#include <stdio.h>

typedef struct body
{
    float height, weight;
} body;

body avg(body, body);

int main(int argc, char *argv[])
{
 
    body father, mother, av;

    printf("�ƹ����� Ű�� ������? : ");
    scanf("%f %f", &father.height, &father.weight);

    printf("��Ӵ��� Ű�� ������? : ");
    scanf("%f %f", &mother.height, &mother.weight);

    av = avg(father, mother);
    printf("�л��� Ű : %d\n", (int)av.height + 5);
    printf("�л��� ������ : %.1f\n", av.weight - 4.5);

    return 0;
}

body avg(body father, body mother)
{
    body av;
    av.height = (father.height + mother.height) / 2;
    av.weight = (father.weight + mother.weight) /2;

    return av;
}

