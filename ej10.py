class area_triangulo:
    def __init__(self,altura,lado): #defino el constructor
        self.altura = altura
        self.lado = lado
    
    def area(self,altura,lado):  #para calcular el area una vez tenga el valor del lado y altura
        return (self.altura*self.lado)/2
    
def entrada(valor):
    while True:
        n = input ("{}:".format(valor))
        try:
            n = float(n)
            break
        except:
            print("Introduce un numero valido por favor")
            pass
    return n

if __name__ == "__main__":
    altura = entrada("¿altura del triangulo?")
    lado = entrada("¿longitud del lado del triangulo?")