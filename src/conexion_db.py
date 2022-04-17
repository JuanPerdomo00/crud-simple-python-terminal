#!/usr/bin/python3

import sqlite3

# conexion a la base de datos
# nombre de la base de datos que se creo en sqlbrowser
database = "../crud.db"

# clase para manejar la conexion
class DB:
    # metode para ejecutar
    def ejecutar_consulta(self, consulta, parametros = ()):
        # with ejecuta y me destrulle la variable cuando la ejecute
        with sqlite3.connect(database) as con:
            self.cursor = con.cursor()
            resultado = self.cursor.execute(consulta, parametros)
            con.commit()
            return resultado
