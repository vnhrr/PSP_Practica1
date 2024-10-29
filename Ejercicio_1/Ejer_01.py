import psutil

# Creo una varibale booleana para usarlo mas adelante con el notepad
abierto = False

# bucle que me almacena todos los procesos en ejecucion en una lista clave valor
# dentro tengo un if que cambia a true el booleano si encuentra un proceso con el nombre notepad.exe
for proce in psutil.process_iter(["pid", "name"]) :
    if proce.name().lower().__eq__("notepad.exe"):
        abierto = True
        print(proce.info)


if abierto :
    print("El bloc de notas esta abierto")