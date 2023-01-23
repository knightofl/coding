#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int i;
    for (i = 0; i < 4294967295U; i++) {
        srand(i);
        if (rand() == 0x5542)
            if(rand() == 0x5a43)
                if(rand() == 0x304d)
                    printf("%d\n", i);
    }
    
    return 0;
}
