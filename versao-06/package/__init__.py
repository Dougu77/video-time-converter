from tkinter import *
from math import trunc, ceil

cor_fundo = '#202020'
cor_letra = '#ffffff'
fonte_geral = 'arial 14'

def espacamento(master, row):

    Label(master, text='',
          bg=cor_fundo,
          font=fonte_geral).grid(row=row, columnspan=2)

def texto_sem_fundo(master, texto, row, column):

    Label(master, text=texto,
          bg=cor_fundo, fg=cor_letra,
          font=fonte_geral).grid(row=row, column=column, sticky=W)

def proxima_entry(event=None):

    print('OK')

def calcular_botao(horas, minutos, segundos, velocidade, erro, temp_original, result_velocidade, temp_real):

    horas_original = horas.get().strip()
    minutos_original = minutos.get().strip()
    segundos_original = segundos.get().strip()
    velocidade_original = velocidade.get().strip()

    validade_h = validar_h(horas_original)
    validade_m = validar_m_s(minutos_original)
    validade_s = validar_m_s(segundos_original)
    validade_v = validar_v(velocidade_original)

    if validade_h == -1 or validade_m == -1 or validade_s == -1 or validade_v == -1:

        erro.set('ERRO! Digite dados válidos')
        temp_original.set('Tempo original:')
        result_velocidade.set('Velocidade:')
        temp_real.set('Tempo real:')

    elif validade_h == validade_m == validade_s == 0:

        erro.set('ERRO! Digite dados válidos')
        temp_original.set('Tempo original:')
        result_velocidade.set('Velocidade:')
        temp_real.set('Tempo real:')

    else:

        erro.set('')

        tempo_calculado = tempo_acelerado(validade_h, validade_m, validade_s, validade_v)

        tempo_original_formatado = formatar_horario((validade_h, validade_m, validade_s))

        velocidade_formatada = formatar_velocidade(validade_v)

        tempo_real_formatado = formatar_horario(tempo_calculado)

        temp_original.set(f'Tempo original: {tempo_original_formatado}')
        result_velocidade.set(f'Velocidade: {velocidade_formatada}')
        temp_real.set(f'Tempo real: {tempo_real_formatado}')

def validar_h(dados):

    num = dados.replace(',', '.')

    if num == '':

        num = 0

    try:

        float(num)

    except ValueError:

        return -1

    else:

        if float.is_integer(float(num)):

            if float(num) < 0:

                return -1

            else:

                return int(trunc(float(num)))

        else:

            return -1

def validar_m_s(dados):


    num = dados.replace(',', '.')

    if num == '':

        num = 0

    try:

        float(num)

    except ValueError:

        return -1

    else:

        if float.is_integer(float(num)):

            if 0 <= float(num) < 60:

                return int(trunc(float(num)))

            else:

                return -1

        else:

            return -1


def validar_v(dados):

    num = dados.replace(',', '.')

    if num == '':

        num = 0

    try:

        float(num)

    except ValueError:

        return -1

    else:

        if float(num) <= 0:

            return -1

        else:

            return float(num)

def tempo_acelerado(horas, minutos, segundos, velocidade):

    minutos_acel = ((horas * 60) + minutos + (segundos / 60)) / velocidade

    horas_conv = minutos_acel // 60
    minutos_conv = trunc(minutos_acel - (horas_conv * 60))
    segundos_conv = ceil((minutos_acel - (trunc(minutos_acel))) * 60)

    return horas_conv, minutos_conv, segundos_conv

def formatar_horario(horario):

    if horario[0] == 0:

        return f'{int(horario[1])}:{int(horario[2]):0>2}'

    else:

        return f'{int(horario[0])}:{int(horario[1]):0>2}:{int(horario[2]):0>2}'

def formatar_velocidade(velocidade):

    if trunc(velocidade) == velocidade:

        return int(velocidade)

    else:

        return float(velocidade)

def recomecar_botao(horas_entry, horas, minutos, segundos, velocidade, erro, temp_original, reslt_velocidade, temp_real):

    horas_entry.focus()
    horas.set('')
    minutos.set('')
    segundos.set('')
    velocidade.set('')
    erro.set('')
    temp_original.set('Tempo original: ')
    reslt_velocidade.set('Velocidade: ')
    temp_real.set('Tempo real: ')
