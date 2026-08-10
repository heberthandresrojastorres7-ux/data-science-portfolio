# ============================================
#  AGENDA DE CONTACTOS CLI
#  Autor: Heberth Rojas
# ============================================

import json
import os

ARCHIVO = "contactos.json"

# --------------------------------------------
# FUNCION 1: Cargar contactos desde JSON
# --------------------------------------------
def cargar_contactos():
    #Si existe el archivo, lo lee. Si no, empieza con lista vacía.#
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

# --------------------------------------------
# FUNCION 2: Guardar contactos en JSON
# --------------------------------------------
def guardar_contactos(contactos):
    #Guarda la lista de contactos en el archivo JSON.#
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(contactos, f, indent=2, ensure_ascii=False)

# --------------------------------------------
# FUNCION 3: Agregar contacto
# --------------------------------------------
def agregar_contacto(contactos):
    #Pide nombre, telefono y email, y lo agrega a la lista.#
    print("\n📇 Agregar nuevo contacto")
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    
    # Creamos un diccionario con los datos
    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    
    contactos.append(contacto)
    guardar_contactos(contactos)
    print(f"✅ Contacto '{nombre}' guardado.")

# --------------------------------------------
# FUNCION 4: Listar contactos
# --------------------------------------------
def listar_contactos(contactos):
    #Muestra todos los contactos numerados.#
    if not contactos:
        print("\n📭 No hay contactos guardados.")
        return
    
    print("\n📋 Lista de contactos:")
    print("-" * 40)
    for i, c in enumerate(contactos, start=1):
        print(f"{i}. {c['nombre']} | {c['telefono']} | {c['email']}")
    print("-" * 40)

# --------------------------------------------
# FUNCION 5: Buscar contacto (TU RETO)
# --------------------------------------------
def buscar_contacto(contactos):
    print("\n🔍 Buscar contacto")
    buscar = input("Nombre: ").strip()
    
    resultados = []
    for c in contactos:
        nombre_contacto = c['nombre'].lower()
        nombre_busqueda = buscar.lower()
        
        if nombre_busqueda in nombre_contacto:
            resultados.append(c)
    
    if not resultados:
        print("❌ No encontrado.")
        return
    
    print(f"✅ Encontrados: {len(resultados)}")
    for c in resultados:
        print(f"  {c['nombre']} | {c['telefono']}")

# --------------------------------------------
# FUNCION 6: Borrar contacto (TU RETO)
# --------------------------------------------
def borrar_contacto(contactos):
    print("\n🗑️ Borrar contacto")
    listar_contactos(contactos)
    numero = input("numero a borrar: ").strip()
    indice = int(numero) - 1
    contactos.pop(indice)
    guardar_contactos(contactos)
    print(f"✅ Contacto borrado.")
# --------------------------------------------
# FUNCION PRINCIPAL: Menu
# --------------------------------------------
def menu():
    #Bucle infinito que muestra el menu hasta que el usuario salga.#
    contactos = cargar_contactos()
    
    while True:
        print("\n" + "=" * 40)
        print("📇 AGENDA DE CONTACTOS")
        print("=" * 40)
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar todos")
        print("4. Borrar contacto")
        print("5. Salir")
        print("-" * 40)
        
        opcion = input("Elige una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            buscar_contacto(contactos)
        elif opcion == "3":
            listar_contactos(contactos)
        elif opcion == "4":
            borrar_contacto(contactos)
        elif opcion == "5":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("\n⚠️ Opción no válida. Intenta de nuevo.")

# --------------------------------------------
# PUNTO DE ENTRADA
# --------------------------------------------
if __name__ == "__main__":
    menu()