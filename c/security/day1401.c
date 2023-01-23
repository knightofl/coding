#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int com;
    int player;
    
    srand(time(NULL));
    
    int count = 6;
    com = rand() % 101 + 1;

    puts("=====  숫자 맞추기 게임 =====");
    printf("기회는 모두 %d번.\n", count);

    while (count) {
	do {
	    printf("1부터 100 사이의 숫자를 입력해 주세요 : ");
	    scanf("%d", &player);
	    while(getchar() != '\n'); // 버퍼 클리어
        } while (player<0 || player>100);
 
	if (com > player)
	    printf("남은 기회 %d회. 그보다 높습니다.\n", --count);
	else if (com < player)
	    printf("남은 기회 %d회. 그보다 낮습니다.\n", --count);
	else if (com == player) {
	    printf("맞았습니다.\n");
	    break;
	}
    }

    if (!count)
	printf("틀렸습니다.\n");
    
    return 0;
}

