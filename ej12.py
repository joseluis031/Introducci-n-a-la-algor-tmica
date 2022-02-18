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