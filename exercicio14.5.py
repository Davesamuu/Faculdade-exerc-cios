#Código refeito e atualizado pelo Chat GPT
quantidade = int(input("Digite a quantidade do produto que você comprou: "))
preco = float(input("Digite o preço dos produtos que você comprou: "))

total = 0
produtos = 0

while quantidade != 0 and preco != 0:
    valor_compra = quantidade * preco
    print(f"Compra atual: {quantidade} x {preco} = R${valor_compra:.2f}")
    
    total += valor_compra
    produtos += quantidade
    
    quantidade = int(input("Digite a quantidade do próximo produto (ou 0 para encerrar): "))
    preco = float(input("Digite o preço dos produtos (ou 0 para encerrar): "))

print("\nResumo final:")
print("O valor total é = R$", total)
print("A quantidade total de produtos comprados foi =", produtos)
print("Fim")
