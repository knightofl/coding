#include <stdio.h>

typedef struct body
{
    float height, weight;
} body;

body avg(body, body);

int main(int argc, char *argv[])
{
 
    body father, mother, av;

    printf("아버지의 키와 몸무게? : ");
    scanf("%f %f", &father.height, &father.weight);

    printf("어머니의 키와 몸무게? : ");
    scanf("%f %f", &mother.height, &mother.weight);

    av = avg(father, mother);
    printf("학생의 키 : %d\n", (int)av.height + 5);
    printf("학생의 몸무게 : %.1f\n", av.weight - 4.5);

    return 0;
}

body avg(body father, body mother)
{
    body av;
    av.height = (father.height + mother.height) / 2;
    av.weight = (father.weight + mother.weight) /2;

    return av;
}

