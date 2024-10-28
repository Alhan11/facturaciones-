class Producto:
    """Clase que representa un producto con nombre, precio y tipo."""

    def __init__(self, nombre, precio, tipo):
        """Inicializa el producto con un nombre, un precio y un tipo."""
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return f"{self.nombre} ({self.tipo}) - ${self.precio:.2f}"


class Inventario:
    """Clase que gestiona el inventario de productos."""

    def __init__(self):
        """Inicializa el inventario con productos predeterminados."""
        self.productos = [
            Producto("Samsung Galaxy S23", 999.99, "Celular"),
            Producto("iPhone 14", 1099.99, "Celular"),
            Producto("Xiaomi 12", 749.99, "Celular"),
            Producto("Google Pixel 7", 899.99, "Celular"),
            Producto("OnePlus 10", 799.99, "Celular"),
            Producto("Sony Xperia 1", 949.99, "Celular"),
            Producto("Dell XPS 13", 1299.99, "Computadora"),
            Producto("Apple MacBook Air", 999.99, "Computadora"),
            Producto("HP Spectre x360", 1149.99, "Computadora"),
            Producto("Lenovo ThinkPad X1", 1399.99, "Computadora"),
            Producto("Epson EcoTank", 249.99, "Impresora"),
            Producto("HP LaserJet", 199.99, "Impresora"),
            Producto("Cargador de celular", 19.99, "Repuesto"),
            Producto("Cable USB-C", 9.99, "Repuesto"),
            Producto("Funda de celular", 14.99, "Repuesto"),
            Producto("Teclado inalámbrico", 29.99, "Repuesto"),
            Producto("Mouse inalámbrico", 25.99, "Repuesto")
        ]

    def mostrar_productos(self):
        """Muestra la lista de productos disponibles en el inventario."""
        print("Productos disponibles:")
        for i, producto in enumerate(self.productos):
            print(f"{i + 1}. {producto}")

    def obtener_producto(self, indice):
        """Devuelve un producto dado su índice en la lista."""
        return self.productos[indice]


class Facturacion:
    """Clase que gestiona la facturación de productos."""

    def __init__(self):
        """Inicializa la lista de productos de la factura."""
        self.productos_factura = []

    def agregar_producto(self, producto):
        """Agrega un producto a la lista de productos de la factura."""
        self.productos_factura.append(producto)

    def calcular_total(self):
        """Calcula el total de la factura."""
        return sum(producto.precio for producto in self.productos_factura)

    def mostrar_factura(self):
        """Muestra los detalles de la factura."""
        print("\nFactura:")
        for producto in self.productos_factura:
            print(producto)
        print(f"Total: ${self.calcular_total():.2f}")


def main():
    inventario = Inventario()  # Crea una nueva instancia de Inventario
    facturacion = Facturacion()  # Crea una nueva instancia de Facturacion

    while True:
        inventario.mostrar_productos()  # Muestra la lista de productos
        try:
            seleccion = int(input("Seleccione el número del producto a agregar (0 para salir): "))
            if seleccion == 0:
                break  # Sale del bucle si el usuario elige 0
            if 1 <= seleccion <= len(inventario.productos):
                producto_seleccionado = inventario.obtener_producto(seleccion - 1)
                facturacion.agregar_producto(producto_seleccionado)  # Agrega el producto a la factura
                print(f"Producto agregado: {producto_seleccionado}\n")
            else:
                print("Selección inválida. Por favor, intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Muestra la factura final al usuario
    facturacion.mostrar_factura()


if __name__ == "__main__":
    main()  # Ejecuta el programa
