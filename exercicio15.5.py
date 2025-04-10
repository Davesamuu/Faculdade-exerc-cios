#Versão do Professor
variavel = True
resp=0
while(variavel == True):
    operacao = str(input("Qual a operação quer ralizar com esses números inseridos?(+,-,/,* ou # para encerrar): "))
    if (operacao == "#"):
        variavel = False
    else:
        num1=float(input("Qual o primeiro numero?"))
        num2=float(input("Qual o segundo numero?"))
        if(operacao=="+"):
            resp=num1+num2
        if(operacao=="-"):
            resp=num1-num2
        if(operacao=="*"):
            resp=num1*num2
        if(operacao=="/"):
            resp=num1/num2
        print ("A resposta é: ", resp)
print("Fim")