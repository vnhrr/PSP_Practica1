import threading
import time

# Funcion que ejecutara cada hilo
# recibe como parametro obligatorio el usuario y el resto es optativo
def procesar_ususario(ususario, **kwargs):
    # Extraemos los valores del diccionario pasado como parametro
    nombre = kwargs.get('nombre','Desconocido')
    edad = kwargs.get('edad','No especificada')
    # Indica que el hilo ha comenzado
    print(f"[Hilo-{threading.current_thread().name}] Procesando Usuario ID: {usuario_id}...")
    time.sleep(1)
    # f al principio indica que es un f-string, que permite hacer uso de variables dentro de la cadena
    # Lo entre comillado es parte de la cadena, lo que de encuentra entre {} son las variables
    print(f"[Hilo-{threading.current_thread().name}] Usuario ID: {ususario}, Nombre: {nombre}, Edad: {edad}")

usuarios = [
    (1, {'nombre': 'Ivan', 'edad': 25}),
    (2, {'nombre': 'Juan', 'edad': 35}),
    (3, {'nombre': 'Oscar', 'edad': 73}),
    (4, {'nombre': 'Pepe', 'edad': 22}),
    (5, {'nombre': 'Fran', 'edad': 5}),
    ]

# Lista que almacenara los hilos creados
hilos=[]

for usuario in usuarios:
    # Extraemos la informacion de cada usuario
    usuario_id, info = usuario
    # Creamos el hilo, dandole la funcion a ejecutar y los parametros
    hilo = threading.Thread(target=procesar_ususario, args=(usuario_id,),
                            kwargs=info)
    # Damos un nombre al hilo
    hilo.name = f"Usuario--{usuario_id}"
    # Iniciamos el hilo y lo añadimos a nuestra lista de hilos
    hilo.start()
    hilos.append(hilo)

# Hacemos que el programa espere a la finalizacion de todos los hilos
for hilo in hilos:
    hilo.join()
print('Todos los hilos han finalizado')