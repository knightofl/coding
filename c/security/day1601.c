#include <stdio.h>

int main(int argc, char *argv[])
{
    typedef struct account
    {
        int deposit;
        int payment;
        int balance;
    } account;

    account acc;

    acc.deposit = 10000;
    acc.payment = 5000;
    acc.balance = acc.deposit - acc.payment;

    printf("���� : %d\n", acc.deposit);
    printf("��� : %d\n", acc.payment);
    printf("�ܾ� : %d\n", acc.balance);
    
    return 0;
}
