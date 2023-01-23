#include <windows.h>

int main(int argc, char *argv[])
{
    HMODULE hModule;

    hModule = LoadLibrary("c:\\dlldll1.dll");

    if (hModule)
        OutputDebugString("Load Succeed!!");
    else
        OutputDebugString("Load Fail!!");

    if (hModule)
        FreeLibrary(hModule);
    
    
    return 0;
}
