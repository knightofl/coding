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
		
	printf("===== ���������� ���� =====\n");
        printf("���ڸ� �Է��� �ּ��� (1.���� / 2. ���� / 3. �� / x. ������) : ");
	
	scanf("%c", &player);
	while(getchar() != '\n'); // ���� Ŭ����
	
	if (player != '1' && player != '2' && player != '3' && player != 'x') {
	    printf("�߸� �Է��ϼ̽��ϴ�!!\n\n");
	    continue;
	}
 
	if (player == '1') {
	    printf("����� ����. ");
	    
	    if (com == 1)
		printf("��ǻ�͵� ����. �����ϴ�.\n");
	    else if (com == 2)
		printf("��ǻ�ʹ� ����. ��ǻ�Ͱ� �̰���ϴ�.\n");
	    else
		printf("��ǻ�ʹ� ��. ����� �̰���ϴ�.\n");
	} else if (player == '2') {
	    printf("����� ����. ");
	    
            if (com == 2)
		printf("��ǻ�͵� ����. �����ϴ�.\n");
	    else if (com == 3)
		printf("��ǻ�ʹ� ��. ��ǻ�Ͱ� �̰���ϴ�.\n");
	    else
		printf("��ǻ�ʹ� ����. ����� �̰���ϴ�.\n");
	} else if (player == '3') {
	    printf("����� ��. ");
	    
	    if (com == 3)
		printf("��ǻ�͵� ��. �����ϴ�.\n");
	    else if (com == 2)
		printf("��ǻ�ʹ� ����. ��ǻ�Ͱ� �̰���ϴ�.\n");
	    else
		printf("��ǻ�ʹ� ����. ����� �̰���ϴ�.\n");
	}	
    } while (player != 'x');

    printf("�ȳ��� ������.\n");
    
    return 0;
}

