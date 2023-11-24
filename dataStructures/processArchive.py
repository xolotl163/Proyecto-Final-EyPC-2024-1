
from . import observatorPattern as Obs

""" definicion de clases """
class processArchive( Obs.Observator ):

    def __init__(self, name):
        self.name = name

    def update(self):

        print( "\nSe ha procesado el archivo" )

        pass

""" creación de objetos """

prArch = processArchive( "Pesudo-NASM" )