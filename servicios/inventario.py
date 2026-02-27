import json
import os
from modelos.producto import Producto

# Gestiona los productos usando un diccionario para búsquedas rápidas (O(1)).
class Inventario:

    # Inicializa el inventario y carga datos del archivo JSON.
    def __init__(self, archivo_datos="inventario.json"):
        self.archivo_datos = archivo_datos
        self.productos = {} 
        self.cargar_desde_archivo()

    # Añade un producto si su ID no existe y guarda los cambios.
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("⚠️ Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()
            print("✅ Producto añadido exitosamente.")

    # Elimina un producto por su ID y actualiza el archivo.
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("🗑️ Producto eliminado exitosamente.")
        else:
            print("❌ Error: Producto no encontrado.")

    # Actualiza cantidad y/o precio de un producto existente.
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            self.guardar_en_archivo()
            print("🔄 Producto actualizado exitosamente.")
        else:
            print("❌ Error: Producto no encontrado.")

    # Busca y muestra productos que coincidan parcialmente con el nombre.
    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            print("🔍 Resultados de la búsqueda:")
            for p in encontrados:
                print(p)
        else:
            print("🤷‍♂️ No se encontraron productos con ese nombre.")

    # Muestra todos los productos almacenados en el inventario.
    def mostrar_todos(self):
        if not self.productos:
            print("📭 El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    # Guarda el diccionario de productos en un archivo JSON.
    def guardar_en_archivo(self):
        datos = {id_prod: prod.to_dict() for id_prod, prod in self.productos.items()}
        with open(self.archivo_datos, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

    # Carga los productos desde el archivo JSON al iniciar.
    def cargar_desde_archivo(self):
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r') as archivo:
                    datos = json.load(archivo)
                    for id_prod, prod_data in datos.items():
                        self.productos[id_prod] = Producto(
                            prod_data["id_producto"],
                            prod_data["nombre"],
                            prod_data["cantidad"],
                            prod_data["precio"]
                        )
            except json.JSONDecodeError:
                print("⚠️ El archivo de inventario está corrupto o vacío. Se iniciará un inventario nuevo.")