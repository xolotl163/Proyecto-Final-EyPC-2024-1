
import dataStructures.generalUse1 as generalUses

#sección de creacion e inicialización de variables globales

flags = generalUses.Flags
registers = generalUses.Registers
instructions = generalUses.Instructions

def main():

    print( instructions.getDictionary()['and'] )
    print( flags.getDictionary()['ZF'] )
    pass
main()