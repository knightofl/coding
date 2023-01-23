#include <stdio.h>

int main(int argc, char *argv[])
{
    int score;
    int grade;

    printf("Your score : ");

    do {
    scanf("%d", &score);
    } while (score<0 || score>100);

    grade = score / 10;

    switch (grade) {
    case 10:
    case 9:
        printf("A\n");
        break;
    case 8:
        printf("B\n");
        break;
    case 7:
        printf("C\n");
        break;
    case 6:
        printf("D\n");
        break;
    default:
        printf("F\n");
        break;
    }
    
    return 0;
}
