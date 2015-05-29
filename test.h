#ifndef _TEST_H
#define _TEST_H

#include "pluginmain.h"

//menu identifiers
#define MENU_DUMP 0
#define MENU_TEST 1
#define MENU_SELECTION 2
#define MENU_FILEOFFSET 3
#define MENU_GRAPH_SELECTION 4
#define MENU_GRAPH_FUNCTION 5

#define MENU_DISASM_ADLER32 6
#define MENU_DUMP_ADLER32 7
#define MENU_STACK_ADLER32 8
#define MENU_DISASM_GRAPH_SELECTION 9
#define MENU_DISASM_GRAPH_FUNCTION 10

//functions
void testInit(PLUG_INITSTRUCT* initStruct);
void testStop();
void testSetup();

#endif // _TEST_H
