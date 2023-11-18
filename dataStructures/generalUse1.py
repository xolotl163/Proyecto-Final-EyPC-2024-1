
#definición de las distintas estrucutras de datos necesarias para el programa

class Dictionary:

    #constructor
    def __init__( self, name ):
        self.name = name
        self.mainDict = {}

    #setters and getters
    def setName(self, newName):
        self.name = newName
    
    def setMainDict(self, newDictionary):
        self.dictionary = newDictionary

    def setDictionary(self, dictionary, newDictionary):
        self.getMainDict()[dictionary]

    def getName(self):
        return self.name

    def getMainDict(self):
        return self.mainDict

    def getDictionary(self, nameDict):
        return self.getMainDict()[ nameDict ]

    def getElement(self, dictionary, key):
        return self.getDictionary()[ dictionary ][ key ]

    #general methods
    def addDictionary(self, nameDictionary):
        self.getMainDict()[nameDictionary] = {}

    def addElement(self, dictionary, key, newElement):
        self.getMainDict()[ dictionary ][ key ] = newElement
    
    def editElement(self, dictionary, key, newElement):
        self.getMainDict()[ dictionary ][ key ] = newElement

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

#instanciación de los objetos
Flags = Dictionary("flags")
Registers = Dictionary("registers")
Instructions = Dictionary("instructions")

#creación de los diccionarios
Flags.addDictionary("bool")
Flags.addDictionary("binary")
Registers.addDictionary("binary")
Instructions.addDictionary("binary")

#se añaden los datos
Flags.addElement( "bool", "CF",  False)
Flags.addElement( "bool", "OF",  False)
Flags.addElement( "bool", "ZF",  False)
Flags.addElement( "bool", "EF",  False)
Flags.addElement( "bool", "GF",  False)
Flags.addElement( "bool", "SMF", False)

Flags.addElement( "binary", "CF",  "0000")
Flags.addElement( "binary", "OF",  "0001")
Flags.addElement( "binary", "ZF",  "0010")
Flags.addElement( "binary", "EF",  "0011")
Flags.addElement( "binary", "GF",  "0100")
Flags.addElement( "binary", "SMF", "0101")

Registers.addElement( "binary", "r1",  "0000")
Registers.addElement( "binary", "r2",  "0001")
Registers.addElement( "binary", "r3",  "0010")
Registers.addElement( "binary", "r4",  "0011")
Registers.addElement( "binary", "r5",  "0100")
Registers.addElement( "binary", "r6",  "0101")
Registers.addElement( "binary", "rR",  "0110")
Registers.addElement( "binary", "rW",  "0111")
Registers.addElement( "binary", "rSA", "1000")
Registers.addElement( "binary", "rSF", "1001")

Instructions.addElement( "binary", "add",  "000000")
Instructions.addElement( "binary", "sub",  "000001")
Instructions.addElement( "binary", "mul",  "000010")
Instructions.addElement( "binary", "cmp",  "000011")
Instructions.addElement( "binary", "divC", "000100")
Instructions.addElement( "binary", "divR", "000101")
Instructions.addElement( "binary", "and",  "000110")
Instructions.addElement( "binary", "or",   "000111")
Instructions.addElement( "binary", "xor",  "001000")
Instructions.addElement( "binary", "shl",  "001001")
Instructions.addElement( "binary", "shr",  "001010")
Instructions.addElement( "binary", "rol",  "001011")
Instructions.addElement( "binary", "ror",  "001100")
Instructions.addElement( "binary", "test", "001101")
Instructions.addElement( "binary", "mov",  "001110")
Instructions.addElement( "binary", "wrt",  "001111")
Instructions.addElement( "binary", "read", "010000")
Instructions.addElement( "binary", "call", "010001")
Instructions.addElement( "binary", "puAS", "010010")
Instructions.addElement( "binary", "popSF","010011")
Instructions.addElement( "binary", "popAS","010100")
Instructions.addElement( "binary", "jmp",  "010101")
Instructions.addElement( "binary", "je",   "010110")
Instructions.addElement( "binary", "jne",  "010111")
Instructions.addElement( "binary", "ja",   "011000")
Instructions.addElement( "binary", "jae",  "011001")
Instructions.addElement( "binary", "jb",   "011010")
Instructions.addElement( "binary", "jbe",  "011011")
Instructions.addElement( "binary", "not",  "011100")