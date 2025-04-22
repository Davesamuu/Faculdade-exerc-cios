cont=0
num=int(input("Digite um número: "))
for i in range(1,num):
    if (num%i==0):
        cont=cont+i
if(num==cont):
    print(f"O número: {num} é perfeito")
else:
    print(f"O número: {num} não é perfeito")
print(cont)