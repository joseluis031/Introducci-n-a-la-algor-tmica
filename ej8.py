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
        return(self.distancia*0.01, 400)
    