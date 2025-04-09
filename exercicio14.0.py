#Código feito e idealizado por mim
quantidade = int(input("Digite a quantidade do produto que você comprou: "))
preco = float(input("Digite o preço dos produtos que voce comprou: "))
total=0
produtos=0
soma1 = 0
soma2 = 0
while(quantidade!=0 and preco!=0):
    soma1=(soma1+(quantidade*preco)-soma2)
    soma2=soma1
    print(quantidade,"*",preco,"=",soma2)
    total=total+quantidade*preco
    produtos=produtos+quantidade
    quantidade = int(input("Digite a quantidade de x produto você comprou: "))
    preco = float(input("Digite o preço dos produtos que voce comprou: "))
print("O valor total é = ",total)    
print("A quantidade de produtos compradas foi =",produtos)
print("Fim")