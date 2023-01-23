#include <windows.h>

typedef void (*PFNFUNC)();
PFNFUNC fnTest;

int main(int argc, char *argv[])
{
    HMODULE hModule;
    hModule = LoadLibrary("c:\\dlldll2.dll");

    if (hModule) {
        fnTest = (PFNFUNC)GetProcAddress(hModule, "test");
        if (fnTest) fnTest();
    }

    if (hModule) FreeLibrary(hModule);
        
    
    return 0;
}
