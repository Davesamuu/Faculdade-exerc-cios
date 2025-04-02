tempo_segundos = int(input("Digite o tempo em segundos: "))

horas = tempo_segundos // 3600
segundos_restantes = tempo_segundos % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(tempo_segundos,"segundos é igual a:",horas,"horas",minutos,"minutos e",segundos,"segundos.")