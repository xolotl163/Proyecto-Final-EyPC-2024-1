
import os
from . import generalUse1 as generalUses
from . import observatorPattern as Obs
from . import decimal_a_binario as binaryConvert

""" definicion e inicializacion de variables y objetos necesarios para el programa """
flags = generalUses.Flags
registers = generalUses.Registers
instructions = generalUses.Instructions
operations = generalUses.Operations0

""" definicion de clases """
class processArchive( Obs.Observator ):

    def __init__(self, name):
        self.name = name

    def update(self, type, archiveRuteIn, archiveRuteOut):
        
        match type:
            
            case "saveTranslated":

                with open( archiveRuteIn, 'r' ) as file:
                    content = file.readlines()
                    #print("Entrada: ")
                    #print( content )
                    
                a = len( content ) - 1 #indice de la ultima linea
                print( a )              
                content[a] = content[a] + '\n'

                
                actualWord = []
                outPut = []
                translatedLine = []

                for i in range( len(content)):
                    line = content[i]
                    #print( "line: "+str(line) )
                    
                    if line == "\n":
                        continue
                    else:

                        for j in range( len(line)):

                            if line[j] == " " or line[j] == "\n":

                                actualWord = "".join( actualWord )

                                if actualWord not in instructions.getDictionary( "binary" ):
                                    actualWord = str( binaryConvert.decimal_a_binario( int(actualWord) ) )
                                    translatedLine.append( actualWord )

                                else:
                                    translatedLine.append( instructions.getElement( "binary", actualWord ) )
                                    
                                actualWord = []

                            else:
                                actualWord.append( line[j] )

                    outPut.append( translatedLine )
                    translatedLine = []

                #print( "\n\nProceso 1: " )
                #print( outPut )

                ref1Arg = "000000000000000000"
                ref2Arg = "000000000"

                print( "\nlen output: "+str( len( outPut ) ) )
                for i in range( len(outPut)):
                    sizeLine = len( outPut[i] )

                    match sizeLine:

                        case 2: #la instruccion tiene 1 argumento
                            outPut[i][1] = operations.fillGaps( ref1Arg, outPut[i][1] )
                        
                        case 3: #la instruccion tiene 2 argumentos
                            outPut[i][1] = operations.fillGaps( ref2Arg, outPut[i][1] )
                            outPut[i][2] = operations.fillGaps( ref2Arg, outPut[i][2] )

                #print("Proceso 2:")
                #print( outPut )
                print( "\nSe ha procesado el archivo\n" )
                
                with open( archiveRuteOut, 'w' ) as outPutArch:   
                    for line in outPut:

                        k = len( line )
                        line[ k-1 ] = line[k-1] + "\n"
                        
                        for word in line:
                            outPutArch.write( word )
                            
            case "load_leftArchive":
                print( "ya se tradujo" )

            case "load_rightArchive":
                print( "guardar traducido" )


""" creación de objetos """
prArch = processArchive( "Pesudo-NASM" )