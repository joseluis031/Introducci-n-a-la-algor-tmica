class area_triangulo:
    def __init__(self,altura,lado): #defino el constructor
        self.altura = altura
        self.lado = lado
    
    def area(self,altura,lado):  #para calcular el area una vez tenga el valor del lado y altura
        return (self.altura*self.lado)/2
    
