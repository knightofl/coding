#include <windows.h>

// extern "C"
void __declspec(dllexport) test()
{
    MessageBox(NULL, "Export Function Test!!", "", MB_OK);
}

BOOL APIENTRY DllMain(HANDLE hModule, DWORD ul_reason_for_call, LPVOID lpResreved)
{
    switch (ul_reason_for_call) {
    case DLL_PROCESS_ATTACH:
        MessageBox(NULL, "DLL Attached!!", "ATTACH", MB_OK);
        break;
    case DLL_PROCESS_DETACH:
        MessageBox(NULL, "DLL Detached!!", "DETACH", MB_OK);
        break;
    case DLL_THREAD_ATTACH:
        break;
    case DLL_THREAD_DETACH:
        break;
    }

    return TRUE;
}
