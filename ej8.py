class prima_anual:
    def __init__(self, antiguedad,distancia,accidentes): #constructor
        self.antiguedad = antiguedad
        self.distancia = distancia
        self.accidentes = accidentes
        
    def prima_antiguedad(self): #calcula impuesto por antiguedad
        if self.antiguedad < 4:
            return 0
        else:
            return 200 + 20*(self.antiguedad -4)
    
    def prima_distancia(self):   #calcula impuesto por distancia
        return (self.distancia*0.01, 400)
    
    def prima_ponderada(self, prima_antiguedad, prima_distancia): #calculo la media ponderada dependiendo del numero de accidentes
        prima_total = prima_antiguedad + prima_distancia
        if self.accidentes <= 3:
            prima_total = prima_total / (self.accidentes + 1)
        else:
            prima_total = 0
        return prima_total
    
def entrada(valor):
    while True:
        n = input("{}:".format(valor))
        try:
            n = int(n)
            break
        except:
            print("Introduzca un numero sin decimales por favor")
            pass
    return n 

if __name__ == "__main__":
    
    antiguedad = entrada("antiguedad")
    distancia = entrada("distancia")
    accidentes = entrada("accidentes")
    
final= prima_anual(antiguedad=antiguedad, distancia=distancia, accidentes=accidentes)

print("La prima ponderada es: {}".format(final.prima_ponderada(final.prima_antiguedad(),final.prima_distancia())))