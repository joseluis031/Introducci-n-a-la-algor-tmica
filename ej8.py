precio = float(input("Precio sin IVA: "))
IVA = 21
precio_conimpuestos = 0
class precios:
    def __init__(self, precio, IVA,precio_conimpuestos): #defino el constructor
        self.precio = precio
        self.IVA = IVA
        self.precio_conimpuestos = precio_conimpuestos
    def con_impuestos(self):
       self.precio_conimpuestos = self.precio + self.precio*0.01*self.IVA
       print("El precio final con impuestos es: ",self.precio_conimpuestos)

resultado = precios(precio, IVA,precio_conimpuestos)
print(resultado.con_impuestos())

capital_invertido = float(input("Capital invertido: "))
interes = float(input("Interes: "))
meses= int(input("¿A cuantos meses?"))
importe = 0
class fincas:
    def __init__(self,capital_invertido,interes,meses, importe):
        self.capital_invertido = capital_invertido
        self.interes = interes
        self.meses = meses
        self.importe = importe
    def importe_interes(self):
        self.importe = round(self.capital_invertido* self.interes*self.meses, 0)
        print("El importe de interes de ", capital_invertido, " a un ", interes*100, "% durante ", meses, " meses es de ", self.importe, " €")
        
resultado2 = fincas(capital_invertido,interes,meses, importe)
print(resultado2.importe_interes())