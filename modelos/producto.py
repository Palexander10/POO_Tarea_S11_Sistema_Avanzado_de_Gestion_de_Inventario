class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id_producto = str(id_producto)
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    @property
    def id_producto(self):
        return self._id_producto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            print("❌ Error: La cantidad no puede ser negativa.")

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print("❌ Error: El precio no puede ser negativo.")

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    def __str__(self):
        return f"📦 ID: {self.id_producto} | 🏷️ Nombre: {self.nombre} | 📊 Cantidad: {self.cantidad} | 💲 Precio: ${self.precio:.2f}"