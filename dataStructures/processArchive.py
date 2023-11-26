
from . import generalUse1 as generalUses
from . import observatorPattern as Obs

""" definicion e inicializacion de variables y objetos necesarios para el programa """
flags = generalUses.Flags
registers = generalUses.Registers
instructions = generalUses.Instructions
operations = generalUses.Operations0

""" definicion de clases """
class processArchive( Obs.Observator ):

    def __init__(self, name):
        self.name = name

    def update(self, type, archiveRute):
        
        match type:
            
            case "translate":

                with open( archiveRute, 'r' ) as file:
                    content = file.readlines()
                    print("Entrada: ")
                    print( content )

                actualWord = []
                outPut = []
                translatedLine = []

                for line in content:

                    if line == "\n":
                        continue
                    else:
                        for letter in line:
                            if letter == " " or letter == "\n":
                                translatedLine.append( instructions.getElement( "binary", "".join(actualWord) ) )
                                actualWord = []
                            else:
                                actualWord.append( letter )

                    outPut.append( translatedLine )
                    actualWord = []
                    translatedLine = []

                print( "\nProceso 1: " )
                print( outPut )

                for i in range( len(outPut)):
                    
                    line = outPut[i]

                    for j in range( len(line)):

                        word = line[j]

                        if len(word) == 6:
                            continue
                        else:
                            size1 = 9
                            size2 = len( word )

                            if size1 == size2:
                                continue

                            if size1 > size2:
                                top = size1
                                bottom = size2
                                #greater = a1
                                smaller = word

                                gap = top - bottom
                                k = 0
                                while k < gap:
                                    smaller = "0" + smaller
                                    k += 1
                                
                                outPut[i][j] = smaller
                
                print("Proceso 2:")
                print( outPut )
                print( "\nSe ha procesado el archivo\n" )

                archOutRute = "/media/greem/Documentos/escuela/clases/programacion de computadoras/proyectoFinal_EyPC/auxArchives/translated.txt"
                with open( archOutRute, 'w' ) as outPutArch:
                    
                    for line in outPut:
                        for word in line:
                            outPutArch.write( word )
                
            case "alreadyTranslated":
                print( "ya se tradujo" )

            case "saveTranslated":
                print( "guardar traducido" )


""" creación de objetos """
prArch = processArchive( "Pesudo-NASM" )