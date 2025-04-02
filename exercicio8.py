valorCompra = int(input("Digite quanto você gastou para ganhar um desconto refente a esse valor"))
if (valorCompra < 200):
    desconto = (valorCompra * 0.15)
    final = valorCompra - desconto
    print("Voce gastou ", valorCompra, " Reais")
    print("Voce ganhou 15% de desconto que é de - ", desconto, " Reais , então seu produto agora custara ", final, " Reais")
else:
    if (valorCompra >= 200 and valorCompra < 500):
        desconto = (valorCompra * 0.20)
        final = valorCompra - desconto
        print("Voce gastou ", valorCompra, " Reais")
        print("Voce ganhou 20% de desconto que é de ", desconto, " Reais , então seu produto agora custara ", final, " Reais")
    else:
        if (valorCompra >= 500):
            desconto = (valorCompra * 0.25)
            final = valorCompra - desconto
            print("Voce gastou ", valorCompra, " Reais")
            print("Voce ganhou 25% de desconto que é de ", desconto, " Reais , então seu produto agora custara ", final, " Reais")