# 🏪 Sistema Avanzado de Gestión de Inventario
Elaborado por: Pablo Alexander Ramón Mosquera

Este proyecto es un sistema de gestión de inventarios para una tienda, desarrollado en Python y operado mediante una interfaz de consola interactiva. Aplica conceptos de Programación Orientada a Objetos (POO), manejo eficiente de colecciones y persistencia de datos mediante archivos.

## 📁 Arquitectura del Proyecto

El sistema está estructurado de forma modular

Decisiones de Diseño 
Para cumplir con los requerimientos de eficiencia y almacenamiento, se tomaron las siguientes decisiones:
1. Uso de Colecciones (Diccionarios)
Se implementó un Diccionario (dict) de Python en la clase Inventario para almacenar los productos.

Eficiencia: La clave (key) del diccionario es el ID del producto y el valor (value) es el objeto Producto. Al estar implementados como tablas hash en Python, los diccionarios permiten operaciones de búsqueda, inserción y eliminación con una complejidad de tiempo. Esto es significativamente más eficiente que recorrer una lista.

Búsquedas: Para la búsqueda por nombre, se utilizó una Lista por comprensión (List Comprehension), iterando sobre los valores del diccionario para encontrar coincidencias parciales.

2. Almacenamiento y Persistencia de Datos (Archivos JSON)
Para el almacenamiento persistente, se utilizó la librería estándar json.

Serialización (Guardar): Antes de escribir en el archivo inventario.json, las instancias de la clase Producto se transforman en diccionarios nativos de Python utilizando el método to_dict(). Esto permite que la función json.dump() pueda escribir los datos sin errores.

Deserialización (Cargar): Al iniciar el programa, el sistema lee inventario.json usando json.load(). Luego, itera sobre los datos recuperados y reconstruye (instancia) los objetos Producto para cargarlos de nuevo en la memoria de la aplicación.

3. Encapsulamiento
La clase Producto utiliza atributos privados (_atributo) controlados mediante decoradores @property (getters y setters). Esto garantiza la integridad de los datos, evitando, por ejemplo, que se ingresen cantidades o precios negativos.