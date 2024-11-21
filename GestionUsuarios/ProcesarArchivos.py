import threading
import time

# Clase que hereda de Thread para procesar archivos
class ProcesadorArchivo(threading.Thread):
    def __init__(self, nombre_archivo, num_lineas):
        super().__init__()
        self.nombre_archivo = nombre_archivo
        self.num_lineas = num_lineas

    def run(self):
        """Simula el procesamiento de cada línea del archivo"""
        for i in range(1, self.num_lineas + 1):
            # Simular tiempo de procesamiento
            time.sleep(0.1)
            print(f"{self.nombre_archivo} - Procesando línea {i}")
        print(f"{self.nombre_archivo} - Procesamiento completado.")

# Lista de archivos y sus líneas a procesar
archivos = [
    ("archivo1.txt", 5),
    ("archivo2.txt", 3),
    ("archivo3.txt", 4),
    ("archivo4.txt", 2)
]

# Crear e iniciar hilos
hilos = []
for nombre_archivo, num_lineas in archivos:
    hilo = ProcesadorArchivo(nombre_archivo, num_lineas)
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("Todos los archivos han sido procesados.")
