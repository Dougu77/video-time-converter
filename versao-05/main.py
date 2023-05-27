from packages.formatar import *
from packages.validar import *
from packages.converter import *

titulo('Velocidade de Vídeo', 70)
print('A função desse programa é calcular o tempo real de um vídeo acelerado.')
print(f'''{"-" * 31} AVISOS {"-" * 31}
-> Digite horas, minutos e segundos separadamente.
-> No caso de não ter algum dos valores, digite 0.''')
linha(70)

while True:

    tempo = validar_Horario()
    velocidade = validar_Velocidade()
    tempo_conv = acelerar_Video(tempo, velocidade)

    titulo('Resultado', 70)
    print(f'''Tempo original: {formatar_Horario(tempo[0], tempo[1], tempo[2])}
Velocidade: {velocidade}
Tempo acelerado: {formatar_Horario(tempo_conv[0], tempo_conv[1], tempo_conv[2])}\n''')

    cont = validar_SN('Calcular mais um tempo? [ S / N ] ')

    if cont:

        linha(70)

    else:

        break
