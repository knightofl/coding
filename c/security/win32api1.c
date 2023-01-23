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
    char fName[30] = {0};
    DWORD dw;
    HANDLE hFile;

    printf("Input Create File Name : ");
    gets(name);

    hFile = CreateFile(name, GENERIC_READ | GENERIC_WRITE, 0, 0,
                       CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, 0);

    if (hFile == INVALID_HANDLE_VALUE)
        error();
    printf("Create Complete!!\n");

    printf("Input Program Name or Path : ");
    gets(fName);

    if (!WriteFile(hFile, fName, strlen(name), &dw, 0))
        error();
    printf("Input Complete!!\n");
    
    CloseHandle(hFile);
    
    return 0;
}
