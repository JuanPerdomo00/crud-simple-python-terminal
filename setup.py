import platform
import os
import time


def clear():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")

def banner():
    print("*"*50)
    print("[*] Instaladore de dependencias by: jakepy [*]")
    print("*"*50)

def install_dependencies():
    clear()
    banner()
    try:
        import colorama
        print("\n[*] Modulos Instalados...")
        exit(0)

    except ImportError:
        print("[!] Modulos no instalados...")
        time.sleep(1)
        print("[!] Instalandos modulos colorama")
        time.sleep(1)
        os.system("pip3 install -r requirements.txt")
        print("\n[!] Instalandos...")
        exit(0)


if __name__ == "__main__":
    install_dependencies()

