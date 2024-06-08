tempo = int(input("Por favor, entre com o número de segundos que deseja converter: "))

divisor_dias = 60*60*24
divisor_horas = divisor_dias/24
divisor_minutos = divisor_horas/60

quantidade_dias    = tempo // divisor_dias
resto_segundos     = tempo % divisor_dias

quantidade_horas   = int(resto_segundos // divisor_horas)
resto_segundos     = int(resto_segundos % divisor_horas)

quantidade_minutos = int(resto_segundos // divisor_minutos)
resto_segundos     = int(resto_segundos % divisor_minutos)

print(f"{quantidade_dias} dias, {quantidade_horas} horas, {quantidade_minutos} minutos e {resto_segundos} segundos.")