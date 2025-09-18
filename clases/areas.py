
class Areas:
    def __init__(self):
        self.base = 0
        self.altura = 0
        self.largo = 0
        self.ancho = 0

    def leer_datos_triangulo(self):
        self.base = float(input("Ingrese la base del triángulo: "))
        self.altura = float(input("Ingrese la altura del triángulo: "))

    def leer_datos_rectangulo(self):
        self.largo = float(input("Ingrese el largo del rectángulo: "))
        self.ancho = float(input("Ingrese el ancho del rectángulo: "))

