class media_notas:
    def __init__(self, nota1, nota2, nota3): #defino el constructor
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def media_aritmetica(self): #defino la media con decimales
        return (self.nota1 + self.nota2 + self.nota3)/3  
    
    def media_ponderada(self,media_aritmetica): #con esta funcion,utilizando round, redondeo la media con decimales
        return round(media_aritmetica)
  
def introduce_nota(i):
    while True:
            nota = input("Introduce la {}ª nota:".format(i+1)) #para que empiece desde 1
            try:
                nota = float(nota)
                break
            except:
                print ("Sustituya la coma por punto por favor")
                pass
    return nota
    
    
if __name__ == "__main__":
    
   notas=[]
   for i in range(3):  #para que solo me pida 3 notas
       n = introduce_nota(i)
       notas.append(n) 
       
    
total = media_notas(n[0], n[1], n[2])
    
print("La media aritmetica es{}:".format(total.media_aritmetica()))
print("La media ponderada es{}".format(total.media_ponderada(total.media_aritmetica())))