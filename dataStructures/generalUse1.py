
#definición de las distintas estrucutras de datos necesarias para el programa

class dictionary:

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

    def addElement(self, newElement, key):
        self.getDictionary()[ key, newElement ]

    def getElement(self, key):
        return self.getDictionary()[ key ]
    
    def editElement(self, key, newElement):
        self.getDictionary()[ key ] = newElement


class Stack:
    
    def __init__(self, name):
        self.name = name
        self.stack = [0]
        self.stackHead = self.stack[0]

""" creación de las estructas y los datos """

flags = dictionary("flags")
flags.addElement("CF", False)
flags.addElement("OF", False)
flags.addElement("ZF", False)
flags.addElement("EF", False)
flags.addElement("GF", False)
flags.addElement("SMF", False)

registers = dictionary("registers")
registers.addElement("r1", "0000")
registers.addElement("r2", "0001")
registers.addElement("r3", "0010")
registers.addElement("r4", "0011")
registers.addElement("r5", "0100")
registers.addElement("r6", "0101")
registers.addElement("rR", "0110")
registers.addElement("rW", "0111")
registers.addElement("rSA", "1000")
registers.addElement("rSF", "1001")

instructions = dictionary("instructions")
instructions.addElement("add",  "000000")
instructions.addElement("sub",  "000001")
instructions.addElement("mul",  "000010")
instructions.addElement("cmp",  "000011")
instructions.addElement("divC", "000100")
instructions.addElement("divR", "000101")
instructions.addElement("and",  "000110")
instructions.addElement("or",   "000111")
instructions.addElement("xor",  "001000")
instructions.addElement("shl",  "001001")
instructions.addElement("shr",  "001010")
instructions.addElement("rol",  "001011")
instructions.addElement("ror",  "001100")
instructions.addElement("test", "001101")
instructions.addElement("mov",  "001110")
instructions.addElement("wrt",  "001111")
instructions.addElement("read", "010000")
instructions.addElement("call", "010001")
instructions.addElement("puAS", "010010")
instructions.addElement("popSF","010011")
instructions.addElement("popAS","010100")
instructions.addElement("jmp",  "010101")
instructions.addElement("je",   "010110")
instructions.addElement("jne",  "010111")
instructions.addElement("ja",   "011000")
instructions.addElement("jae",  "011001")
instructions.addElement("jb",   "011010")
instructions.addElement("jbe",  "011011")
instructions.addElement("not",  "011100")