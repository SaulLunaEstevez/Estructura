from producto import Producto

class Almacen:
    def __init__(self):
        self.productos = []
        self.retirados = []
        
    def agregar_producto(self):
        producto = Producto(f"producto{len(self.productos) + 1}")
        self.productos.append(producto)
        
    def retirar_producto(self, nombre_producto=None):
        if nombre_producto:
            self.productos = [p for p in self.productos if p.nombre != nombre_producto]
        else:
            if self.productos:
                producto_retirado = self.productos.pop()
                self.retirados.append(producto_retirado)
                
    def disminuir_cantidad(self, nombre_producto, cabtudad_a_disminuir):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.cantidad -= cabtudad_a_disminuir
                if producto.cantidad <= 0:
                    producto.cantidad += cabtudad_a_disminuir
                    self.retirados.append(producto)
                    self.productos.remove(producto)
                    
                break

    def eliminar_todos(self):
        for prod in self.productos:
            self.retirados.append(prod)
        self.productos.clear()

    def mostrar_productos(self):
        return self.productos
    
    def mostrar_retirados(self):
        return self.retirados
