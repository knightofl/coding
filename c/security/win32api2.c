#include <windows.h>
#include <stdio.h>
#include <string.h>

void error()
{
    MessageBox(0, "Error!!", "Warning", MB_OK);
    printf("Operation Failed!!\n");

    exit(1);
}

int main(int argc, char *argv[])
{
    char name[20] = {0};
    char buffer[30] = {0};
    DWORD dw;
    HANDLE hFile;

    printf("Input File Name : ");
    gets(name);

    hFile = CreateFile(name, GENERIC_READ | GENERIC_WRITE, 0, 0,
                       OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, 0);

    if (hFile == INVALID_HANDLE_VALUE)
        error();
    printf("Open Complete!!\n");

    if (!ReadFile(hFile, buffer, sizeof(buffer), &dw, 0))
        error();
    printf("Read Complete!!\n");

    ShellExecute(NULL, "open", buffer, 0, 0, SW_SHOW);
    
    CloseHandle(hFile);
    
    return 0;
}
