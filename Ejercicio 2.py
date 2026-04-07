class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        return "el valor de x es= " + str(self.x) + " y el valor de y es = " + str(self.y)

    def opuesto(self):
        return Punto(-self.x, -self.y)


# prueba
p1 = Punto(3, 5)

print(p1.eje_x())
print(p1.eje_y())
print(p1.impresion())

p2 = p1.opuesto()
print(p2.impresion())
