import random


class Pregunta():

    def __init__(self, texto, respuestas, respuesta_correcta, dificultad,
                 categoria):
        self.letras = ['a', 'b', 'c', 'd']
        self.texto = texto
        self.respuestas = self.mix(respuestas)
        self.respuesta_correcta = respuesta_correcta
        self.dificultad = dificultad
        self.categoria = categoria


    def mix(self, respuestas: []) -> dict:
        opciones = {}
        for letra in self.letras:
            opciones[letra] = random.choice(respuestas)
            respuestas.remove(opciones[letra])
        return opciones

    def validar_opcion(self,opcion):
        return self.is_correcta(
            self.obtener_respuesta(opcion)
        )

    def is_correcta(self,respuesta):
        return respuesta == self.respuesta_correcta

    def obtener_respuesta(self, letra):
        return self.respuestas.get(letra,None)

    def eliminar(self, letra):
        del self.respuestas[letra]

    def __str__(self):
        representacion_str = f'{self.texto}   \n'
        for letra in self.letras:
            if letra in self.respuestas:
                representacion_str += f'{letra}. {self.respuestas[letra]} \n'
        return representacion_str
