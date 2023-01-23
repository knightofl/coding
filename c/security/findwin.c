#include <stdio.h>
#include <windows.h>

// HWND FindWindow(LPCTSTR lpClassName, LPCTSTR lpWindowName);

int main(int argc, char *argv[])
{
    printf("FindWindow Exam.\n");

    if (FindWindow("notepad", 0))
        MessageBox(0, "Debugger Detected!!", "Warning", MB_OK);
    else
        printf("Normal Execution!!\n");
    
    
    return 0;
}
