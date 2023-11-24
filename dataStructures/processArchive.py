
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
                print( "\nSe ha procesado el archivo" )

            case "alreadyTranslated":
                print( "ya se tradujo" )

            case "saveTranslated":
                print( "guardar traducido" )


""" creación de objetos """
prArch = processArchive( "Pesudo-NASM" )