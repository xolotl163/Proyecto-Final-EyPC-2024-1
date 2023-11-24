
import dataStructures.generalUse1 as generalUses
import GUI.interfaz as GUI
import dataStructures.observatorPattern as Obs
import dataStructures.processArchive as PrArch

#sección de creacion e inicialización de objetos generales al programa
flags = generalUses.Flags
registers = generalUses.Registers
instructions = generalUses.Instructions

userInterface = GUI.UserInterface
concreteObservator = PrArch.prArch 

#seccion de funciones para el programa
def main():

    userInterface.addObservator( concreteObservator )
    userInterface.mainLoop()

    pass

main()