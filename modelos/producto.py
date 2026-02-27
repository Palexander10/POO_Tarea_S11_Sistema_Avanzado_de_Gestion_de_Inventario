# Representa un producto del inventario con encapsulamiento.
class Producto:

    # Inicializa los atributos del producto.
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id_producto = str(id_producto)
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio
    
    # Retorna el ID único del producto.
    @property
    def id_producto(self):
        return self._id_producto

    # Retorna el nombre del producto.
    @property
    def nombre(self):
        return self._nombre

    # Modifica el nombre del producto.
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Retorna la cantidad en stock.
    @property
    def cantidad(self):
        return self._cantidad

    # Modifica la cantidad validando que no sea negativa.
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            print("❌ Error: La cantidad no puede ser negativa.")

    # Retorna el precio del producto.
    @property
    def precio(self):
        return self._precio

    # Modifica el precio validando que no sea negativo.
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print("❌ Error: El precio no puede ser negativo.")

    # Convierte el producto a diccionario para guardarlo en JSON.
    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    def __str__(self):
        return (
        f"📦 ID: {self.id_producto}\n"
        f"🏷️ Nombre: {self.nombre}\n"
        f"📊 Cantidad: {self.cantidad}\n"
        f"💲 Precio: ${self.precio:.2f}"
    )