# Introduccion-a-la-algoritmica
La direccion de GitHub de este repositorio es: [GitHub](https://github.com/joseluis031/Introduccion-a-la-algoritmica.git)

## Ejercicio 8: Porcentajes, IVA e inversiones
```
precio = float(input("Precio sin IVA: "))
IVA = 21
precio_conimpuestos = 0
class precios:
    def __init__(self, precio, IVA,precio_conimpuestos): #defino el constructor
        self.precio = precio
        self.IVA = IVA
        self.precio_conimpuestos = precio_conimpuestos
    def con_impuestos(self):
       self.precio_conimpuestos = round(self.precio + self.precio*0.01*self.IVA, 2)
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
        self.importe = round(self.capital_invertido* self.interes*self.meses, 2)
        print("El importe de interes de ", capital_invertido, " a un ", interes*100, "% durante ", meses, " meses es de ", self.importe, " €")
        
resultado2 = fincas(capital_invertido,interes,meses, importe)
print(resultado2.importe_interes())
```

## Ejercicio 9: Media aritmética ponderada
```
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
```

## Ejercicio 10: Área del triángulo

```
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
```

## Ejercicio 11: Salario y horas extra

```
horasextra = int(input("¿Cuantas horas extra has trabajado? "))
horas = horasextra + 35 #elminimo
extra = 0
sueldo = 0
class trabajo:
    def __init__(self, horasextra, horas, extra, sueldo): #defino el constructor
        self.horasextra = horasextra
        self.horas = horas
        self.extra = extra
        self.sueldo = sueldo
    
    def horas_totales(self):
        if 36 < self.horas < 43:
            self.extra = float(self.horas*17) * 1.25 
            self.sueldo = (35 * 17) + self.extra  
            print("Ha trabajado: ",horasextra,"horas extra y su sueldo es: ",self.sueldo, "€ ya que ha trabajado en total: ",self.horas,"horas")
            
        if self.horas >= 44:
            self.extra = float(self.horas*17) * 1.50
            self.sueldo = (35*17) + self.extra
            print("Ha trabajado: ",horasextra,"horas extra y su sueldo es: ",self.sueldo,"€ ya que ha trabajado en total: ",self.horas,"horas")
            
resultado = trabajo(horasextra, horas, extra, sueldo)
print(resultado.horas_totales())
```

## Ejercicio 12: Cuenta de depósito

```
cuenta = input("¿Quiere abrir una cuenta en el banco?:")
saldo = 0

class banco:
    def __init__(self,cuenta,saldo): #defino el constructor
        self.cuenta = cuenta
        self.saldo = saldo
    def respuesta(self):
        if self.cuenta == "no":
            print("De acuerdo, gracias")
        if self.cuenta == "si":
            self.saldo = 0
            abono = int(input("Introduzca el dinero que desea:"))
            self.saldo = abono
            print("Tu saldo es:" , self.saldo)
    
    def actividad(self):
        act = input("¿Quiere consultar,retirar o abonar dinero?")
        if act == "no":
            print("De acuerdo, gracias")
        if act == "consultar":
            print("Su saldo es: ", self.saldo , "€")
        if act == "retirar":
            retiro = float(input("Dinero a retirar:"))
            self.saldo = self.saldo - retiro
            print("Su saldo actual es: ",self.saldo)
        if act == "abonar":
            ingreso = float(input("Dinero a ingresar"))
            self.saldo = self.saldo + ingreso
            print("Su saldo es: ", self.saldo, "€")
            
total = banco(cuenta,saldo) 
print(total.respuesta())
print(total.actividad())
```
