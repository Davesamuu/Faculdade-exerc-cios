for i in range(10, 1001):
    centena = (i//100) % 10  # pega a centena
    dezena = (i//10) % 10  # pega a dezena
    unidade = (i % 10)  # pega a dezena
    if (centena == 0 and dezena < unidade):
        print(f"O numero {i} é ascendente pois: {dezena}<{unidade}")
    else:
        if (centena < dezena and dezena < unidade):
            print(
                f"O numero {i} é ascedente pois: {centena}<{dezena}<{unidade}")
