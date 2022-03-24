from unicodedata import decimal
from decimal import Decimal


peso=int(input("Cuanto pesas, en kilos?"))
altura=(input("Cuánto mides, en metros?"))
alturaDecimal=Decimal(altura.replace(',','.'))

def calcularImc(peso, alturaDecimal):
    imc=peso/alturaDecimal**2
    return round(imc,2)

print("Tu IMC es: "+str(calcularImc(peso, alturaDecimal)))

