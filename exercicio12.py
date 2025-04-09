nota = float(input("Digite uma nota: "))
while(nota>10 or 0>=nota):
    print("Nota invalida")
    nota = float(input("Digite uma nota: "))
if(nota<=10 or nota>=0):
    print("Nota valida") 
print("Fim")