import time
from os import system  # Importamos el módulo 'os' para usar comandos del sistema, como 'Pause' en Windows.
import subprocess  # Importamos 'subprocess' para ejecutar programas y comandos del sistema operativo.
import asyncio  # Importamos 'asyncio' para trabajar con programación asíncrona en Python.


# Función que ejecuta el Bloc de notas de forma síncrona
def showNotepad1():
    try:
        # Utilizamos subprocess.run para ejecutar 'Notepad.exe'. Esto es una llamada síncrona, por lo que bloquea el programa hasta que Notepad se cierre.
        subprocess.run(['Notepad.exe', ])
    except subprocess.CalledProcessError as e:
        # Capturamos cualquier excepción que ocurra si el comando falla y mostramos el error.
        print(e.output)


# Función asíncrona que ejecuta el Bloc de notas
async def showNotepad2():
    try:
        # Usamos 'asyncio.create_subprocess_exec' para ejecutar 'notepad.exe' de forma asíncrona.
        # Al ser una llamada asíncrona, el programa principal continúa ejecutándose sin esperar a que Notepad se cierre.
        await asyncio.create_subprocess_exec('notepad.exe')
    except subprocess.CalledProcessError as e:
        # Capturamos cualquier excepción que ocurra si el comando falla y mostramos el error.
        print(e.output)


# Función principal asíncrona
async def main():
    inicio = time.time()
    fin = 0
    eleccion = input("Seleccione opcion\n 1:ejecucion sincrona\n 2:ejecucion asincrona")
    if(eleccion== "1"):
        print("inicio llamada síncrona")
        showNotepad1()  # Llamada a la función síncrona para ejecutar el Bloc de notas. Bloqueará el programa hasta que se cierre.
        print("fin llamada síncrona")
        fin = time.time()
        print(fin-inicio, "segundos")
    elif(eleccion== "2"):
        print("inicio llamada asíncrona")
        await showNotepad2()  # Llamada a la función asíncrona para ejecutar el Bloc de notas. No bloqueará el programa principal.
        print("fin llamada asíncrona")

        # Mensaje para que el usuario presione una tecla antes de finalizar el programa.
        print("pulsa una tecla para terminar")
        system('Pause')  # Pausamos la ejecución del programa, esperando que el usuario presione una tecla.
        fin = time.time()
        print(fin - inicio, "segundos")
    else:
        print("Opcion no valida")


# Ejecutamos la función principal asíncrona con 'asyncio.run'
asyncio.run(main())