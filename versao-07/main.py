# Imports

from tkinter import *
from packages.interface import *
from packages.numeros import *

# Configurações - Interface

base = Tk()
base.title('Velocidade de Vídeo')
base.geometry('664x760+1156+100')
base.resizable(False, False)
base.configure(bg='#202020')

# Configurações - Escrita

cor_fundo = '#202020'
cor_titulo = '#404040'
cor_cabeçalho = '#606060'
letra_cor = '#ffffff'
erro_cor = '#ff0000'
fonte_titulo = 'arial 28'
fonte_geral = 'arial 14'

# Cabeçalho

titulo(base, 'Velocidade de Vídeo', 0)

Label(base, text='''>>> A função desse programa é calcular o tempo real de um vídeo acelerado.
>>> Digite horas, minutos e segundos separadamente.
>>> No caso de não ter algum dos valores, digite 0, ou não digite.
>>> Digite <Tab> para trocar de campo.''',
      bg=cor_cabeçalho, fg=letra_cor,
      font=fonte_geral, justify=LEFT).grid(row=1, columnspan=2, sticky='we')


# Horas

texto_sem_fundo(base, 'Horas:', 2, 0)

horas_valor = StringVar()

horas_entry = Entry(base, textvariable=horas_valor, font=fonte_geral)

horas_entry.grid(row=3, column=0, sticky=W)

horas_entry.focus()

# Minutos

texto_sem_fundo(base, 'Minutos:', 2, 1)

minutos_valor = StringVar()

minutos_entry = Entry(base, textvariable=minutos_valor, font=fonte_geral)

minutos_entry.grid(row=3, column=1, sticky=W)

# -----

espacamento(base, 4)

# Segundos

texto_sem_fundo(base, 'Segundos:', 5, 0)

segundos_valor = StringVar()

segundos_entry = Entry(base, textvariable=segundos_valor, font=fonte_geral)

segundos_entry.grid(row=6, column=0, sticky=W)

# Velocidade

texto_sem_fundo(base, 'Velocidade:', 5, 1)

velocidade_valor = StringVar()

velocidade_entry = Entry(base, textvariable=velocidade_valor, font=fonte_geral)

velocidade_entry.grid(row=6, column=1, sticky=W)

# -----

espacamento(base, 7)

# Calcular - Botão

calcular_botao = Button(base, text='Calcular', bg=cor_cabeçalho,
                        fg=letra_cor, font=fonte_geral,
                        command=lambda: calcular(horas_valor, minutos_valor, segundos_valor,
                                                 velocidade_valor, erro_valor, resul_original_valor,
                                                 result_velocidade_valor, result_real_valor))

calcular_botao.grid(row=8, columnspan=2, sticky='we')

calcular_botao.bind('<Return>', lambda e: calcular_botao.invoke())

# -----

espacamento(base, 9)

# Erro

erro_valor = StringVar()

erro_label = Label(base, textvariable=erro_valor,
                   bg=cor_fundo, fg=erro_cor, font=fonte_geral)

erro_label.grid(row=10, columnspan=2, sticky='we')

# -----

espacamento(base, 11)

# Resultado - Título

titulo(base, 'Resultado', 12)

# -----

espacamento(base, 13)

# Resultado - Tempo original

resul_original_valor = StringVar()

resul_original_valor.set('Tempo original:')

resul_original_label = Label(base, textvariable=resul_original_valor,
                             bg=cor_fundo, fg=letra_cor, font=fonte_geral)

resul_original_label.grid(row=14, columnspan=2, sticky=W)

# -----

espacamento(base, 15)

# Resultado - Velocidade

result_velocidade_valor = StringVar()

result_velocidade_valor.set('Velocidade:')

result_velocidade_label = Label(base, textvariable=result_velocidade_valor,
                                bg=cor_fundo, fg=letra_cor, font=fonte_geral)

result_velocidade_label.grid(row=16, columnspan=2, sticky=W)

# -----

espacamento(base, 17)

# Resultado - Tempo real

result_real_valor = StringVar()

result_real_valor.set('Tempo real:')

result_real_label = Label(base, textvariable=result_real_valor,
                          bg=cor_fundo, fg=letra_cor, font=fonte_geral)

result_real_label.grid(row=18, columnspan=2, sticky=W)

# -----

espacamento(base, 19)

# Recomeçar - Botão

recomecar_botao = Button(base, text='Recomeçar', bg=cor_cabeçalho,
                         fg=letra_cor, font=fonte_geral,
                         command=lambda: recomecar(horas_entry, horas_valor, minutos_valor, segundos_valor,
                                                   velocidade_valor, erro_valor, resul_original_valor,
                                                   result_velocidade_valor, result_real_valor))

recomecar_botao.grid(row=20, columnspan=2, sticky='we')

recomecar_botao.bind('<Return>', lambda e: recomecar_botao.invoke())

base.mainloop()
