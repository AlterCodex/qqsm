import sqlite3

from dominio.juego import Juego
from dominio.usuario import Usuario


class PersistenciaUsuario():

    def connect(self):
        self.con = sqlite3.connect("juego.sqlite")
        self.__crear_tabla()


    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE Usuario(user_name text primary key)"
            cursor.execute(query)
            query = "CREATE TABLE Juego(ID INTEGER PRIMARY KEY AUTOINCREMENT,"\
                    "                   user_name text," \
                    "                   questionary_id text," \
                    "                   points int)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_usuario(self,usuario : Usuario):
        cursor = self.con.cursor()
        query = "insert into Usuario(user_name ) values(" \
                f" ?)"
        cursor.execute(query, (usuario.nombre,))
        self.con.commit()

    def obtener_usuario(self,user_name : str):
        cursor = self.con.cursor()
        query = "select *  from Usuario where user_name = " \
                f" ?"
        cursor.execute(query, (user_name,))

        rows = cursor.fetchall()

        for row in rows:
            return Usuario(row[0])
        return None

    def guardar_juego(self,juego : Juego):
        cursor = self.con.cursor()
        query = "insert into Juego(user_name,questionary_id ,points) values(" \
                f" ?,?,?)"
        cursor.execute(query, (juego.usuario.nombre,
                               juego.questionario.uuid,
                               juego.puntaje))
        self.con.commit()

    def obtener_juegos(self,user: Usuario):
        cursor = self.con.cursor()
        query = "select *  from Juego where user_name = " \
                f" ?"
        cursor.execute(query, (user.nombre,))

        rows = cursor.fetchall()
        juegos=[]
        for row in rows:
            j= Juego(
                user,
                row[2]
            )
            j.incrementar_puntaje(row[3])
            juegos.append(j)
        return juegos
