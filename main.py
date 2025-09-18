from clases.areas import Areas

mi_area = Areas()

mi_area.leer_datos_triangulo()
print(f"Base del triángulo: {mi_area.base}")
print(f"Altura del triángulo: {mi_area.altura}")
mi_area.leer_datos_rectangulo()

print(f"Largo del rectángulo: {mi_area.largo}")
print(f"Ancho del rectángulo: {mi_area.ancho}")

from clases.areas import Areas

mi_area = Areas()
mi_area.leer_datos_circulo()
mi_area.mostrar_area_circulo()