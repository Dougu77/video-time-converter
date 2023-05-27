# Imports

from tkinter import *
from math import trunc, ceil

# Funções

def validar_float(dados):

    num = dados.get().strip().replace(',', '.')

    if num == '':

        num = 0

    try:

        float(num)

    except:

        return -1

    else:

        return float(num)

def validar_int(dados):

    num = float(validar_float(dados))

    if num.is_integer():

        return int(trunc(num))

    else:

        return -1

def validar_horario(horas, minutos, segundos):

    h = validar_int(horas)
    m = validar_int(minutos)
    s = validar_int(segundos)

    if h < 0 or m < 0 or s < 0:

        return -1

    elif h == m == s == 0:

        return -1

    elif m >= 60 or s >= 60:

        return -1

    else:

        return h, m, s

def validar_velocidade(velocidade):

    v = validar_float(velocidade)

    if v <= 0:

        return -1

    else:

        return v

def validar_calculo(horas, minutos, segundos, velocidade):

    horario = validar_horario(horas, minutos, segundos)
    v = validar_velocidade(velocidade)

    if horario == -1 or v == -1:

        return -1

    else:

        return horario[0], horario[1], horario[2], v

def calcular(horas, minutos, segundos, velocidade, erro, result_original, result_vel, result_real, event=None):

    dados = validar_calculo(horas, minutos, segundos, velocidade)

    if dados == -1:

        erro.set('ERRO! Dados inválidos')
        result_original.set('Tempo original:')
        result_vel.set('Velocidade:')
        result_real.set('Tempo real:')

    else:

        real = acelerar_video(dados)

        tempo_original = formatar_horario(dados[:3])
        velocidade_formatada = formatar_velocidade(dados[3])
        tempo_real = formatar_horario(real)

        erro.set('')
        result_original.set(f'Tempo original: {tempo_original}')
        result_vel.set(f'Velocidade: {velocidade_formatada}')
        result_real.set(f'Tempo real: {tempo_real}')

def acelerar_video(dados):

    tempo_real = ((dados[0] * 60) + dados[1] + (dados[2] / 60)) / dados[3]

    horas = tempo_real // 60
    minutos = trunc(tempo_real - (horas * 60))
    segundos = ceil((tempo_real - (trunc(tempo_real))) * 60)

    return horas, minutos, segundos

def formatar_horario(horario):

    if horario[0] == 0:

        return f'{int(horario[1])}:{int(horario[2]):0>2}'

    else:

        return f'{int(horario[0])}:{int(horario[1]):0>2}:{int(horario[2]):0>2}'

def formatar_velocidade(velocidade):

    if trunc(velocidade) == velocidade:

        return trunc(velocidade)

    else:

        return velocidade
