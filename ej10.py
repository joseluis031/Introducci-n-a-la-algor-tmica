altura = float(input("¿altura del triangulo?"))
lado = float(input("¿longitud del lado del triangulo?"))


class area_triangulo:
    def __init__(self,altura,lado): #defino el constructor
        self.altura = altura
        self.lado = lado
    
    def area(self):  #para calcular el area una vez tenga el valor del lado y altura
        return (self.altura*self.lado)/2

    
total = area_triangulo(altura,lado)
print ("El area del triangulo es: ",total.area())
