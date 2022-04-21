#!/usr/bin/python3
# _*_ coding: utf-8 -*-
# author: jakepy

# Modulos
from colorama import Fore
import conexion_db as con
import platform
import os
import time
import sqlite3


# establecemos la coneccion con la base de datos sqllite
db = con.DB()


class Color:
    off = Fore.RESET
    v = Fore.GREEN
    r = Fore.RED
    m = Fore.MAGENTA
    y = Fore.YELLOW
    b = Fore.BLUE


# limpia la pantalla de la terminal
def clear_pant():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")


def banner():
    clear_pant()
    print(f"{Color.v}={Color.off}"*20)
    print(f"{Color.r}[*]  {Color.m}CRUD Python {Color.r}[*]{Color.off}")
    print(f"{Color.v}={Color.off}"*20)


def continuar():
    try:
        continuar = str(input(f"\n{Color.r}[!] {Color.v}volver al menu? Si[s] o No[n]: {Color.off}")).lower()
        if continuar == "s" or "si" and continuar != "":
            banner()
            menu()
            opcion()

        elif continuar == "n" or "no" and continuar != "":
            banner()
            print(f"{Color.y}[*] Gracias Por usar el programa {Color.r}:){Color.off}")
            exit(0)

        else:
            clear_pant()
            banner()
            print(f"\n{Color.r}[!] Error... Ingrese un valor{Color.off}\n")
            exit(1)

    except KeyboardInterrupt:
        banner()
        print(f"\n{Color.r}[!] saliendo forzado{Color.off}\n")
        exit(1)
    
    except ValueError:
        print(f"{Color.r}[!] Error ingrese una opcion{Color.off}")
        continuar()

################################################################################
# Funciones para padir a la base de datos
def create():
    try:
        nombre: str = str(input(f"{Color.y}[+] {Color.v}Ingrese el Nombre: {Color.off}"))
        email: str = str(input(f"{Color.y}[+] {Color.v}Ingrese el email: {Color.off}"))
        if len(nombre) > 0 and len(email) > 0:
            # insertar los datos
            # ejecuta la consulta y la guarda 
            sql: str = "INSERT INTO campos(nombre, email) VALUES(?, ?)"
            parametros: str = (nombre, email)
            db.ejecutar_consulta(sql, parametros)
            clear_pant()
            banner()
            print(f"\n{Color.v}[*] Guardados.. {Color.m}:){Color.off}\n")
            continuar()

        else:
            banner()
            print(f"\n{Color.r}[!] Ingrese Datos Validos{Color.off}\n")
            exit(1)

    except KeyboardInterrupt:
        clear_pant()
        banner()
        print(f"{Color.r}\n[!] Salio forzado !!!...{Color.off}\n")
        exit(1)


def read():
    sql: str = db.ejecutar_consulta("SELECT * FROM campos")
    for data in sql:
        print(f"""
        {Color.y}ID: {Color.v}{data[0]}{Color.off}
        {Color.y}Nombre: {Color.v}{data[1]}{Color.off}
        {Color.y}Email: {Color.v}{data[2]}{Color.off}
        """)


def update():
    try:
        id: int = int(input(f"{Color.y}[+] {Color.v}Ingrese el ID a actualizar: {Color.off}"))
        nombre: str = str(input(f"{Color.y}[+] {Color.v}Ingrese el nuevo Nombre: {Color.off}"))
        email: str = str(input(f"{Color.y}[+] {Color.v}Ingrese el nuevo email: {Color.off}"))
        if id != "":
            sql:str = "UPDATE campos SET nombre=?, email=? WHERE id=?"
            parametros = (nombre, email, id)
            db.ejecutar_consulta(sql, parametros)
            clear_pant()
            banner()
            print(f"{Color.y}[*] {Color.v}Actualizados {Color.m}:){Color.off}")
            continuar()
    
    except ValueError:
        clear_pant()
        banner()
        print(f"\n{Color.r}[!] Error Interno...{Color.off}\n")
        exit(1)

    except  KeyboardInterrupt:
        clear_pant()
        banner()
        print(f"\n{Color.r}[!] Error salio forzado{Color.off}\n")


def delete():
    try:
        id: int = int(input(f"{Color.y}[+] {Color.v}Ingrese el ID a borrarr: {Color.off}"))
        if id != "":
            sql = "DELETE FROM campos WHERE id=?"
            parametros = (id,)
            db.ejecutar_consulta(sql, parametros)
            print(f"{Color.y}[!] {Color.v}Eliminado{Color.b}.{Color.r}.{Color.m}.{Color.off}")
            continuar()
    
    except KeyboardInterrupt:
        banner()
        print(f"{Color.r}[!] saliendo forzado {Color.off}")
        exit(1)

    except ValueError:
        banner()
        print(f"{Color.r}[!] Error Ingrese el numero del ID{Color.off}\n")
        continuar()
    

def buscar():
    try:
        nombre: str = str(input(f"{Color.y}[+] {Color.v}Ingrese el Nombre a Buscar: {Color.off}"))
        if len(nombre) > 0:
            sql = "SELECT * FROM campos WHERE nombre LIKE ?"
            parametros = (f"%{nombre}%")
            res = db.ejecutar_consulta(sql, parametros)
            for data in res:
                print(f"""
                {Color.y}[{Color.b}+{Color.y}] ID: {Color.v}{data[0]}{Color.off}
                {Color.y}[{Color.b}+{Color.y}] Nombre {Color.v}{data[1]}{Color.off}
                {Color.y}[{Color.b}+{Color.y}] Email {Color.v}{data[2]}{Color.off}
                """)

    except KeyboardInterrupt:
        print(f"{Color.r}[!] Salio Forzado...{Color.off}")
        exit(1)

    except sqlite3.ProgrammingError:
        clear_pant()
        banner()
        print(f"\n{Color.r}[!] El nombre no existe{Color.off}")
        continuar()
################################################################################


def menu():
    banner()
    print(f"""
{Color.m}1. {Color.v}Agregar Registro{Color.off}
{Color.m}2. {Color.v}Listar Registro{Color.off}
{Color.m}3. {Color.v}Actualizar Registro{Color.off}
{Color.m}4. {Color.v}Borrar Registro{Color.off}
{Color.m}5. {Color.v}Buscar{Color.off}
{Color.m}6. {Color.v}Salir del programa
        {Color.off}""")
    try:
        menu: int = int(input(f"{Color.b}[{Color.r}*{Color.b}] Seleccione una opcion: {Color.off}"))
        return menu
        
    except KeyboardInterrupt:
        clear_pant()
        banner()
        print(f"\n\n{Color.r}[!] Salio Forzado...{Color.off}\n")
        exit(1)

    except ValueError:
        clear_pant()
        banner()
        print(f"\n{Color.r}[!] Error Interno...{Color.off}\n")
        exit(1)


def opcion():
    n = menu()
    # menu del programa
    while menu != 6:  
        try:
            if n == 1:
                banner()
                create()
                time.sleep(1.5)
                banner()
                continuar()
                break

            elif n == 2:
                banner()
                read()
                time.sleep(2)
                banner()
                continuar()
                break

            elif n == 3:
                banner()
                update()
                time.sleep(1.5)
                banner()
                continuar()
                break

            elif n == 4:
                banner()
                delete()
                time.sleep(1.5)
                banner()
                continuar()
                break

            elif n == 5:
                banner()
                buscar()
                time.sleep(1.5)
                banner() 
                continuar()
                break

            elif n == 6:
                banner()
                print(f"\n{Color.r}[!] {Color.r}B{Color.y}y{Color.b}e{Color.m}.{Color.y}.{Color.b}.\n{Color.off}")
                break

            else:
                clear_pant()
                banner()
                print(f"\n{Color.r}[!] Error Ingrese un numero valido{Color.off}\n")
                exit(1)
                
        except  KeyboardInterrupt as e:
            print(f"{Color.r}[!] Salio Forzado...{Color.off}", e)
            exit(1)


def main():
    opcion()


if __name__ == "__main__":
    main()