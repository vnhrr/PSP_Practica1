import os

# Función para contar líneas y palabras en el contenido recibido
def contar_lineas_y_palabras(texto):
    lineas = texto.count('\n') + 1 if texto else 0
    palabras = len(texto.split())
    return lineas, palabras

# Creamos un pipe para la comunicación entre padre e hijo
padre_a_hijo, hijo_a_padre = os.pipe(), os.pipe()  # Pipe bidireccional

# Fork para crear el proceso hijo
pid = os.fork()

if pid > 0:
    # Proceso padre
    os.close(padre_a_hijo[0])  # Cierra el extremo de lectura del pipe de padre a hijo
    os.close(hijo_a_padre[1])  # Cierra el extremo de escritura del pipe de hijo a padre

    # **Parte 1: Envío de mensaje y respuesta en mayúsculas**
    mensaje = "Hola desde el proceso padre"
    os.write(padre_a_hijo[1], mensaje.encode())  # Envía mensaje al hijo
    respuesta = os.read(hijo_a_padre[0], 1024)  # Lee respuesta del hijo
    print("Padre recibió del hijo:", respuesta.decode())  # Muestra la respuesta del hijo

    # **Parte 2: Envío de archivo y conteo de líneas y palabras**
    # Enviamos el contenido de un archivo al hijo
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
        os.write(padre_a_hijo[1], contenido.encode())  # Envía contenido del archivo al hijo

    # Recibe los resultados del conteo de líneas y palabras del hijo
    conteo = os.read(hijo_a_padre[0], 1024)
    lineas, palabras = conteo.decode().split(',')
    print(f"Padre recibió del hijo: Líneas={lineas}, Palabras={palabras}")

    os.close(padre_a_hijo[1])
    os.close(hijo_a_padre[0])

else:
    # Proceso hijo
    os.close(padre_a_hijo[1])  # Cierra el extremo de escritura del pipe de padre a hijo
    os.close(hijo_a_padre[0])  # Cierra el extremo de lectura del pipe de hijo a padre

    # **Parte 1: Recibe mensaje y responde en mayúsculas**
    mensaje_recibido = os.read(padre_a_hijo[0], 1024).decode()
    respuesta = mensaje_recibido.upper()
    os.write(hijo_a_padre[1], respuesta.encode())  # Envía respuesta en mayúsculas al padre

    # **Parte 2: Recibe el contenido del archivo y realiza el conteo**
    contenido_recibido = os.read(padre_a_hijo[0], 1024).decode()
    lineas, palabras = contar_lineas_y_palabras(contenido_recibido)
    conteo = f"{lineas},{palabras}"
    os.write(hijo_a_padre[1], conteo.encode())  # Envía el conteo al padre

    os.close(padre_a_hijo[0])
    os.close(hijo_a_padre[1])
