ano = int(input("Digite um ano para saber se ele é bissexto ou não"))
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("O ano", ano, "é bissexto")
else:
    print("O ano", ano, "não é bissexto")