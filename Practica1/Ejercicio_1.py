from os import access

# psutil es una librería que permite acceder a información sobre los procesos y recursos del sistema.
import psutil
from psutil import AccessDenied

try:
    # Pedimos el nombre al usuario y añadimos el .exe para evitar errores
    proceso = input("Escribe el nombre del proceso que quieras analizar: ")
    proceso = proceso + ".exe"
    ejecucion = False
    procesosEncontrados = []
    # Bucle de todos los procesos del sistema utilizando psutil.process_iter(), que devuelve un iterador de procesos.
    for proc in psutil.process_iter():
        # Controlamos tambien poner las letras en minusculas para evitar problemas con la busqueda
        if (proceso.lower().__eq__(proc.name().lower())):
            # Obtenemos el nombre del proceso usando proc.name()
            processName = proc.name()
            # El ID del proceso con proc.id
            processID = proc.pid
            # El estado del proceso con proc.status()
            processStatus = proc.status()
            # El porcentaje de memoria usado
            processMem = proc.memory_percent()
            # Imprimimos el nombre del proceso seguido de su PID, el estatus y el uso de memoria.
            print(processName, ' ::: ', processID, processStatus, processMem)
            ejecucion = True
            # Almacenamos los procesos encontrados en una lista
            procesosEncontrados.append(proc)

    # Bucle que comprueba si se ha encontrado el programa, encaso afismativo da la opcion de finalizarlo en caso
    # contrario muestra un mensaje de que no se encontro el programa
    if (ejecucion):
        print("¿Desea finalizar el proceso ", proc.name(), "?", "\n")
        try:
            if input("Pulse S para SI o cualquier tecla para NO".lower()).__eq__("s"):
                # Finalizamos los procesos que teniamos almacenados
                for p in procesosEncontrados:
                    p.kill()
                print("Se finalizo el proceso correctamente")
            else:
                print("El proceso sigue en ejecucion")

        except AccessDenied:
            print("No tienes acceso para realizar esa accion")

    else:
        print("El proceso no se encuentra en ejecucion.")

    # Capturamos cualquier excepción que pueda ocurrir durante la iteración de procesos.
    # Por ejemplo, pueden surgir excepciones si un proceso termina mientras se está obteniendo información,
    # si no tenemos permisos suficientes para acceder a la información del proceso, o si el proceso está en estado zombi.
# except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
except:
    # Si ocurre cualquier error, imprimimos un mensaje de error.
    print("ERROR")
