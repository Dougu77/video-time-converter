def linha(tamanho):

    """
    -> Escreve uma linha branca.
    :param tamanho: tamanho da linha.
    """

    print('-' * tamanho)


def titulo(titulo, tamanho):

    """
    -> Formatação de título.
    :param titulo: título da linha central.
    :param tamanho: tamanho da linha.
    """

    linha(tamanho)
    print(titulo.center(tamanho))
    linha(tamanho)


def formatar_Horario(horas=0, minutos=0, segundos=0):

    """
    -> Formatação de horário.
    :param horas: valor das horas.
    :param minutos: valor dos minutos.
    :param segundos: valor dos segundos.
    :return: horário formatado.
    """

    if horas == 0 and 0 <= minutos < 60 and 0 <= segundos < 60:

        horario = f'{int(minutos)}:{int(segundos):0>2}'

    if horas > 0 and 0 <= minutos < 60 and 0 <= segundos < 60:

        horario = f'{int(horas)}:{int(minutos):0>2}:{int(segundos):0>2}'

    return horario

