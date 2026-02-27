from modelos.producto import Producto
from servicios.inventario import Inventario

# Muestra el menú principal y retorna la opción elegida.
def mostrar_menu():
    print("\n" + "="*45)
    print("🏪 SISTEMA AVANZADO DE GESTIÓN DE INVENTARIO 🏪")
    print("="*45)
    print("1️⃣ Añadir nuevo producto ➕")
    print("2️⃣ Eliminar producto ➖")
    print("3️⃣ Actualizar producto 🔄")
    print("4️⃣ Buscar producto por nombre 🔍")
    print("5️⃣ Mostrar todos los productos 📋")
    print("6️⃣ Salir 🚪")
    print("="*45)
    return input("👉 Seleccione una opción: ")

# Función principal que maneja el bucle del programa y las opciones del usuario.
def main():
    inventario = Inventario()

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            print("\n--- ➕ Añadir Producto ---")
            id_prod = input("🆔 Ingrese ID único del producto: ")
            nombre = input("🏷️ Ingrese nombre del producto: ")
            try:
                cantidad = int(input("📊 Ingrese cantidad: "))
                precio = float(input("💲 Ingrese precio: "))
                nuevo_producto = Producto(id_prod, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("❌ Error: La cantidad debe ser un entero y el precio un número.")

        elif opcion == '2':
            print("\n--- ➖ Eliminar Producto ---")
            id_prod = input("🆔 Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == '3':
            print("\n--- 🔄 Actualizar Producto ---")
            id_prod = input("🆔 Ingrese el ID del producto a actualizar: ")
            print("💡 Deje en blanco el campo si no desea actualizarlo.")
            str_cantidad = input("📊 Nueva cantidad: ")
            str_precio = input("💲 Nuevo precio: ")
            
            nueva_cantidad = int(str_cantidad) if str_cantidad else None
            nuevo_precio = float(str_precio) if str_precio else None
            
            inventario.actualizar_producto(id_prod, nueva_cantidad, nuevo_precio)

        elif opcion == '4':
            print("\n--- 🔍 Buscar Producto ---")
            nombre = input("🏷️ Ingrese el nombre (o parte del nombre) a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == '5':
            print("\n--- 📋 Lista de Productos ---")
            inventario.mostrar_todos()

        elif opcion == '6':
            print("\n💾 Guardando datos...")
            print("👋 ¡Saliendo del sistema. Hasta pronto!")
            break

        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()