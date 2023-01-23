#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    unsigned char p[126158] = {0};
    int i;

    FILE *fr = fopen("c:\\cpr\\level6.exe", "rb");
    FILE *fw = fopen("c:\\cpr\\level6+.exe", "wb");

    if (fr)
        fread(p, 126158, 1, fr);

    for (i= 0; i < 126158; i += 10)
        memmove(p + i, p + i + 1, 126158 - i -1);


    if (fw)
        fwrite(p, 126158, 1, fw);

    fclose(fw);
    fclose(fr);

    return 0;
}
