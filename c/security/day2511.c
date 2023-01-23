#include <stdio.h>

char* sstr(char *, char *);
int slen(char *);

int main(int argc, char *argv[])
{
    char string[20] = "apapple";
    char *search = "app";
    char *result;

    result = sstr(string, search);

    printf("string address : %p\n", string);
    printf("result address : %p\n", result);
    printf("result : %s\n", result);
    
    return 0;
}

char* sstr(char *str, char *sch)
{
    int i, j;

    for (i = 0; i <= slen(str) - slen(sch); i++) {
        for (j = 0; j < slen(sch); j++)
            if (str[i+j] != sch[j])
                break;
        if (!sch[j])
            return str + i;
    }
    
    return NULL;
}

int slen(char* str)
{
    int len = 0;
    while (str[len++]);
    
    return len - 1;
}

/*
char* sstr(const char *in, const char *str)
{
    char c;
    size_t len;

    c = *str++;
    if (!c)
        return (char *) in;	// Trivial empty string case

    len = strlen(str);

    do {
        char sc;

        do {
            sc = *in++;
            if (!sc)
                return (char *) 0;
        } while (sc != c);
    } while (strncmp(in, str, len) != 0);

    return (char *) (in - 1);
}
*/