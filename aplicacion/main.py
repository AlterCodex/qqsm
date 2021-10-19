import random

from dominio.categorias import categorias
from dominio.juego import Juego
from dominio.pregunta import Pregunta
from dominio.questionario import Questionario
from dominio.usuario import Usuario
from infraestructura.json_persistence import jsonPersistence as saver
from infraestructura.user_persistence import PersistenciaUsuario

if __name__ == '__main__':
    questionario = saver.load_json('599778c7-eb3b-4c90-97a8-6a7cbc0368c4.json')
    user_name = input('ingrese el usuario:')
    db= PersistenciaUsuario()
    db.connect()
    usuario= db.obtener_usuario(user_name)
    if usuario is None:
        usuario= Usuario(user_name)
        db.guardar_usuario(usuario)
    else:
        resp=input('Quiere ver los ultimos juegos de '
              f'{usuario.nombre} (Y/N)?')[0]
        if resp=='Y':
            juegos= db.obtener_juegos(usuario)
            for j in juegos:
                print(j)

    juego = Juego(usuario,questionario)
    for p in questionario.preguntas:
        print(usuario)
        print(p)
        opcion=input("ingrese la opcion deseada:")
        if not p.validar_opcion(opcion):
            print('Perdio')
            db.guardar_juego(juego)
            break
        else:
            juego.incrementar_puntaje(1)
    else:
        db.guardar_juego(juego)
        print("gano")



def generateRandom():
    questionary = Questionario()
    for i in range(1,11):
        print(f'creando pregunta{i}')
        respuestas = [
                f'Respuesta {i},1',
                f'Respuesta {i},2',
                f'Respuesta {i},3',
                f'Respuesta {i},4',
            ]
        p= Pregunta(
            f'Texto {i}',
            respuestas ,
            respuestas [3],
            i,
            random.choice(categorias)
        )
        questionary.add(p)
    saver.save_json(questionary)