#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int coin;
    int guess;
    
    srand(time(NULL));
    
    do {
        coin = rand() % 2 + 1;
	
	printf("===== 동전 앞뒤 맞추기 게임 =====\n");
        printf("숫자를 입력해 주세요 (1.앞면 / 2. 뒷면) : ");
	
	scanf("%d", &guess);

	if (coin == guess)
	    printf("맞았습니다.\n\n");
	else
	    printf("틀렸습니다.\n\n");
    } while (guess == 1 || guess == 2);

    printf("1과 2 이외의 글자를 입력하셨네요. 안녕히 가세요.\n");
    
    return 0;
}
