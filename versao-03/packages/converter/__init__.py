from math import trunc, ceil


def acelerar_Video(tempo, velocidade=1):

    """
    -> Calcula o tempo real de um vídeo acelerado.
    :param tempo: tupla que contém o tempo original.
    :param velocidade: valor da velocidade.
    :return: tupla com o tempo real, sendo
    [0] = horas; [1] = minutos; [2] = segundos.
    """

    horas = tempo[0]
    minutos = tempo[1]
    segundos = tempo[2]

    minutos_acel = ((horas * 60) + minutos + (segundos / 60)) / velocidade

    horas_conv = minutos_acel // 60
    minutos_conv = trunc(minutos_acel - (horas_conv * 60))
    segundos_conv = ceil((minutos_acel - (trunc(minutos_acel))) * 60)

    return horas_conv, minutos_conv, segundos_conv

