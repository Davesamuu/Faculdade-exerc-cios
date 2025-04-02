print("Vamos calcular o seu imc")
peso = float(input("Digite o seu peso"))
altura = float(input("Digite a sua altura"))

imc = peso / (altura * altura)

if (imc < 18):
    print("Voce esta abaixo do peso ja que seu imc é de ", imc)
else:
    if (imc >= 18 and imc < 25):
        print("Peso normal ja que seu imc é de ", imc)
    else:
        if (imc >= 25 and imc < 30):
            print("Voce esta acima do peso ja que seu imc é de ", imc)
        else:
            if (imc >= 30):
                print("Voce esta obeso ja que seu imc é de ", imc)