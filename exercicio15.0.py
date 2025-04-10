#Minha versão
variavel = True
while(variavel == True):
    operacao = str(input("Qual a operação quer ralizar com esses números inseridos?(+,-,/,* ou # para encerrar): "))
    if (operacao == "#"):
        variavel = False
        print("Fim")
    else:
        if (operacao == "+"):
            num1 = float(input("Digite um número: "))
            num2 = float(input("Digite mais um número: "))
            print(f"A soma dos núemeros é {num1+num2}")
        if (operacao == "-"):
            num1 = float(input("Digite um número: "))
            num2 = float(input("Digite mais um número: "))
            print(f"A soma dos núemeros é {num1-num2}")
        if (operacao == "/"):
            num1 = float(input("Digite um número: "))
            num2 = float(input("Digite mais um número: "))
            print(f"A soma dos núemeros é {num1/num2}")
        if (operacao == "*"):
            num1 = float(input("Digite um número: "))
            num2 = float(input("Digite mais um número: "))
            print(f"A soma dos núemeros é {num1*num2}")