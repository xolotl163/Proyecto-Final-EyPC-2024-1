
#clase base, solo se crea para herencia, nada más
class Observator:

    def __init__(self):
        pass

    def update( self ):
        pass

#objetos que se van a poder monitorear de forma libre
class ObservableSubject:

    def __init__(self ):
        #se deja sin nada para poder sobreescribirse por las clases derivadas
        pass

    def addObservator(self, newObr):
        self.observators.append( newObr )

    def rmvObservator( self, obr ):
        self.observators.remove( obr )

    def notifyObs( self, message, archiveRuteIn, archiveRuteOut ):
        for ob in self.observators:
            ob.update(message, archiveRuteIn, archiveRuteOut)
