
import GUI.interfaz as GUI
import dataStructures.processArchive as PrArch

#sección de creacion e inicialización de objetos generales al programa
userInterface = GUI.UserInterface
concreteObservator = PrArch.prArch 

#seccion de funciones para el programa
def main():

    userInterface.addObservator( concreteObservator )
    userInterface.mainLoop()

    pass

main()