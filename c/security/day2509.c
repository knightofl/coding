#include <stdio.h>

int scmp(char *, char *);

int main(int argc, char *argv[])
{
    char str1[10] = "Hello";
    char str2[10] = "He2lo";
    char str3[10] = "Heplo";

    int result;

    result = scmp(str1, str2);
    printf("result : %d\n", result);

    result = scmp(str1, str3);
    printf("result : %d\n", result);

    str2[2] = 'l';
    result = scmp(str1, str2);
    printf("result : %d\n", result);

    result = scmp("abc", "abcd");
    printf("result : %d\n", result);

    return 0;
}

int scmp(char *str1, char *str2)
{
    int cmp = 0;
    int i = 0;

    while ((str1[i] && str2[i]) && (str1[i] == str2[i]))
            i++;
 
    if (str1[i] > str2[i])
        cmp = 1;
    else if (str1[i] < str2[i])
        cmp = -1;
    
    return cmp;

}

/*
int scmp(const char *str1, const char *str2)
{
    for (; *str1 == *str2; str1++, str2++)
        if (*str1 == '\0')
            return 0;

	return ((*(unsigned char *)str1 < *(unsigned char *)str2) ? -1 : +1);
}
*/