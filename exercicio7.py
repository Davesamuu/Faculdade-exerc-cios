idade = int(input("Digite a sua idade para descobrir sua categoria na natação"))
if (idade <= 8):
    print("Sua categoria é a infantil A")
else:
    if (idade < 13):
        print("Sua categoria é a infantil B")
    else:
        if (idade < 18):
            print("Sua categoria é a Juvenil A")
        else:
            if (idade < 21):
                print("Sua categoria é a Juvenil B")
            else:
                if (idade >= 21):
                    print("Sua categoria é a Senior")