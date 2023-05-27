# Imports

from tkinter import *

# Configurações - Escrita

cor_fundo = '#202020'
cor_titulo = '#404040'
letra_cor = '#ffffff'
fonte_titulo = 'arial 28'
fonte_geral = 'arial 14'

# Funções

def titulo(master, texto='', row=0):

    Label(master, text=texto, bg=cor_titulo,
          fg=letra_cor, font=fonte_titulo).grid(row=row, columnspan=2, sticky='we')

def texto_sem_fundo(master, texto='', row=0, column=0):

    Label(master, text=texto, bg=cor_fundo,
          fg=letra_cor, font=fonte_geral).grid(row=row, column=column, sticky=W)

def espacamento(master, row):

    Label(master, text='', bg=cor_fundo,
          font=fonte_geral).grid(row=row, columnspan=2)

def recomecar(horas_entry, horas_valor, minutos, segundos, velocidade, erro, result_original, result_vel, result_real):

    horas_valor.set('')
    minutos.set('')
    segundos.set('')
    velocidade.set('')
    erro.set('')
    result_original.set('Tempo original:')
    result_vel.set('Velocidade:')
    result_real.set('Tempo real:')

    horas_entry.focus()
