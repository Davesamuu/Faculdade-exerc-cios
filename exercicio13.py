idade = int(input("Digite uma idade: "))
soma_idades = 0
divisao = 0
while (idade != 0):
    print(idade)
    soma_idades = soma_idades+idade
    divisao = divisao+1
    idade = int(input("Digite mais uma idade: "))
print("A média de todas as suas idades é = ", soma_idades/divisao)
print("Fim")
