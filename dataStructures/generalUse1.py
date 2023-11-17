
#definición de las distintas estrucutras de datos necesarias para el programa

class Dictionary:

    #constructor
    def __init__( self, name ):
        self.name = name
        self.dictionary = {}

    #setters and getters
    def setName(self, newName):
        self.name = newName
    
    def setDictioanry(self, newDictionary):
        self.dictionary = newDictionary

    def getName(self):
        return self.name

    def getDictionary(self):
        return self.dictionary

    #general methods

    def addElement(self, key, newElement):
        self.getDictionary()[ key ] = newElement

    def getElement(self, key):
        return self.getDictionary()[ key ]
    
    def editElement(self, key, newElement):
        self.getDictionary()[ key ] = newElement


class Stack:

    #constructor    
    def __init__(self, name):
        self.name = name
        self.stack = [0] #vacía, cero por default
        self.stackHead = self.stack[0]
        self.indexHead = 0

    #setter and getters
    def setName(self, newName):
        self.name = newName

    def setStackHead(self, newHead):
        self.stackHead = newHead
    
    def setStack(self, newStack):
        self.stack = newStack

    def getName(self):
        return self.name

    def getStackHead(self):
        return self.stackHead
    
    def getStack(self):
        return self.stack
    
    #general methods to the class
    def push(self, newElement):
        self.getStack().append( newElement )
        self.indexHead = len( self.getStack() ) - 1
    
    def pop(self, index):
        self.getStack().pop( index )
        self.indexHead = len( self.getStack() ) - 1

""" creación de las estructas y los datos """

Flags = Dictionary("flags")
Flags.addElement("CF",  False)
Flags.addElement("OF",  False)
Flags.addElement("ZF",  False)
Flags.addElement("EF",  False)
Flags.addElement("GF",  False)
Flags.addElement("SMF", False)

Registers = Dictionary("registers")
Registers.addElement("r1",  "0000")
Registers.addElement("r2",  "0001")
Registers.addElement("r3",  "0010")
Registers.addElement("r4",  "0011")
Registers.addElement("r5",  "0100")
Registers.addElement("r6",  "0101")
Registers.addElement("rR",  "0110")
Registers.addElement("rW",  "0111")
Registers.addElement("rSA", "1000")
Registers.addElement("rSF", "1001")

Instructions = Dictionary("instructions")
Instructions.addElement("add",  "000000")
Instructions.addElement("sub",  "000001")
Instructions.addElement("mul",  "000010")
Instructions.addElement("cmp",  "000011")
Instructions.addElement("divC", "000100")
Instructions.addElement("divR", "000101")
Instructions.addElement("and",  "000110")
Instructions.addElement("or",   "000111")
Instructions.addElement("xor",  "001000")
Instructions.addElement("shl",  "001001")
Instructions.addElement("shr",  "001010")
Instructions.addElement("rol",  "001011")
Instructions.addElement("ror",  "001100")
Instructions.addElement("test", "001101")
Instructions.addElement("mov",  "001110")
Instructions.addElement("wrt",  "001111")
Instructions.addElement("read", "010000")
Instructions.addElement("call", "010001")
Instructions.addElement("puAS", "010010")
Instructions.addElement("popSF","010011")
Instructions.addElement("popAS","010100")
Instructions.addElement("jmp",  "010101")
Instructions.addElement("je",   "010110")
Instructions.addElement("jne",  "010111")
Instructions.addElement("ja",   "011000")
Instructions.addElement("jae",  "011001")
Instructions.addElement("jb",   "011010")
Instructions.addElement("jbe",  "011011")
Instructions.addElement("not",  "011100")