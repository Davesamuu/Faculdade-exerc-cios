numero1 = int(input("Digite um numero"))
numero2 = int(input("Digite mais um numero"))
numero3 = int(input("Digite mais outro numero"))

if (numero1 == numero2 == numero3):
    print(numero1, "=", numero2, "=", numero3)
else:
    if (numero1 > numero2 and numero1 > numero3 and numero2 > numero3):
        print(numero1, ">", numero2, ">", numero3)
    else:
        if (numero1 > numero2 and numero1 > numero3 and numero3 > numero2):
            print(numero1, ">", numero3, ">", numero2)
        else:
            if (numero2 > numero1 and numero2 > numero3 and numero1 > numero3):
                print(numero2, ">", numero1, ">", numero3)
            else:
                if (numero2 > numero1 and numero2 > numero3 and numero3 > numero1):
                    print(numero2, ">", numero3, ">", numero1)
                else:
                    if (numero3 > numero1 and numero3 > numero2 and numero1 > numero2):
                        print(numero3, ">", numero1, ">", numero2)
                    else:
                        if (numero3 > numero1 and numero3 > numero2 and numero2 > numero1):
                            print(numero3, ">", numero2, ">", numero1)