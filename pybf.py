'''

 ******                    **            ****                 **           **            **                                           **
/*////**                  //            /**/                 /**          /**           /**                  ******                  /**
/*   /**  ******  ******   ** *******  ****** **   **  ***** /**  **      /** *******  ******  *****  ******/**///** ******  *****  ******  *****  ******
/******  //**//* //////** /**//**///**///**/ /**  /** **///**/** **       /**//**///**///**/  **///**//**//*/**  /**//**//* **///**///**/  **///**//**//*
/*//// ** /** /   ******* /** /**  /**  /**  /**  /**/**  // /****        /** /**  /**  /**  /******* /** / /******  /** / /*******  /**  /******* /** /
/*    /** /**    **////** /** /**  /**  /**  /**  /**/**   **/**/**       /** /**  /**  /**  /**////  /**   /**///   /**   /**////   /**  /**////  /**
/******* /***   //********/** ***  /**  /**  //******//***** /**//**      /** ***  /**  //** //******/***   /**     /***   //******  //** //******/***
///////  ///     //////// // ///   //   //    //////  /////  //  //       // ///   //    //   ////// ///    //      ///     //////    //   ////// ///

DESCRIPTION:
    Brainfuck interpreter written in Python.

    Windows: py pybf.py test.bf
    Linux: python3 pybf.py test.bf

DEVELOPER:
    NAME: MorcilloSanz
    EMAIL: amorcillosanz@gmail.com
    TWITTER: @MorcilloSanz

VERSION:
    1.0

MIT License

Copyright (c) 2020 MorcilloSanz
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

import sys

#Operators
INCREASE = '+'
DECREASE = '-'
LEFT_SHIFT = '<'
RIGHT_SHIFT = '>'
LOOP_START = '['
LOOP_END = ']'
PRINT = '.'
INPUT = ','

#Only files whose extension is .bf will be executed
EXTENSION = '.bf'

class Interpreter():

    global INCREASE
    global DECREASE
    global LEFT_SHIFT
    global RIGHT_SHIFT
    global LOOP_START
    global LOOP_END
    global PRINT
    global INPUT

    def __init__(self):
        self.restart()

    def __executeLoop(self, code):
        pass

    def restart(self):
        self.buffer = [0]
        self.position = 0
        self.output = ''
        self.loopStart = 0
        self.loopEnd = 0
        self.output = ''

    def executeCode(self, code):
        index = 0
        for c in code:
            if(c == INCREASE):
                self.buffer[self.position] += 1
            elif(c == DECREASE):
                if(self.buffer[self.position] > 0):
                    self.buffer[self.position] -= 1
            elif(c == LEFT_SHIFT):
                if(self.position > 0):
                    self.position -= 1
            elif(c == RIGHT_SHIFT):
                if(self.position >= len(self.buffer) - 1):
                    self.buffer.append(0)
                self.position += 1
            elif(c == LOOP_START):
                self.loopStart = index
            elif(c == LOOP_END):
                self.loopEnd = index
                if(self.buffer[self.position] > 0):
                    loopCode = ""
                    for i in range(self.loopEnd - self.loopStart + 1):
                        loopCode += code[self.loopStart + i]
                    self.executeCode(loopCode)
                else:
                    continue
            elif(c == PRINT):
                self.output = self.output + chr(self.buffer[self.position])
            elif(c == INPUT):
                value = input('Input: ')
                if(len(value) > 1):
                    print('Only ' + value[0] + ' will be considered')
                self.buffer[self.position] = ord(value[0])
            index += 1

    def getOutput(self):
        return self.output

def runProgram(interpreter, filePath):
    code = ''
    file = open(filePath, 'r')
    for line in file:
        code = code + line
    file.close()
    interpreter.executeCode(code)
    print(interpreter.getOutput())
    interpreter.restart()

files = []
interpreter = Interpreter()
if(len(sys.argv) > 1):
    for a in sys.argv:
        if(a.find(EXTENSION) != -1):
            files.append(a)

for f in files:
    print('File: ' + f)
    runProgram(interpreter, f)
    print('')
