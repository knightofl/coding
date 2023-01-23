#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int inpNum(void); // 1부터 100까지의 수를 입력받아 반환.
int match(int, int); // 이기면 1, 지면 0 반환.

int main(int argc, char *argv[])
{
    int com;
    int count = 6;
    char game;

    srand(time(NULL));

    do {
	com = rand() % 101 + 1;

	puts("=====  숫자 맞추기 게임 =====");
	printf("기회는 모두 %d번입니다.\n", count);

	if (match(com, count))
	    printf("맞췄습니다!! ");
	else
	    printf("맞추지 못했습니다. ");

	printf("다시 하시겠습니까? (y/n) : ");
	scanf("%c", &game);
    } while (game == 'y');
    
    return 0;
}



int match(int com, int count)
{
    int player;

    while (count) {
	player = inpNum();

	if (com == player)
	    return 1;
	else if (com > player)
	    printf("그보다 높습니다. 남은 기회는 %d회.\n", --count);
	else
	    printf("그보다 낮습니다. 남은 기회는 %d회.\n", --count);
    }

    return 0;
}


int inpNum(void)
{
    int num;
    
    do {
	printf("1부터 100 사이의 숫자를 입력해 주세요 : ");
	scanf("%d", &num);
	while(getchar() != '\n'); // 버퍼 클리어
    } while (num<1 || num>100);
	
    return num;
}
