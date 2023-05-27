from packages.formatar import *
from packages.validar import *
from math import trunc, ceil

titulo('Velocidade de Vídeo', 70)
print('A função desse programa é calcular o tempo real de um vídeo acelerado.')
print(f'''{"-" * 31} AVISOS {"-" * 31}
-> Digite horas, minutos e segundos separadamente.
-> No caso de não ter algum dos valores, digite 0.''')
linha(70)

horas = validar_Horas()
minutos = validar_Minutos()
segundos = validar_Segundos()
velocidade = validar_Float('Velocidade: ')

minutos_convertidos = ((horas * 60) + minutos + (segundos / 60)) / velocidade

horas_aceleradas = minutos_convertidos // 60
minutos_acelerados = trunc(minutos_convertidos - (horas_aceleradas * 60))
segundos_acelerados = ceil((minutos_convertidos - (horas_aceleradas * 60) - minutos_acelerados) * 60)

titulo('Resultado', 70)
print('Tempo original: ', end='')
print(formatar_Horario(horas, minutos, segundos))
print(f'Velocidade: {velocidade}')
print('Tempo acelerado: ', end='')
print(formatar_Horario(int(horas_aceleradas), int(minutos_acelerados), int(segundos_acelerados)))

input('\nPressione ENTER para encerrar o programa')
