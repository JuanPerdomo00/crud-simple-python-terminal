#!/usr/bin/python3
# _*_ coding: utf-8 -*-
# author: jakepy

# Modulos
from colorama import Fore
import conexion_db as con
import platform
import os
import time

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

################################################################################
# Funciones para padir a la base de datos
def create():
    try:
        nombre: str = str(input("[+] Ingrese el Nombre: "))
        email: str = str(input("[+] Ingrese el email: "))
        if len(nombre) > 0 and len(email) > 0:
            # insertar los datos
            # ejecuta la consulta y la guarda 
            sql: str = "INSERT INTO campos(nombre, email) VALUES(?, ?)"
            parametros: str = (nombre, email)
            db.ejecutar_consulta(sql, parametros)
            print(f"{Color.v}[*] Guardados.. :){Color.off}")
        else:
            print("[!] Ingrese Datos Validos")
            exit()

    except KeyboardInterrupt:
        clear_pant()
        banner()
        print(f"{Color.r}\n[!] Salio forzado !!!...{Color.off}\n")
        exit(1)


def read():
    sql: str = db.ejecutar_consulta("SELECT * FROM campos")
    for data in sql:
        print(f"""
        ID: {data[0]}
        Nombre: {data[1]}
        Email: {data[2]}
        """)


def update():
    try:
        id: int = int(input("[+] Ingrese el ID a actualizar: "))
        nombre: str = str(input("[+] Ingrese el nuevo Nombre: "))
        email: str = str(input("[+] Ingrese el nuevo email: "))
        if id != "":
            sql:str = "UPDATE campos SET nombre=?, email=? WHERE id=?"
            parametros = (nombre, email, id)
            db.ejecutar_consulta(sql, parametros)
            print("[*] Actualizados :)")
    
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
        id: int = int(input("[+] Ingrese el ID a borrarr: "))
        if id != "":
            sql = "DELETE FROM campos WHERE id=?"
            parametros = (id,)
            db.ejecutar_consulta(sql, parametros)
            print("[!] Eliminado...")
    
    except KeyboardInterrupt:
        banner()
        print(f"{Color.r}[!] saliendo forzado {Color.off}")
        exit(1)

    except ValueError:
        banner()
        print(f"{Color.r}[!] Error Ingrese el numero del ID{Color.off}\n")
        continuar()


def buscar():
    nombre: str = str(input("[+] Ingrese el Nombre a Buscar: "))
    if len(nombre) > 0:
        sql = "SELECT * FROM campos WHERE nombre LIKE ?"
        parametros = (f"%{nombre}%")
        res = db.ejecutar_consulta(sql, parametros)
        for data in res:
            print(f"""
            [+] ID: {data[0]}
            [+] Nombre {data[1]}
            [+] Email {data[2]}
            """)
################################################################################


def continuar():
    continuar = str(input(f"\n{Color.r}[!] {Color.v}volver al menu? Si[s] o No[n]: {Color.off}")).lower()
    if continuar == "s" or "si":
        banner()
        menu()
        opcion()
    elif continuar == "n" or "no":
        banner()
        print(f"{Color.y}[*] Gracias Por usar el programa {Color.r}:){Color.off}")
        exit(0)
    else:
        print(f"{Color.r}[!]Error...{Color.off}")
        exit(1)


def menu():
    banner()
    print(f"""{Color.y}
1. Agregar Registro
2. Listar Registro
3. Actualizar Registro
4. Borrar Registro
5. Buscar
6. Salir del programa
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


def opcion():
    n = menu()
    # menu del programa
    while menu != 6:  
        try:
            if n == 1:
                banner()
                create()
                time.sleep(1.5)
                clear_pant()
                banner()
                continuar()
                break

            elif n == 2:
                banner()
                read()
                break

            elif n == 3:
                banner()
                update()
                break

            elif n == 4:
                banner()
                delete()
                break

            elif n == 5:
                banner()
                buscar()
                break

            elif n == 6:
                banner()
                print(f"\n{Color.v}[!] Bye...\n{Color.off}")
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
