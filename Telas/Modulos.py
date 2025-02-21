import tkinter as tk
from tkinter import Button
from tkinter.ttk import Style


class FuncoesAuxiliares:
    def __init__(self):
        self.style = Style()
        self.style.configure('TLabel',background='#C0C0C0', font=('calibri', 15, 'bold'), padding=(10, 5, 0, 0))
        self.style.configure('TEntry', font=('calibri', 15), padding=(10, 5))
        self.style.configure('TSpinbox', font=('calibri', 15, 'bold'), padding=(10, 4))
        self.style.configure('TCombobox', font=('calibri', 12, 'bold'), padding=(10, 4))
        self.style.configure("Treeview.Heading", font=('calibri', 13))
        self.style.configure("Treeview", font=('calibri', 13))

""" def validate_input(*args):
value = entry_var.get()

# Remove todos os caracteres que não são números ou um ponto decimal
value = ''.join(char for char in value if char.isdigit() or char == '.')

# Garante que haja apenas um ponto decimal
if value.count('.') > 1:
    value = value[:value.rfind('.')]

# Garante que o valor seja exibido no formato "0.00"
if not value:
    value = "0.00"
elif value.count('.') == 0:
    value += ".00"
elif value.index('.') == 0:
    value = "0" + value

entry_var.set(value)"""


class MenuSuperiorSalvar:
    def __init__(self, janela, cor_de_fundo):
        self.janela = janela
        cor_de_fundo='#2A6ED1'
        self.frame = tk.Frame(janela, bg=cor_de_fundo)
        self.frame.grid(column=0, row=0, columnspan=8, sticky='ew')

        self.photosalvar = tk.PhotoImage(file="Imagens/salvar.png")
        self.photoimagesalvar = self.photosalvar.subsample(1, 1) #D0DFBB

        self.btnSalvar = Button(self.frame, text="Salvar",image=self.photoimagesalvar, width=80,
                                font=('calibri', 14, 'bold'), fg='#C3C3C3', compound='top', bg=cor_de_fundo)
        self.btnSalvar.grid(column=0, row=0, padx=10, pady=5)

        self.photovoltar = tk.PhotoImage(file="Imagens/voltar.png")
        self.photoimagevoltar = self.photovoltar.subsample(1, 1)


        self.btnVoltar = Button(self.frame, text="Voltar",image=self.photoimagevoltar, width=80,
                                font=('calibri', 14, 'bold'), fg='#C3C3C3',
                                compound='top', command=self.clickVoltar, bg=cor_de_fundo)
        self.btnVoltar.grid(column=3, row=0,padx=(410, 20))
    def clickVoltar(self):
        self.janela.destroy()

    def detalhae(self):
        self.btnSalvar.destroy()

        self.photosalvar = tk.PhotoImage(file="Imagens/exportar.png")
        self.photoimagesalvar = self.photosalvar.subsample(1, 1)  # D0DFBB

        self.btnSalvar = Button(self.frame, text="Exportar", image=self.photoimagesalvar,
                                             width=80,
                                             font=('calibri', 14, 'bold'), fg='#C3C3C3', compound='top', bg='#2A6ED1')
        self.btnSalvar.grid(column=0, row=0, padx=10, pady=5)


class MenuSuperiorConfirmar:
    def __init__(self, janela, cor_de_fundo, padxVoltar=410):
        self.janela = janela
        cor_de_fundo = '#2A6ED1'
        self.frame = tk.Frame(janela, bg=cor_de_fundo)
        self.frame.grid(column=0, row=0, columnspan=8, sticky='ew')

        self.photoconfirmar = tk.PhotoImage(file="Imagens/confirmar.png")
        self.photoimageconfirmar = self.photoconfirmar.subsample(2, 2)

        self.btnConfirmar = Button(self.frame, text="Confirmar",image=self.photoimageconfirmar, width=80, height=80,
                                   font=('calibri', 12, 'bold'),fg='#C3C3C3', bg=cor_de_fundo, compound='top')
        self.btnConfirmar.grid(column=0, row=0, padx=(10, 250), pady=5)

        self.photovoltar = tk.PhotoImage(file="Imagens/voltar.png")
        self.photoimagevoltar = self.photovoltar.subsample(1, 1)

        self.btnVoltar = Button(self.frame, text="Voltar",image=self.photoimagevoltar, width=80,
                                font=('calibri', 12, 'bold'),fg='#C3C3C3', bg=cor_de_fundo,
                                compound='top', command=self.clickVoltar)
        self.btnVoltar.grid(column=3, row=0,padx=(padxVoltar, 20))
    def clickVoltar(self):
        self.janela.destroy()


class MenuInferiorConsulta:
    def __init__(self, janela, cor_de_fundo,num_row=5):
        self.janela = janela
        cor_de_fundo = '#2A6ED1'
        self.frame = tk.Frame(janela, bg=cor_de_fundo)
        self.frame.grid(column=0, row=num_row, columnspan=8, sticky='ew', pady=10)

        self.photoexportar = tk.PhotoImage(file="Imagens/exportar.png")
        self.photoimageexportar = self.photoexportar.subsample(1, 1)  # D0DFBB

        self.btnExportar = Button(self.frame, text="Exportar", image=self.photoimageexportar,
                                width=80,
                                font=('calibri', 14, 'bold'), fg='#C3C3C3', compound='top', bg='#2A6ED1')
        self.btnExportar.grid(column=0, row=0, padx=10, pady=0)

        self.btnExportar.config(state='disabled')

        self.photoLimpar = tk.PhotoImage(file="Imagens/editar.png")
        self.photoimageLimpar = self.photoLimpar.subsample(1, 1)
        self.btnLimpar = Button(self.frame, text="Limpar", image=self.photoimageLimpar, width=80, height=80,
                                fg='#C3C3C3', bg=cor_de_fundo, font=('calibri', 14, 'bold'),
                                compound='top')
        self.btnLimpar.grid(column=10, row=0, padx=(650, 0), pady=5)


class MenuSuperiorConsulta:
    def __init__(self, janela, cor_de_fundo):
        self.janela = janela
        cor_de_fundo = '#2A6ED1'
        self.frame = tk.Frame(janela, bg=cor_de_fundo)
        self.frame.grid(column=0, row=0, columnspan=8, sticky='ew')

        self.photoNovo = tk.PhotoImage(file="Imagens/novo.png")
        self.photoNovoImagem = self.photoNovo.subsample(1, 1)
        self.btnNovo = Button(self.frame, text="Novo", image=self.photoNovoImagem,width=80,
                              font=('calibri', 14, 'bold'), fg='#C3C3C3', bg=cor_de_fundo, compound='top')
        self.btnNovo.grid(column=0, row=0, padx=10, pady=5)


        self.photoeditar = tk.PhotoImage(file="Imagens/editar.png")
        self.photoimageeditar = self.photoeditar.subsample(1, 1)
        self.btnEditar = Button(self.frame, text="Editar",image=self.photoimageeditar, width=80, bg=cor_de_fundo,
                                font=('calibri', 14, 'bold'), fg='#C3C3C3', compound='top')
        self.btnEditar.grid(column=1, row=0, padx=5)

        self.photodeletar = tk.PhotoImage(file="Imagens/deletar.png")
        self.photoimagedeletar = self.photodeletar.subsample(1, 1)
        self.btnDeletar = Button(self.frame, text="Deletar", image=self.photoimagedeletar, width=80,
                                 font=('calibri', 14, 'bold'), fg='#C3C3C3', bg=cor_de_fundo, compound='top')
        self.btnDeletar.grid(column=2, row=0, padx=5)

        self.photovoltar = tk.PhotoImage(file="Imagens/voltar.png")
        self.photoimagevoltar = self.photovoltar.subsample(1, 1)
        self.btnVoltar = Button(self.frame, text="Voltar", image=self.photoimagevoltar,width=80,
                                font=('calibri', 14, 'bold'), fg='#C3C3C3', bg=cor_de_fundo,compound='top', command=self.clickVoltar)
        self.btnVoltar.grid(column=3, row=0, padx=(450, 20))

    def clickVoltar(self):
        self.janela.destroy()