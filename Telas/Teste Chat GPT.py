import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import pygame

from Classes.item import Item


class ItemForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Item")

        # Crie variáveis para os campos do Item
        self.id_item_var = tk.StringVar()
        self.descricao_var = tk.StringVar()
        self.qtd_var = tk.DoubleVar()
        self.preco_var = tk.DoubleVar()

        # Crie rótulos e campos de entrada para os atributos do Item
        tk.Label(master, text="ID Item:").grid(row=0, column=0)
        tk.Entry(master, textvariable=self.id_item_var).grid(row=0, column=1)

        tk.Label(master, text="Descrição:").grid(row=1, column=0)
        tk.Entry(master, textvariable=self.descricao_var).grid(row=1, column=1)

        tk.Label(master, text="Quantidade:").grid(row=2, column=0)
        tk.Entry(master, textvariable=self.qtd_var).grid(row=2, column=1)

        tk.Label(master, text="Preço:").grid(row=3, column=0)
        tk.Entry(master, textvariable=self.preco_var).grid(row=3, column=1)

        # Crie um botão para exibir os valores
        tk.Button(master, text="Mostrar Item", command=self.mostrar_item).grid(row=4, column=0, columnspan=2)

    def mostrar_item(self):
        id_item = self.id_item_var.get()
        descricao = self.descricao_var.get()
        qtd = self.qtd_var.get()
        preco = self.preco_var.get()

        item = Item(iditem=id_item, descricao=descricao, qtd=qtd, preco=preco)
        print("Informações do Item:")
        print("ID do Item:", item.get_id_item())
        print("Descrição:", item.get_descricao())
        print("Quantidade:", item.get_qtd())
        print("Preço:", item.get_preco())


###from PIL import Image

#icon = pygame.image.load("copiar.png")
#pygame.display.set_icon(icon)

#image = Image.open('copiar.png')
#image.show()

#if __name__ == "__main__":
 #   root = tk.Tk()
  #  app = ItemForm(root)
   # root.mainloop()

import tkinter
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
# Position text in frame
Label(root, text = 'Position image on button')
# Create a photoimage object of the image in the path
photo = PhotoImage(file ="../Imagens/copiar.png")
# Resize image to fit on button
photoimage = photo.subsample(1, 2)
# Position image on button
var=Button(root, image = photoimage)
var.grid(row=0)
mainloop()
