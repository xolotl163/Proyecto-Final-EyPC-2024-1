
"""definición de las distintas estrucutras de datos necesarias para el programa"""

#sección definicion de clases
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
        return self.getMainDict()[ dictionary ][ key ]

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
        self.stack = [] #vacía, cero por default
        self.stackHead = 0
        self.indexHead = 0

    #setter and getters
    def setName(self, newName):
        self.name = newName

    def setStackHead(self, newHead):
        size = len( self.getStack() )
        self.stackHead = self.getStack()[size-1]
        self.indexHead = size-1
    
    def setStack(self, newStack):
        self.stack = newStack

    def getStack(self):
        return self.stack

    def getName(self):
        return self.name

    def getStackHead(self):
        return self.stackHead
    
    #general methods to the class
    def push(self, newElement):

        if len( self.getStackHead() ) == 0:
            self.getStack().append( newElement )
            self.setStackHead( self.getStack()[0] )
        else:
            self.getStack().append( newElement )
            size = len( self.getStack() )
            self.setStackHead( self.getStack()[size-1] )

    def pop(self, index):
        self.getStack().pop( index )
        size = len( self.getStack() )
        self.setStackHead( self.getStack()[size-1] )

"""seccion definicion de funciones"""

class Operations:

    def __init__(self):
        pass

    #funciones auxiliares
    def fillGaps(self, a1, a2 ):

        size1 = len(a1)
        size2 = len(a2)

        if size1 == size2:
            return

        if size1 > size2:

            top = size1
            bottom = size2
            #greater = a1
            smaller = a2

            gap = top - bottom
            for i in range( gap ):
                a2 = "0" + a2

            return a2

        else:
            top = size2
            bottom = size1
            #greater = a2
            smaller = a1

            gap = top - bottom
            for j in range( gap ):
                a1 = "0" + a1

            return a1

    #arimeticas
    def add(self, a1, a2 ):
        a1 = a1 + a2

    def sub(self, a1, a2 ):
        a1 = a1 - a2

    def mul(self, a1, a2 ):
        a1 = a1 * a2

    def cmp(self, a1, a2 ):

        #se ponen a valor inicial (false) las banderas de comparacion
        Flags.getDictionary("bool")["EF"] = False
        Flags.getDictionary("bool")["GF"] = False
        Flags.getDictionary("bool")["SMF"] = False

        if a1 == a2:
            Flags.getDictionary("bool")["EF"] = True
        elif a1 > a2:
            Flags.getDictionary("bool")["GF"] = True
        elif a1 < a2:
            Flags.getDictionary("bool")["SMF"] = True

    def divC(self, a1, a2 ):
        a1 = a1 / a2

    def divR(self, a1, a2 ):
        a1 = a1 % a2

    #logicas
    def AND(self, a1, a2 ):

        self.fillGaps( a1, a2 )
        size = len(a1)

        i = 0
        while i < size:
            if (a1[i] == '1') and (a2[i] == '1'):
                a1[i] == '1'
            elif (a1[i] == '1') and (a2[i] == '0'):
                a1[i] == '0'
            elif (a1[i] == '0') and (a2[i] == '1'):
                a1[i] == '0'
            elif (a1[i] == '0') and (a2[i] == '0'):
                a1[i] == '0'

            i += 1

    def OR(self, a1, a2 ):

        self.fillGaps( a1, a2 )
        size = len(a1)

        i = 0
        while i < size:
            if (a1[i] == '1') or (a2[i] == '1'):
                a1[1] = '1'
            i += 1

    def NOT(self, a1 ):

        size = len(a1)

        i = 0
        while i < size:
            if a1[i] == '1':
                a1[i] = '0'
            elif a1[i] == '0':
                a1[i] = '1'
            i += 1 

    def XOR(self, a1, a2 ):

        self.fillGaps( a1, a2 )
        size = len(a1)

        i = 0
        while i < size:
            if (a1[i] == '1') and (a2[i] == '1'):
                a1[i] == '0'
            elif (a1[i] == '1') and (a2[i] == '0'):
                a1[i] == '1'
            elif (a1[i] == '0') and (a2[i] == '1'):
                a1[i] == '1'
            elif (a1[i] == '0') and (a2[i] == '0'):
                a1[i] == '0'
            i += 1

    def shl(self, a1, n ):

        i = 0
        while i < n:
            a1 = a1 + "0"
            i += 1

    def shr(self, a1, n ):

        i = 0 
        while i < n:
            a1 = "0" + a1
            i += 1

    def ROR(self, a1, n ):

        size = len(a1)
        aux1 = []
        aux2 = []

        A = size - n
        for i in range( A, size ):
            aux1.append( a1[i] )

        B = size - A
        for i in range( 0, B ):
            aux2.append( a1[i] )

        a1 = aux1 + aux2

    def ROL(self, a1, n ):

        size = len(a1)
        aux1 = []
        aux2 = []

        for i in range( 0, n ):
            aux1.append( a1[i] )

        for i in range( n, size ):
            aux2.append( a1[i] )

        a1 = aux2 + aux1

    def test(self, a1, a2 ):
        pass

    #administracion de memoria
    def mov(self, target, origin ):
        Registers.editElement( "data", target, origin )

    def wrt(self, message ):
        print( message )

    def read(self, target ):
        target = input()

    #uso de stacks y funciones
    def call(self, name ):
        pass 

    def puAS(self, a1 ):
        ArgumentStack.push( a1 )

    def popSF(self):
        FunctionStack.pop()

    def popAS(self):
        ArgumentStack.pop()

""" creación de las estructas y los datos """

#instanciación de los objetos
Operations0 = Operations()
Flags = Dictionary("flags")
Registers = Dictionary("registers")
Instructions = Dictionary("instructions")

FunctionStack = Stack("function stack")
ArgumentStack = Stack("argument stack")

#creación de los diccionarios
Flags.addDictionary("bool")
Registers.addDictionary("data")
Instructions.addDictionary("binary")

#se añaden los datos
Flags.addElement( "bool", "CF",  False)
Flags.addElement( "bool", "OF",  False)
Flags.addElement( "bool", "ZF",  False)
Flags.addElement( "bool", "EF",  False)
Flags.addElement( "bool", "GF",  False)
Flags.addElement( "bool", "SMF", False)

Registers.addElement( "data", "r1", None )
Registers.addElement( "data", "r2", None )
Registers.addElement( "data", "r3", None )
Registers.addElement( "data", "r4", None )
Registers.addElement( "data", "r5", None )
Registers.addElement( "data", "r6", None )
Registers.addElement( "data", "rR", None )
Registers.addElement( "data", "rW", None )
Registers.addElement( "data", "rSA", None )
Registers.addElement( "data", "rSF", None )

Instructions.addElement( "binary", "CF",  "0000")
Instructions.addElement( "binary", "OF",  "0001")
Instructions.addElement( "binary", "ZF",  "0010")
Instructions.addElement( "binary", "EF",  "0011")
Instructions.addElement( "binary", "GF",  "0100")
Instructions.addElement( "binary", "SMF", "0101")
Instructions.addElement( "binary", "r1",  "0000")
Instructions.addElement( "binary", "r2",  "0001")
Instructions.addElement( "binary", "r3",  "0010")
Instructions.addElement( "binary", "r4",  "0011")
Instructions.addElement( "binary", "r5",  "0100")
Instructions.addElement( "binary", "r6",  "0101")
Instructions.addElement( "binary", "rR",  "0110")
Instructions.addElement( "binary", "rW",  "0111")
Instructions.addElement( "binary", "rSA", "1000")
Instructions.addElement( "binary", "rSF", "1001")
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