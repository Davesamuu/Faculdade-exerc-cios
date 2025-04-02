sexo = str(input("Digite seu sexo"))
altura = float(input("Digite sua altura"))
if(sexo == "M"):
    peso_ideal = (72.7*altura) - 58
    print("Você é",sexo,"Então seu peso ideal é de =",peso_ideal,"kg")
if(sexo == "F"):
    peso_ideal = (62.1*altura) - 44.7
    print("Você é",sexo,"Então seu peso ideal é de =",peso_ideal,"kg")
