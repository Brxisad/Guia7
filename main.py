from figuras import Cuadrado, Circulo, Triangulo

figuras = [
    Cuadrado(4),
    Circulo(3),
    Triangulo(6, 2)
]

for figura in figuras:
    print(f"Área: {figura.area():.2f}")