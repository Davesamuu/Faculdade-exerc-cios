for i in range(1000, 10000):
    p1 = (i // 100)  # pega os dois primeiros dígitos
    p2 = (i % 100)   # pega os dois últimos dígitos
    teste = p1 + p2
    if (teste * teste == i):
        print(f"O numero {i} atende as demandas pois: ({p1}+{p2})² é = {i}")
