
class Areas:
    def __init__(self):
        self.base = 0
        self.altura = 0
        self.largo = 0
        self.ancho = 0
        self.radio = 0

    def leer_datos_triangulo(self):
        self.base = float(input("Ingrese la base del triángulo: "))
        self.altura = float(input("Ingrese la altura del triángulo: "))

    def leer_datos_rectangulo(self):
        self.largo = float(input("Ingrese el largo del rectángulo: "))
        self.ancho = float(input("Ingrese el ancho del rectángulo: "))

    def leer_datos_circulo(self):
        self.radio = float(input("Ingrese el radio del círculo: "))

    def calcular_area_circulo(self):
        return 3.1416 * (self.radio ** 2)

    def mostrar_area_circulo(self):
        area = self.calcular_area_circulo()
        print(f"El área del círculo es: {area}")

