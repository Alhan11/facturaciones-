class Producto:
    """Clase que representa un producto con nombre y precio."""

    def __init__(self, nombre, precio):
        """Inicializa el producto con un nombre y un precio."""
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return f"{self.nombre} - ${self.precio:.2f}"


class Facturacion:
    """Clase que gestiona la facturación de productos."""

    def __init__(self):
        """Inicializa la lista de productos."""
        self.productos = []

    def agregar_producto(self, nombre, precio):
        """Agrega un producto a la lista de productos."""
        producto = Producto(nombre, precio)
        self.productos.append(producto)

    def calcular_total(self):
        """Calcula el total de la factura."""
        return sum(producto.precio for producto in self.productos)

    def mostrar_factura(self):
        """Muestra los detalles de la factura."""
        print("Factura:")
        for producto in self.productos:
            print(producto)
        print(f"Total: ${self.calcular_total():.2f}")


def main():
    facturacion = Facturacion()  # Crea una nueva instancia de Facturacion

    while True:
        nombre_producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
        if nombre_producto.lower() == 'salir':
            break  # Sale del bucle si el usuario escribe 'salir'

        precio_producto = float(input("Ingrese el precio del producto: "))  # Lee el precio del producto

        # Agrega el producto a la factura
        facturacion.agregar_producto(nombre_producto, precio_producto)

    # Muestra la factura final al usuario
    facturacion.mostrar_factura()


if __name__ == "__main__":
    main()  # Ejecuta el programa
