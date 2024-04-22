from tkinter import *
from conectar import cursor, conexao
from read import listar_numeros, listar_numeros_no


janela = Tk()

class Aplicacao:
    def __init__(self):
        self.janela = janela
        self.tela()


    def tela(self):
        self.janela.title('Mega Sena')
        self.janela.configure(background='#ff0')
        self.janela.geometry('700x500')
        self.janela.resizable(True, False)
        self.janela.maxsize(width=700, height=500)
        self.janela.mainloop()