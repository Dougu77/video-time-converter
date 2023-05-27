from math import trunc, ceil

print('=' * 57)
print('=' * 18, 'Aceleração de Vídeo', '=' * 18)
print('=' * 57)

print('\nEsse programa tem como objetivo calcular o tempo real de um vídeo acelerado.')
print('Digite as horas, os minutos e os segundos separadamente, no caso de não possuir algum desses valores, utilize 0.')
print('Utilize ponto "." ao invés de vírgula ",".\n')

while True:

    h = int(input('Digite as horas: '))

    if h >= 0:

        break

while True:

    m = int(input('Digite os minutos: '))

    if 0 <= m < 60:

        break

while True:

    s = int(input('Digite os segundos: '))

    if 0 <= s < 60:

        break

while True:

    v = float(input('Digite a velocidade: '))

    if v > 0:

        break

min_con = h * 60 + m + s / 60
temp_real_min = min_con / v

novo_h = temp_real_min // 60
novo_m = trunc(temp_real_min - (novo_h * 60))
novo_s = ceil((temp_real_min - novo_m - (novo_h * 60)) * 60)

if novo_s == 60:

    novo_s = 0
    novo_m += 1

if novo_m == 60:

    novo_m = 0
    novo_h += 1

format_h = int(novo_h)
format_m = novo_m
format_s = novo_s

if novo_m < 10:

    format_m = str(novo_m)
    format_m = '0' + format_m

if novo_s < 10:

    format_s = str(novo_s)
    format_s = '0' + format_s

if novo_h > 0:

    print(f'''\nAceleração: {v}
Tempo real do vídeo: {format_h}:{format_m}:{format_s}''')

if novo_h == 0 and novo_m != 0:

    print(f'''\nAceleração: {v}
Tempo real do vídeo: {format_m}:{format_s}''')

if novo_h == 0 and novo_m == 0:

    if novo_s > 1:

        print(f'''\nAceleração: {v}
Tempo real do vídeo: {novo_s} segundos''')

    else:

        print(f'''\nAceleração: {v}
Tempo real do vídeo: {novo_s} segundo''')

input('\nPressione ENTER para encerrar o programa')
