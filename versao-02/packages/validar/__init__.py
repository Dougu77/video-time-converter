from math import trunc


def validar_Int(pergunta):

    """
    -> Valida se a resposta digitada foi um número inteiro.
    :param pergunta: pergunta, com resposta de um número inteiro.
    :return: resposta, formatada como um número inteiro.
    """

    while True:

        try:

            inteiro = int(input(pergunta))

        except:

            print('ERRO! Digite uma resposta válida.')

        else:

            break

    return inteiro


def validar_Float(pergunta):

    """
    -> Valida se a resposta digitada foi um float.
    :param pergunta: perrgunta, com resposta de um float.
    :return: resposta, formatada como float.
    """

    while True:

        real = input(pergunta).strip().replace(',', '.')

        if real.isalpha() or len(real) == 0:

            print('ERRO! Digite uma resposta válida.')

        else:

            break

    return float(real)


def validar_Horas():

    """
    -> Valida se a resposta é um número inteiro maior ou igual a 0.
    :return: valor das horas.
    """

    while True:

        horas = validar_Int('Horas: ')

        if horas >= 0:

            break

        else:

            print('ERRO! Digite um número maior ou igual a 0.')

    return horas


def validar_Minutos():

    """
    -> Valida se a resposta é um número inteiro entre 0 e 59.
    :return: valor dos minutos.
    """

    while True:

        minutos = validar_Int('Minutos: ')

        if 0 <= minutos < 60:

            break

        else:

            print('ERRO! Digite um número entre 0 e 59.')

    return minutos


def validar_Segundos():

    """
    -> Valida se a resposta é um número inteiro entre 0 e 59.
    :return: valor dos segundos.
    """

    while True:

        segundos = validar_Int('Segundos: ')

        if 0 <= segundos < 60:

            break

        else:

            print('ERRO! Digite um número entre 0 e 59.')

    return segundos
