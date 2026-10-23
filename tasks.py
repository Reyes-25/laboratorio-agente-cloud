def agregar_tarea(tareas, titulo, categoria="General"):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("El titulo es obligatorio")
    categoria = categoria.strip()
    if not categoria:
        raise ValueError("La categoria es obligatoria")
    tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "categoria": categoria,
        "completada": False,
    }
    tareas.append(tarea)
    return tarea

def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea
    raise ValueError("Tarea no encontrada")

def eliminar_tarea(tareas, tarea_id):
    for indice, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            del tareas[indice]
            return tarea
    raise ValueError("Tarea no encontrada")

def pendientes(tareas, categoria=None):
    tareas_pendientes = [t for t in tareas if not t["completada"]]
    if categoria is not None:
        categoria = categoria.strip().casefold()
        return [
            tarea
            for tarea in tareas_pendientes
            if tarea["categoria"].casefold() == categoria
        ]
    return tareas_pendientes
