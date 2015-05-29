#include "FunctionGraph.h"
#include <list>
#include <set>
#include <stdio.h>

struct previous_edge_struct_s
{
    ULONG_PTR source;
    ULONG_PTR targetfalse;
    ULONG_PTR targettrue;
};

#define TEXTLEN 256

static char vcg_params[] =  "manhattan_edges: yes\n"
                            "layoutalgorithm: mindepth\n"
                            "finetuning: no\n"
                            "layout_downfactor: 100\n"
                            "layout_upfactor: 0\n"
                            "layout_nearfactor: 0\n"
                            "xlspace: 12\n"
                            "yspace: 30\n"
                            "colorentry 32: 0 0 0\n"
                            "colorentry 33: 0 0 255\n"
                            "colorentry 34: 0 0 255\n"
                            "colorentry 35: 128 128 128\n"
                            "colorentry 36: 128 128 128\n"
                            "colorentry 37: 0 0 128\n"
                            "colorentry 38: 0 0 128\n"
                            "colorentry 39: 0 0 255\n"
                            "colorentry 40: 0 0 255\n"
                            "colorentry 41: 0 0 128\n"
                            "colorentry 42: 0 128 0\n"
                            "colorentry 43: 0 255 0\n"
                            "colorentry 44: 0 128 0\n"
                            "colorentry 45: 255 128 0\n"
                            "colorentry 46: 0 128 0\n"
                            "colorentry 47: 128 128 255\n"
                            "colorentry 48: 255 0 0\n"
                            "colorentry 49: 128 128 0\n"
                            "colorentry 50: 1 1 1\n"
                            "colorentry 51: 192 192 192\n"
                            "colorentry 52: 0 0 255\n"
                            "colorentry 53: 0 0 255\n"
                            "colorentry 54: 0 0 255\n"
                            "colorentry 55: 128 128 128\n"
                            "colorentry 56: 128 128 255\n"
                            "colorentry 57: 0 128 0\n"
                            "colorentry 58: 0 0 128\n"
                            "colorentry 59: 0 0 255\n"
                            "colorentry 60: 128 0 128\n"
                            "colorentry 61: 0 128 0\n"
                            "colorentry 62: 0 128 0\n"
                            "colorentry 63: 0 128 64\n"
                            "colorentry 64: 0 0 128\n"
                            "colorentry 65: 0 0 128\n"
                            "colorentry 66: 255 0 255\n"
                            "colorentry 67: 128 128 0\n"
                            "colorentry 68: 0 0 128\n"
                            "colorentry 69: 0 0 255\n"
                            "colorentry 70: 0 0 128\n"
                            "colorentry 71: 0 0 255\n"
                            "colorentry 72: 0 0 0\n"
                            "colorentry 73: 255 255 255\n"
                            "colorentry 74: 192 187 175\n"
                            "colorentry 75: 0 255 255\n"
                            "colorentry 76: 0 0 0\n"
                            "colorentry 77: 128 0 0\n"
                            "colorentry 78: 128 128 128\n"
                            "colorentry 79: 128 128 0\n"
                            "colorentry 80: 255 0 255\n"
                            "colorentry 81: 0 0 0\n"
                            "colorentry 82: 0 0 255\n"
                            "colorentry 83: 100 255 255\n";

//escape comments
static void sanitize(const char* comment, char* cleaned)
{
    char* t;
    for(t = cleaned; *comment; comment++)
    {
        if(*comment == '"')
        {
            *t++ = '\\';
            *t = '"';
        }
        else if(*comment == '\\')
        {
            *t++ = '\\';
            *t = '\\';
        }
        else
        {
            *t = *comment;
        }
        t++;
    }
    *t = '\0';
}

bool make_flowchart(ULONG_PTR start, ULONG_PTR end, const wchar_t* szTargetFile, GETINSTRINFO getInstrInfo)
{
    HANDLE temp_file = CreateFileW(szTargetFile, GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    if(temp_file == INVALID_HANDLE_VALUE)
        return false;

    char buffer[TEXTLEN * 2 + 4];
    ULONG_PTR currentnode = start;

    int writelen = sprintf(buffer, "graph: {\ntitle: \"Graph of %p\"\n", start);
    DWORD len_written;
    WriteFile(temp_file, buffer, (DWORD) writelen, &len_written, NULL);
    WriteFile(temp_file, vcg_params, (DWORD) strlen(vcg_params), &len_written, NULL);
    writelen = sprintf(buffer, "node: { title: \"%p\" vertical_order: 0 color: 83 fontname: \"courR12\" label: \"%p:", currentnode, currentnode);
    WriteFile(temp_file, buffer, (DWORD) writelen, &len_written, NULL);

    std::set<ULONG_PTR> nodelist; //list of node addresses, just to make sure we are not handling nodes multiple times
    std::list<instr_info> disasmlist;
    ULONG_PTR psize = 0;
    ULONG_PTR current_addr = start;

    // first pass - disassemble instructions and enumerate nodes
    do
    {
        current_addr += psize;

        //get instr_info
        instr_info disasm_result;
        ULONG_PTR next_addr = getInstrInfo(current_addr, &disasm_result);
        psize = next_addr - current_addr;
        if(psize <= 0)
            psize = 1;

        //add instr_info to list
        disasmlist.push_back(disasm_result);

        // enumerate nodes
        if(currentnode == 0)
        {
            currentnode = current_addr;
            nodelist.insert(currentnode);
        }
        if((disasm_result.jmpaddr >= start) && (disasm_result.jmpaddr < end))
        {
            // this is a jump - start of an edge and pointer to a node
            nodelist.insert(disasm_result.jmpaddr);
            currentnode = 0; // update current_addrnode on next pass
        }
    }
    while(current_addr + psize <= end);

    // walk through saved disasm list and split into nodes
    currentnode = start;
    bool orphannode = true;
    previous_edge_struct_s previous_edge;
    memset(&previous_edge, 0, sizeof(previous_edge_struct_s));
    std::string edgelist;
    for(std::list<instr_info>::iterator i = disasmlist.begin(); i != disasmlist.end(); ++i)
    {
        instr_info disasm_result = *i;
        current_addr = disasm_result.addr;

        //node contents (address)
        if(nodelist.find(current_addr) != nodelist.end()) //found current_addr in set
        {
            if(orphannode)
            {
                writelen = sprintf(buffer, "edge: { sourcename: \"%p\" targetname: \"%p\" }\n", currentnode, current_addr);
                edgelist += buffer;
            }
            orphannode = true;
            currentnode = current_addr;
            writelen = sprintf(buffer, "\" }\n");
            WriteFile(temp_file, buffer, (DWORD) writelen, &len_written, NULL);
            writelen = sprintf(buffer, "node: { title: \"%p\" color: 83 fontname: \"courR12\" label: \"%p:", current_addr, current_addr);
            WriteFile(temp_file, buffer, (DWORD) writelen, &len_written, NULL);
        }

        //node contents (disassembly)
        if(disasm_result.comment.length())
        {
            char clean_comment[TEXTLEN * 2];
            sanitize(disasm_result.comment.c_str(), clean_comment);
            writelen = sprintf(buffer, "\n%s\t; %s", disasm_result.instrText.c_str(), clean_comment);
        }
        else
        {
            writelen = sprintf(buffer, "\n%s", disasm_result.instrText.c_str());
        }

        WriteFile(temp_file, buffer, (DWORD)writelen, &len_written, NULL);

        if(previous_edge.source != 0)
        {
            // append stored edge info with currentnode info to edgelist buffer
            previous_edge.targetfalse = currentnode;
            writelen = sprintf(buffer, "edge: { sourcename: \"%p\" targetname: \"%p\" label: \"false\" color: red }\n", previous_edge.source, previous_edge.targetfalse);
            edgelist += buffer;
            writelen = sprintf(buffer, "edge: { sourcename: \"%p\" targetname: \"%p\" label: \"true\" color: darkgreen }\n", previous_edge.source, previous_edge.targettrue);
            edgelist += buffer;
            previous_edge.source = 0;
        }

        if((disasm_result.jmpaddr >= start) && (disasm_result.jmpaddr < end))
        {
            // this is a jump - start of an edge and pointer to a node
            orphannode = false;
            previous_edge.source = currentnode;
            previous_edge.targettrue = disasm_result.jmpaddr;
            previous_edge.targetfalse = 0;

            if(!_stricmp(disasm_result.instrText.substr(0, 3).c_str(), "jmp"))
            {
                // straight jmp, no true/false
                writelen = sprintf(buffer, "edge: { sourcename: \"%p\" targetname: \"%p\" }\n", previous_edge.source, previous_edge.targettrue);
                edgelist += buffer;
                previous_edge.source = 0;
            }
        }
    }

    // close last node
    writelen = sprintf(buffer, "\" vertical_order: %d }\n", nodelist.size());
    WriteFile(temp_file, buffer, (DWORD)writelen, &len_written, NULL);

    // write edgelist
    WriteFile(temp_file, edgelist.c_str(), (DWORD)edgelist.length(), &len_written, NULL);

    writelen = sprintf(buffer, "}\n");
    WriteFile(temp_file, buffer, (DWORD)writelen, &len_written, NULL);

    CloseHandle(temp_file);

    return true;
}
