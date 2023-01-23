#include <windows.h>
#include <stdio.h>
#include <string.h>
#include <TlHelp32.h>

BOOL injectDll(DWORD, char*);
BOOL ejectDll(DWORD, char*);
BOOL moduleList(DWORD);
void inject(void);
void eject(void);
void pList(void);
void mList(void);


// fflush(stdin); system("cls");
// 두 함수는 윈도우 환경에서만 정상작동



int main(int argc, char *argv[])
{
    int hChoice;

    do {
        system("cls");

        printf("==== DLL Handling ====\n");
        printf("== 1. DLL Injection ==\n");
        printf("== 2. DLL Ejection  ==\n");
        printf("== 3. Process List  ==\n");
        printf("== 4. Module List   ==\n");
        printf("== 5. Quit          ==\n");
        printf("======================\n\n");

        printf("=> What do you want? => ");
        fflush(stdin);
        scanf("%d", &hChoice);

        switch (hChoice) {
        case 1:
            inject();
            break;
        case 2:
            eject();
            break;
        case 3:
            pList();
            break;
        case 4:
            mList();
            break;
        default:
            break;
        }
    } while (hChoice != 5);

    return 0;
}



void inject(void)
{
    DWORD dwPid;
    char szDllPath[256];

    printf("\n==== DLL Injection ====\n");
    printf("=> Input PID to inject => ");
    fflush(stdin);
    scanf("%d", &dwPid);

    printf("=> Input DLL PATH to inject => ");
    fflush(stdin);
    scanf("%s", szDllPath);
    
    if (injectDll(dwPid, szDllPath))
        printf("Injection Succeeded! ");
    else printf("Injection Failed! ");

    printf("Hit Any Key!");
    fflush(stdin);
    while (!getchar());
}


void eject(void)
{
    DWORD dwPid;
    char szModule[256];

    printf("\n==== DLL Ejection ====\n");
    printf("=> Input PID to eject => ");
    fflush(stdin);
    scanf("%d", &dwPid);
    
    printf("=> Input DLL name or PATH to eject => ");
    fflush(stdin);
    scanf("%s", szModule);

    if (ejectDll(dwPid, szModule))
        printf("Ejection Succeeded! ");
    else printf("Ejection Failed! ");

    printf("Hit Any Key!");
    fflush(stdin);
    while (!getchar());
}


void pList(void)
{
    HANDLE hModuleSnap = INVALID_HANDLE_VALUE;
    PROCESSENTRY32 pe32;
    
    printf("\n==== Process List ====\n");

    hModuleSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    pe32.dwSize = sizeof(PROCESSENTRY32);

    if (Process32First(hModuleSnap, &pe32)) {
        printf("PID\tPROCESS\n");
        
        do {
            printf("%d\t%s\n", pe32.th32ProcessID, pe32.szExeFile);
        } while (Process32Next(hModuleSnap, &pe32));
    }

    CloseHandle(hModuleSnap);

    printf("Hit Any Key!");
    fflush(stdin);
    while (!getchar());
}


void mList(void)
{
    DWORD dwPid;

    printf("\n===== Module List =====\n");
    printf("=> Input PID to list => ");
    fflush(stdin);
    scanf("%d", &dwPid);

    if (moduleList(dwPid))
        printf("Listing Succeeded! ");
    else printf("Listing Failed! ");

    printf("Hit Any Key!");
    fflush(stdin);
    while (!getchar());
}


BOOL injectDll(DWORD dwPid, char* szDllPath)
{
    HMODULE hKernel32;
    HANDLE hProcess, hThread;
    LPVOID pLibRemote;
    LPTHREAD_START_ROUTINE pThreadProc;
    int nLen = strlen(szDllPath) + 1;

    FILE* fDll = fopen(szDllPath, "rb");
    
    if (!(hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwPid))) {
        printf("PID %d is Error! (%d)\n", dwPid, GetLastError());
        return FALSE;
    }

    if (!fDll) {
        printf("DLL file is not found!\n");
        return FALSE;
    } else fclose(fDll);

    hKernel32 = GetModuleHandle("kernel32.dll");            
    pLibRemote = VirtualAllocEx(hProcess, NULL, nLen, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
    WriteProcessMemory(hProcess, pLibRemote, (LPVOID) szDllPath, nLen, NULL);
    pThreadProc = (LPTHREAD_START_ROUTINE) GetProcAddress(hKernel32, "LoadLibraryA");
    hThread = CreateRemoteThread(hProcess, NULL, 0, pThreadProc, pLibRemote, 0, NULL);

    CloseHandle(hProcess);
    CloseHandle(hThread);

    return TRUE;
}


BOOL ejectDll(DWORD dwPid, char* szModule)
{    
    HANDLE hModuleSnap = INVALID_HANDLE_VALUE;
    MODULEENTRY32 me32;
    HANDLE hProcess, hThread;
    LPTHREAD_START_ROUTINE pThreadProc;
    HMODULE hKernel32;
    BOOL existModule = FALSE;

    hModuleSnap = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE, dwPid);
    me32.dwSize = sizeof(MODULEENTRY32);
 
    if (!Module32First(hModuleSnap, &me32)) {
        printf("Module Creation Error! (%d)\n", GetLastError());
        CloseHandle(hModuleSnap);
        return FALSE;
    }

    do {
        if (!stricmp(me32.szModule, szModule) | !stricmp(me32.szExePath, szModule))
            break;
    } while (existModule = Module32Next(hModuleSnap, &me32));

    if (!existModule) {
        printf("Module is not found!\n");
        CloseHandle(hModuleSnap);
        return FALSE;
    }

    hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwPid);
    hKernel32 = GetModuleHandle("kernel32.dll");
    pThreadProc = (LPTHREAD_START_ROUTINE) GetProcAddress(hKernel32, "FreeLibrary");
    hThread = CreateRemoteThread(hProcess, NULL, 0, pThreadProc, me32.modBaseAddr, 0, NULL);
 
    CloseHandle(hModuleSnap);
    CloseHandle(hProcess);
    CloseHandle(hThread);

    return TRUE;
}


BOOL moduleList(DWORD dwPid)
{
    HANDLE hModuleSnap = INVALID_HANDLE_VALUE;
    MODULEENTRY32 me32;

    hModuleSnap = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE, dwPid);
    me32.dwSize = sizeof(MODULEENTRY32);

    if (!Module32First(hModuleSnap, &me32)) {
        printf("Module Creation Error! (%d)\n", GetLastError());
        CloseHandle(hModuleSnap);
        return FALSE;
    }

    do {
        printf("%s\n", me32.szExePath);
    } while (Module32Next(hModuleSnap, &me32));

    CloseHandle(hModuleSnap);

    return TRUE;
}
