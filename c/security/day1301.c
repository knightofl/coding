#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int com;
    char player;
    
    srand(time(NULL));
    
    do {
        com = rand() % 3 + 1;
		
	printf("===== 가위바위보 게임 =====\n");
        printf("숫자를 입력해 주세요 (1.가위 / 2. 바위 / 3. 보 / x. 끝내기) : ");
	
	scanf("%c", &player);
	while(getchar() != '\n'); // 버퍼 클리어
	
	if (player != '1' && player != '2' && player != '3' && player != 'x') {
	    printf("잘못 입력하셨습니다!!\n\n");
	    continue;
	}
 
	if (player == '1') {
	    printf("당신은 가위. ");
	    
	    if (com == 1)
		printf("컴퓨터도 가위. 비겼습니다.\n");
	    else if (com == 2)
		printf("컴퓨터는 바위. 컴퓨터가 이겼습니다.\n");
	    else
		printf("컴퓨터는 보. 당신이 이겼습니다.\n");
	} else if (player == '2') {
	    printf("당신은 바위. ");
	    
            if (com == 2)
		printf("컴퓨터도 바위. 비겼습니다.\n");
	    else if (com == 3)
		printf("컴퓨터는 보. 컴퓨터가 이겼습니다.\n");
	    else
		printf("컴퓨터는 가위. 당신이 이겼습니다.\n");
	} else if (player == '3') {
	    printf("당신은 보. ");
	    
	    if (com == 3)
		printf("컴퓨터도 보. 비겼습니다.\n");
	    else if (com == 2)
		printf("컴퓨터는 가위. 컴퓨터가 이겼습니다.\n");
	    else
		printf("컴퓨터는 바위. 당신이 이겼습니다.\n");
	}	
    } while (player != 'x');

    printf("안녕히 가세요.\n");
    
    return 0;
}

