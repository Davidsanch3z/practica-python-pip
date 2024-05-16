class Task:
    def __init__(self, id, nombre, descripcion, completada=False):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.completada = completada

# Inicializa un contador global para los IDs de las tareas
next_id = 1

def agregar_tarea(nombre, descripcion):
    global next_id  # Usa la variable global para el ID
    nueva_tarea = Task(next_id, nombre, descripcion)
    tareas.append(nueva_tarea)
    print("Tarea agregada con éxito.")
    next_id += 1  # Incrementa el ID para la próxima tarea

def ver_tareas():
    if not tareas:
        print("No hay tareas disponibles.")
        return
    for tarea in tareas:
        print(f"[{tarea.id}] {tarea.nombre} - {tarea.descripcion} - Completada: {tarea.completada}")

def marcar_completada(id_tarea):
    for tarea in tareas:
        if tarea.id == id_tarea:
            tarea.completada = True
            print(f"Tarea '{tarea.nombre}' marcada como completada.")
            return
    print("Error: La tarea especificada no existe.")

def eliminar_tarea(id_tarea):
    global tareas
    tareas = [tarea for tarea in tareas if tarea.id != id_tarea]
    print("Tarea eliminada con éxito.")

tareas = []
while True:
    print("\n--- Menú ---")
    print("1. Agregar Tarea")
    print("2. Ver Tareas")
    print("3. Marcar Tarea como Completada")
    print("4. Eliminar Tarea")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        agregar_tarea(nombre, descripcion)

    elif opcion == "2":
        ver_tareas()

    elif opcion == "3":
        id_tarea = int(input("Ingrese el ID de la tarea a marcar como completada: "))
        marcar_completada(id_tarea)

    elif opcion == "4":
        id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
        eliminar_tarea(id_tarea)

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Error: Opción no válida. Por favor, seleccione una opción válida.")