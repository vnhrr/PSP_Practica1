import psutil
import asyncio

#ni idea de como hacer esto

async def programa():
    print("Pulse cualquier tecla para iniciar.")
    print("Igualmente pulse cualquier tecla para salir")
    inic = False
    pararPrograma(input())
    await asyncio.coroutine
    obtenerProcesos(inic)

def pararPrograma(tecla : str):
    if tecla != "":
        return False
    else:
        return True

def obtenerProcesos(inic : bool):
    while inic:
        for proce in psutil.process_iter(["pid", "name"]):
            print(proce.info, "\t", proce.cpu_percent(), "\t", proce.memory_percent())







