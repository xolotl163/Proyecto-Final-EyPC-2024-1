
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
                        content.remove( line )
                    else:
                        for letter in line:
                            if letter == "\n": #termina la linea
                                continue
                            elif letter == " ":
                                translatedLine.append( instructions.getElement( "binary", "".join(actualWord) ) )
                                actualWord = []
                            else:
                                actualWord.append( letter )

                    outPut.append( str( translatedLine ) )
                    actualWord = []
                    translatedLine = []

                print( "salida" )
                print( outPut )
                print( "\nSe ha procesado el archivo" )

            case "alreadyTranslated":
                print( "ya se tradujo" )

            case "saveTranslated":
                print( "guardar traducido" )


""" creación de objetos """
prArch = processArchive( "Pesudo-NASM" )