from packages.formatar import *
from packages.validar import *
from packages.converter import *

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
tempo_conv = acelerar_Video((horas, minutos, segundos), velocidade)

titulo('Resultado', 70)
print(f'''Tempo original: {formatar_Horario(horas, minutos, segundos)}
Velocidade: {velocidade}
Tempo acelerado: {formatar_Horario(tempo_conv[0], tempo_conv[1], tempo_conv[2])}''')

input('\nPressione ENTER para encerrar o programa')
