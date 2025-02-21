import tkinter as tk
from Telas.Modulos import FuncoesAuxiliares
from Telas.telas_ajuste_itens import Consulta_Ajuste_Item
from Telas.telas_ajuste_tanque import Consulta_Ajuste_Tanque
from Telas.telas_colheita import Consulta_Colheita
from Telas.telas_compras import Consulta_Compra
from Telas.telas_entrada_peixe import Consulta_Entrada_Peixe
from Telas.telas_fornecedor import Consulta_Fornecedor
from Telas.telas_horarios_alimentacao import Consulta_Horario_Alimentacao
from Telas.telas_itens import Consulta_Item
from Telas.telas_tanque import Consulta_Tanque


class Menu_principal:
    def __init__(self):

        self.window = tk.Tk()

        self.window.state("zoomed")
        self.window.style = FuncoesAuxiliares().style

        self.window.title("Tilapicultura")
        self.cor_de_fundo = '#C0C0C0'
        self.cor_de_fundo_menu = '#2A6ED1'
        self.window.config(background=self.cor_de_fundo)
        self.largura_tela_width = self.window.winfo_screenwidth()
        self.altura_tela_height = self.window.winfo_screenheight()
        self.menu_superior_tanque()

        self.frame_menu_lateral = tk.Frame(self.window)
        self.frame_menu_lateral.grid(row=1, column=0,rowspan=10, padx=0, sticky='sn', pady=0)
        self.frame_menu_lateral.config(background=self.cor_de_fundo_menu)
        self.photofornecedor = tk.PhotoImage(file="Imagens/fornecedor.png")
        self.photoimagefornecedor = self.photofornecedor.subsample(1,1)  # D0DFBB

        self.btnfornecedor = tk.Button(self.frame_menu_lateral, text="Fornecedor", image=self.photoimagefornecedor,
                                   width=100, height=100,
                                   font=('calibri', 14, 'bold'), fg='#C3C3C3', compound='top',
                                   bg=self.cor_de_fundo_menu, command=self.clickFornecedor)
        self.btnfornecedor.grid(column=0, row=0, padx=10, pady=10)

        self.photocompra= tk.PhotoImage(file="Imagens/Compra.png")
        self.photoimagecompra = self.photocompra.subsample(2, 2)  # D0DFBB

        self.btncompra = tk.Button(self.frame_menu_lateral, text="Compras", image=self.photoimagecompra,
                                       width=100, height=100,
                                       font=('calibri', 14, 'bold'), fg='#C3C3C3', compound='top',
                                       bg=self.cor_de_fundo_menu, command=self.clickCompra)
        self.btncompra.grid(column=0, row=1, padx=10, pady=10)

        self.photoitens = tk.PhotoImage(file="Imagens/produto.png")
        self.photoimageitens = self.photoitens.subsample(1, 1)  # D0DFBB

        self.btnitens = tk.Button(self.frame_menu_lateral, text="Itens", image=self.photoimageitens,
                                   width=100, height=100,
                                   font=('calibri', 14, 'bold'), fg='#C3C3C3', compound='top',
                                   bg=self.cor_de_fundo_menu, command=self.clickItem)
        self.btnitens.grid(column=0, row=2, padx=10, pady=10)

        self.photoajusteitens = tk.PhotoImage(file="Imagens/Cadastro.png")
        self.photoimageajusteitens = self.photoajusteitens.subsample(2, 2)  # D0DFBB

        self.btnAjusteItens = tk.Button(self.frame_menu_lateral, text="Ajuste Itens", image=self.photoimageajusteitens,
                                  width=100, height=100,
                                  font=('calibri', 14, 'bold'), fg='#C3C3C3', compound='top',
                                  bg=self.cor_de_fundo_menu, command=self.clickAjusteItens)
        self.btnAjusteItens.grid(column=0, row=3, padx=10, pady=10)

        self.lbl = tk.Label(self.window, bg=self.cor_de_fundo_menu,height=self.altura_tela_height)
        self.lbl.grid(column=0, row=6, padx=0, pady=550)


        self.photoalogo = tk.PhotoImage(file="Imagens/726-removebg-preview.png")
        self.photoimagelogo = self.photoalogo.subsample(3, 3)  # D0DFBB

        self.lbllogo = tk.Label(image=self.photoimagelogo,height=125,width=125,bg=self.cor_de_fundo_menu)
        self.lbllogo.grid(column=0, row=0, padx=0, pady=0)

        self.lbl = tk.Label(self.window, bg=self.cor_de_fundo_menu, height=8, width=self.largura_tela_width)
        self.lbl.grid(column=4, row=0, padx=0, pady=0)



    def menu_superior_tanque(self):
        self.frame_menu_superior_peixes = tk.Frame(self.window)
        self.frame_menu_superior_peixes.grid(row=0, column=1, padx=0, pady=0)
        self.frame_menu_superior_peixes.config(background=self.cor_de_fundo_menu)

        self.phototanque = tk.PhotoImage(file="Imagens/piscicultura (2).png")
        self.photoimagetanque = self.phototanque.subsample(4, 4)  # D0DFBB

        self.btnTanque = tk.Button(self.frame_menu_superior_peixes, text="Tanque", image=self.photoimagetanque,
                                   width=100, height=100,
                                   font=('calibri', 14, 'bold'), fg='#C3C3C3', compound='top',
                                   bg=self.cor_de_fundo_menu, command=self.clickTanque)
        self.btnTanque.grid(column=0, row=0, padx=10, pady=10)

        self.photoEntrada = tk.PhotoImage(file="Imagens/tanque 3.png")
        self.photoimageEntrada = self.photoEntrada.subsample(3, 3)  # D0DFBB

        self.btnEntrada = tk.Button(self.frame_menu_superior_peixes, text="Entrada Peixes",
                                          image=self.photoimageEntrada,
                                          width=100, height=100,
                                          font=('calibri', 12, 'bold'), fg='#C3C3C3', compound='top',
                                          command=self.clickEntradaPeixe, bg=self.cor_de_fundo_menu)
        self.btnEntrada.grid(column=1, row=0, padx=10, pady=10)

        self.photoColheita = tk.PhotoImage(file="Imagens/piscicultura.png")
        self.photoimageColheita = self.photoColheita.subsample(2, 2)  # D0DFBB

        self.btnColheita = tk.Button(self.frame_menu_superior_peixes, text="Colheita", image=self.photoimageColheita,
                                     width=100, height=100,
                                     font=('calibri', 14, 'bold'), fg='#C3C3C3', compound='top',
                                     command=self.clickColheita, bg=self.cor_de_fundo_menu)
        self.btnColheita.grid(column=2, row=0, padx=10, pady=10)

        self.photoAjusteTanque = tk.PhotoImage(file="Imagens/anzol-de-pesca.png")
        self.photoimageAjusteTanque = self.photoAjusteTanque.subsample(3, 3)  # D0DFBB

        self.btnAjusteTanque = tk.Button(self.frame_menu_superior_peixes, text="Ajuste Tanque",
                                         image=self.photoimageAjusteTanque,
                                         width=100, height=100,
                                         font=('calibri', 12, 'bold'), fg='#C3C3C3', compound='top',
                                         command=self.clickAjusteTanque, bg=self.cor_de_fundo_menu)
        self.btnAjusteTanque.grid(column=3, row=0, padx=10, pady=10)


        self.photoHorario = tk.PhotoImage(file="Imagens/relogio.png")
        self.photoimageHorario = self.photoHorario.subsample(2, 2)  # D0DFBB

        self.btnHorario = tk.Button(self.frame_menu_superior_peixes, text="Hórario\nAlimentação",
                                    image=self.photoimageHorario,
                                    width=100, height=100,
                                    font=('calibri', 13, 'bold'), fg='#C3C3C3', bg=self.cor_de_fundo_menu,
                                    command=self.clickHorarioAlimentacao, compound='top')

        self.btnHorario.grid(column=4, row=0, padx=10, pady=10)

    def clickItem(self):
        Consulta_Item()

    def clickFornecedor(self):
        Consulta_Fornecedor()

    def clickAjusteItens(self):
        Consulta_Ajuste_Item()
    def clickCompra(self):
        Consulta_Compra()
    def clickHorarioAlimentacao(self):
        Consulta_Horario_Alimentacao()
        pass

    def clickAjusteTanque(self):
        Consulta_Ajuste_Tanque()

    def clickColheita(self):
       Consulta_Colheita()

    def clickTanque(self):
        Consulta_Tanque()
        pass
    def clickEntradaPeixe(self):
        Consulta_Entrada_Peixe()

Menu_principal().window.mainloop()

