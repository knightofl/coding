#define _WIN32_WINNT 0x501
#include <stdio.h>
#include <windows.h>

// BOOL WINAPI IsDebuggerPresent(void);

int main()
{
    printf("IsDebuggerPresent Exam.\n");

    if (IsDebuggerPresent()) {
        printf("Debugger Detected!!\n");
        system("pause");
        exit(0);
    } else
        printf("Normal Execution!!\n");

    return 0;

}
