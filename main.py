
import dataStructures.generalUse1 as generalUses
import GUI.interfaz as GUI

#sección de creacion e inicialización de variables globales

flags = generalUses.Flags
registers = generalUses.Registers
instructions = generalUses.Instructions

userInterface = GUI.UserInterface

def main():

    userInterface.mainLoop()

    pass

main()