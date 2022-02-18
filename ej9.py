nota1 = float(input("Introduce la 1ª nota:"))
nota2 = float(input("Introduce la 2ª nota:"))
nota3 = float(input("Introduce la 3ª nota:"))


class media_notas:
    def __init__(self, nota1, nota2, nota3): #defino el constructor
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def media_aritmetica(self): #defino la media con decimales
        return (self.nota1 + self.nota2 + self.nota3)/3  
    
    def media_ponderada(self): #con esta funcion,utilizando round, redondeo la media con decimales
        return round((self.nota1 + self.nota2 + self.nota3)/3,0)



resultado = media_notas(nota1, nota2, nota3)  
print("La media aritmetica es:", resultado.media_aritmetica())
print("La media ponderada es:",resultado.media_ponderada())