

class Juego():

    def __init__(self, usuario,questionario):
        self.questionario=questionario
        self.usuario=usuario
        self.puntaje=0

    def incrementar_puntaje(self,puntos):
        self.puntaje+=puntos

    def __str__(self):
        return str(self.usuario)+'--'+str(self.questionario)+'--'+str(self.puntaje)