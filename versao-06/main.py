# Módulos

from tkinter import *
from package import *

# Configurações GUI

base = Tk()
base.title('Velocidade de Vídeo')
base.geometry('664x804+1156+100')
base.resizable(False, False)
base.configure(bg=cor_fundo)

# Configurações escrita

cor_fundo = '#202020'
cor_titulo = '#404040'
cor_cabeçalho = '#606060'
cor_letra = '#ffffff'
cor_erro = '#ff0000'
fonte_titulo = 'arial 28'
fonte_geral = 'arial 14'

# Cabeçalho

Label(base, text='Velocidade de Vídeo',
      bg=cor_titulo, fg=cor_letra,
      font=fonte_titulo).grid(row=0, columnspan=2, sticky='we')

Label(base, text='''>>> A função desse programa é calcular o tempo real de um vídeo acelerado.
>>> Digite horas, minutos e segundos separadamente.
>>> No caso de não ter algum dos valores, digite 0, ou não digite.
>>> Digite <Tab> para trocar de campo.
>>> Digite <Enter> para fazer o cálculo, ou pressione o botão "Calcular".
>>> Digite <Espaço> para recomeçar, ou pressione o botão "Recomeçar".''',
      bg=cor_cabeçalho, fg=cor_letra,
      font=fonte_geral, justify=LEFT).grid(row=1, columnspan=2, sticky='we')

# Horas

texto_sem_fundo(base, 'Horas:', 2, 0)

horas_entry = StringVar()

horas = Entry(base, textvariable=horas_entry, font=fonte_geral)

horas.grid(row=3, column=0, sticky=W)

horas.focus_set()

# Minutos

texto_sem_fundo(base, 'Minutos:', 2, 1)

minutos_entry = StringVar()

minutos = Entry(base, textvariable=minutos_entry,
                font=fonte_geral).grid(row=3, column=1, sticky=W)

# -----

espacamento(base, 4)

# Segundos

texto_sem_fundo(base, 'Segundos:', 5, 0)

segundos_entry = StringVar()

segundos = Entry(base, textvariable=segundos_entry,
                 font=fonte_geral).grid(row=6, column=0, sticky=W)

# Velocidade

texto_sem_fundo(base, 'Velocidade:', 5, 1)

velocidade_entry = StringVar()

velocidade = Entry(base, textvariable=velocidade_entry,
                   font=fonte_geral).grid(row=6, column=1, sticky=W)

# -----

espacamento(base, 7)

# Calcular

calcular = Button(base, text='Calcular',
                  bg=cor_cabeçalho, fg=cor_letra,
                  font=fonte_geral,
                  command=lambda: calcular_botao(horas_entry, minutos_entry, segundos_entry,
                                                 velocidade_entry, erro_dados, tempo_original_dados,
                                                 velocidade_dados, tempo_real_dados))

calcular.grid(row=8, columnspan=2, sticky='we')

base.bind('<Return>', lambda e: calcular.invoke())

# -----

espacamento(base, 9)

# Erro

erro_dados = StringVar()

erro = Label(base, textvariable=erro_dados,
             bg=cor_fundo, fg=cor_erro,
             font=fonte_geral).grid(row=10, columnspan=2, sticky='we')

# -----

espacamento(base, 11)

# Resultado - Título

Label(base, text='Resultado',
      bg=cor_titulo, fg=cor_letra,
      font=fonte_titulo).grid(row=12, columnspan=2, sticky='we')

# -----

espacamento(base, 13)

# Resultado - Tempo original

tempo_original_dados = StringVar()

tempo_original_dados.set('Tempo original:')

tempo_original = Label(base, textvariable=tempo_original_dados,
                       bg=cor_fundo, fg=cor_letra,
                       font=fonte_geral).grid(row=14, columnspan=2, sticky=W)

# -----

espacamento(base, 15)

# Resultado - Velocidade

velocidade_dados = StringVar()

velocidade_dados.set('Velocidade:')

velocidade_resultado = Label(base, textvariable=velocidade_dados,
                             bg=cor_fundo, fg=cor_letra,
                             font=fonte_geral).grid(row=16, columnspan=2, sticky=W)

# -----

espacamento(base, 17)

# Resultado - Tempo real

tempo_real_dados = StringVar()

tempo_real_dados.set('Tempo real:')

tempo_real = Label(base, textvariable=tempo_real_dados,
                   bg=cor_fundo, fg=cor_letra,
                   font=fonte_geral).grid(row=18, columnspan=2, sticky=W)

# -----

espacamento(base, 19)

# Recomeçar

recomecar = Button(base, text='Recomeçar',
                   bg=cor_cabeçalho, fg=cor_letra,
                   font=fonte_geral,
                   command=lambda: recomecar_botao(horas, horas_entry, minutos_entry, segundos_entry,
                                                   velocidade_entry, erro_dados, tempo_original_dados,
                                                   velocidade_dados, tempo_real_dados))

recomecar.grid(row=20, columnspan=2, sticky='we')

base.bind('<space>', lambda e: recomecar.invoke())

base.mainloop()
