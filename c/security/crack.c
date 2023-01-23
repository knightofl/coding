#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

int main()
{
    int pid;
    char buffer[BUFSIZ];

    int fd_p2c[2]; //parent -> child
    int fd_c2p[2]; //child -> parent

    int n1, n2;

    srand(time(0));
    
    if (pipe(fd_p2c) || pipe(fd_c2p) != 0) {
        perror("pipe error!\n");
        exit(EXIT_FAILURE);
    }

    pid = fork();
    
    if (pid == -1) {
        perror("fork error!\n");
        exit(EXIT_FAILURE);
    } else if (pid == 0) { //child process
        dup2(fd_c2p[1], 1); //stdout to c2p input
        dup2(fd_p2c[0], 0); //stdin to p2c output
        execl("./justone", "justone", NULL); 
        perror("execl error!\n");
        exit(EXIT_FAILURE);
    } else { //parent process
        n1 = rand() /10000;
        n2 = rand() /10000;  

        sprintf(buffer, "%d", n1+n2);
        write(fd_p2c[1], buffer, BUFSIZ);
        
        read(fd_c2p[0], buffer, BUFSIZ);
        printf("%s\n", buffer);
    }

    return 0;
}
