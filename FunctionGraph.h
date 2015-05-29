#ifndef _FUNCTIONGRAPH_H
#define _FUNCTIONGRAPH_H

#include <windows.h>
#include <string>

struct instr_info
{
    ULONG_PTR addr;
    ULONG_PTR jmpaddr;
    std::string instrText;
    std::string comment;
};

typedef ULONG_PTR(*GETINSTRINFO)(ULONG_PTR addr, instr_info* info);

bool make_flowchart(ULONG_PTR start, ULONG_PTR end, const wchar_t* szTargetFile, GETINSTRINFO getInstrInfo);

#endif //_FUNCTIONGRAPH_H