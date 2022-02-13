class media_notas:
    def __init__(self, nota1, nota2, nota3): #defino el constructor
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def media_aritmetica(self): #defino la media con decimales
        return (self.nota1 + self.nota2 + self.nota3)/3  
    
    def media_ponderada(self,media_aritmetica): #con esta funcion,utilizando round, redondeo la media con decimales
        return round(media_aritmetica)
    
    