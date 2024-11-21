import threading

# Clase para gestionar las sesiones de usuario
class SesionUsuario:
    # Mi clase necestira un solo atributo que sera de tipo threating.local
    def __init__(self, datos_sesion):
        self.datos_sesion = datos_sesion

    # Asocion un nombre a mi hilo local
    def iniciar_sesion(self, nombre_usuario):
        self.datos_sesion.nombre_usuario = nombre_usuario

    # Muestra el nombre del hilo local
    def mostrar_sesion(self):
        try:
            print(f"Hilo {threading.current_thread().name}: Usuario actual -> {self.datos_sesion.nombre_usuario}")
        except AttributeError:
            print(f"Hilo {threading.current_thread().name}: No hay ningún usuario en sesión.")

# Objeto threading.local para almacenamiento local de hilo
datos_sesion = threading.local()


def gestionar_sesion(nombre_usuario):
    # Inicialiazamos una SesionUsuario con el objeto threating.local
    sesion = SesionUsuario(datos_sesion)
    # Pasamos el parametro que se almacenara en el objeto como define este metodo de la clase SesionUsuario
    sesion.iniciar_sesion(nombre_usuario)
    # Imprimimos la informacion
    sesion.mostrar_sesion()


if __name__ == "__main__":
    # Lista de nombres de usuarios para las sesiones
    usuarios = ["Polo", "Pepe", "Paco", "Pepito"]

    # Como en el ejercicio anterior, inicializamos los hilos pasando el metodo target y los datos que quermos almacenar
    hilos = []
    for usuario in usuarios:
        hilo = threading.Thread(target=gestionar_sesion, args=(usuario,))
        # Guardamos el hilo en una lista
        hilos.append(hilo)
        # Inicializamos el hilo
        hilo.start()

    # Hacemos un join para que el programa finalice cuando todos los hilos hayan acabado su tarea
    for hilo in hilos:
        hilo.join()
