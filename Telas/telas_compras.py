import re
from tkinter import Tk, Toplevel, Label, Entry, Button, CENTER, NSEW, PhotoImage, END, messagebox
from tkinter.ttk import *


from Classes.compra import Compra
from Classes.compraitem import Compraitem
from Classes.item import Item
from Classes.pessoa import Fornecedor
from Telas.Modulos import FuncoesAuxiliares, MenuSuperiorSalvar, MenuSuperiorConfirmar, MenuInferiorConsulta, \
    MenuSuperiorConsulta
from Telas.telas_fornecedor import Seleciona_Fornecedor
import tkinter as tk
from tkinter import Button
from tkinter.ttk import Style



from Telas.telas_itens import Seleciona_Item


class Seleciona_Item_Qtd:
    def __init__(self,item:Item):
        self.window = Toplevel()
        self.window.resizable(False, False)
        self.window.style = FuncoesAuxiliares().style
        # self.window.transient(tela)  # Marca como a janela anterior
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()
        self.window.title("Seleciona Item")
        self.window.geometry('500x250')
        tamanhofonte = 12
        self.item = item

        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)


        self.menuSuperior = MenuSuperiorConfirmar(self.window, 'blue',50)
        #self.menuSuperior.btnConfirmar.config(command=self.btnConfirmar)

        self.lblNome = Label(self.window, text=item.dados_principais(), font=('calibri', 20, 'bold'))
        self.lblNome.grid(row=1, sticky='EW')

        self.lbltipo = Label(self.window, text="quantidades")
        self.lbltipo.grid(row=2, sticky='EW')
        self.numqtdAnterior = Spinbox(self.window, from_=0, to=100000)
        self.numqtdAnterior.insert(10,'0')
        self.numqtdAnterior.grid(row=3, sticky='EW', padx=(10, 5))


class Cadastro_Compra:
    def __init__(self, tela:Tk, compra=Compra()):
        self.compra = compra
        self.telaAnterior = tela
        self.window = Toplevel()
        self.window.geometry('620x500')
        self.window.resizable(False, False)
        self.window.style = FuncoesAuxiliares().style
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()  # Bloqueia a janela anterior
        self.window.transient(tela)  # Marca como a janela anterior

        self.window.title("Cadastro Compras")
        tamanhofonte = 12
        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)
        self.menuSuperior = MenuSuperiorSalvar(self.window, 'blue')
        self.menuSuperior.btnSalvar.config(command=self.clickSalvar)

        self.lblfornecedor = Label(self.window, text="Fornecedor")
        self.lblfornecedor.grid(column=0, row=1, columnspan=2, sticky='EW')
        self.txtfornecedor = Entry(self.window, style='TEntry', font=('calibri', tamanhofonte, 'normal'),width=35)
        self.txtfornecedor.grid(column=0, row=2, sticky='EW',padx=(10,0) )

        self.btnbuscar = Button(self.window, text="Buscar")
        self.btnbuscar.grid(column=1, row=2, padx=(10,0), pady=5)
        self.btnbuscar.config(command=self.clickBuscar)

        self.lblvalortotal = Label(self.window, text="Valor Total")
        self.lblvalortotal.grid(row=1, column=2, columnspan=4, sticky='EW')
        self.txtvalortotal = Entry(self.window, font=('calibri', tamanhofonte, 'normal'))
        self.txtvalortotal.grid(row=2, column=2, columnspan=7, sticky='EW', padx=(0, 25))
        self.txtvalortotal.insert(0, str(compra.get_valor_total()))

        self.index = 0

        self.tree = self.create_tree_widget()

        self.photoNovo = PhotoImage(file="Imagens/novo.png")
        self.photoNovoImagem = self.photoNovo.subsample(2, 2)
        self.btnNovo = Button(self.window, text="Incluir", image=self.photoNovoImagem, width=270,
                              font=('calibri', 14, 'bold'), fg='#C3C3C3', bg='#2A6ED1',
                              compound='left',command=self.clickNovo)
        self.btnNovo.grid(column=0,columnspan=2, row=4, padx=0, pady=5)

        """self.photoRemover = PhotoImage(file="Imagens/novo.png")
        self.photoRemoverImagem = self.photoRemover.subsample(2, 2)
        self.btnRemover = Button(self.window, text="Remover", image=self.photoRemoverImagem, width=250,
                              font=('calibri', 14, 'bold'), fg='#C3C3C3', bg='#2A6ED1', compound='left')
        self.btnRemover.grid(column=1,columnspan=2, row=4, padx=10, pady=5)"""

        self.atualizar_tree()

        if self.compra.get_id_compra() > 0:
            self.bloqueiaEdicao()


    def clickBuscar(self):
        forne =Fornecedor()
        self.sel = Seleciona_Fornecedor(self.window, self.compra.get_fornecedor())
        self.sel.menuSuperior.btnConfirmar.config(command=self.clickConfirmarFornecedor)

    def clickNovo(self):
        item = Item()
        self.sel = Seleciona_Item(item)
        self.sel.menuSuperior.btnConfirmar.config(command=self.clickConfirmarItem)
    def clickSalvar(self):
        try:
            message = self.compra.Salvar()
            if (str(message) != ""):
                messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(message))
            else:
                messagebox.showinfo('Salvo', "Salvo com sucesso")
                self.telaAnterior.focus_force()
                self.window.destroy()
        except Exception as erro:
            messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(message) + "\n" + str(erro))
            print(str(erro))
        finally:
            self.window.destroy()
    def clickConfirmarItem(self):
        selected_item = self.sel.tree.focus()
        if selected_item != '':
            details = self.sel.tree.item(selected_item)
            itemJaCadastrado = False
            for it in self.compra.get_compra_itens():
                if it.get_id_item() == int(details.get("values")[0]):
                    itemJaCadastrado = True
                    messagebox.showerror('ERRO ! ', 'Esse item já foi cadastrado !')
            if itemJaCadastrado == False:
                item = Item().listar(" WHERE IdItem =" + str(details.get("values")[0]))
                self.telaItem = Seleciona_Item_Qtd(item[0])
                self.telaItem.menuSuperior.btnConfirmar.config(command=self.btnConfirmarQtdItem)

    def btnConfirmarQtdItem(self):
        if int(self.telaItem.numqtdAnterior.get()) > 0:
            compraItem=Compraitem(self.telaItem.item.get_id_item(), 0,
                                  float(self.telaItem.numqtdAnterior.get()) * float(self.telaItem.item.get_preco()),
                                  self.telaItem.numqtdAnterior.get(), self.telaItem.item)
            self.compra.get_compra_itens().append(compraItem)
            self.tree.insert('', self.index + 1, values=(
                compraItem.get_item().get_descricao(),
                compraItem.get_item().get_texto_tipo_item(),
                str(compraItem.get_qtd()),
                'R$ ' + str(compraItem.get_valor())))
            self.alterar_valorTotal()
            self.telaItem.window.destroy()
        #if self.telaItem.

    def clickConfirmarFornecedor(self):
        selected_item = self.sel.tree.focus()
        if selected_item != '':
            details = self.sel.tree.item(selected_item)
            self.compra.set_id_fornecedor(int(details.get("values")[0]))
            forne = Fornecedor().Buscar(" WHERE IdPessoa =" + str(self.compra.get_id_fornecedor()))
            self.compra.set_fornecedor(forne)

            print(self.compra.get_fornecedor().get_pessoa().dados_principais())
            self.alterar_valor(self.compra.get_fornecedor().get_pessoa().dados_principais())
            self.sel.window.destroy()

    def alterar_valorTotal(self):
        valorTotal = 0
        for it in self.compra.get_compra_itens():
            valorTotal += it.get_valor()
        self.compra.set_valor_total(valorTotal)
        self.txtvalortotal.config(state='normal')  # Muda para o estado normal para alterar o valor
        self.txtvalortotal.delete(0, 'end')  # Limpa o conteúdo atual do campo
        self.txtvalortotal.insert(0, str(valorTotal))  # Insere um novo texto no campo
        self.txtvalortotal.config(state='readonly')

    def alterar_valor(self, message:str):
        self.txtfornecedor.config(state='normal')  # Muda para o estado normal para alterar o valor
        self.txtfornecedor.delete(0, 'end')  # Limpa o conteúdo atual do campo
        self.txtfornecedor.insert(0, message)  # Insere um novo texto no campo
        self.txtfornecedor.config(state='readonly')

    def create_tree_widget(self):
        columns = ('descricao','tipo','qtd', 'valor')
        tree = Treeview(self.window, columns=columns, show='headings', height=10)

        # define headings
        tree.heading('descricao', text='Descrição')
        tree.column('descricao', width=220)
        tree.heading('tipo', text='Tipo')
        tree.column('tipo', width=160, anchor=CENTER)
        tree.heading('qtd', text='Qtd')
        tree.column('qtd', width=60, anchor=CENTER)
        tree.heading('valor', text='Valor total'.format("R$ 0.000"))
        tree.column('valor', width=150, anchor=CENTER)
        tree.grid(row=3, column=0, columnspan=3, sticky=NSEW, padx=10,pady=10)
        tree.bind('<<TreeviewSelect>>', self.item_selected)
        return tree

    def atualizar_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        index =0

        for it in self.compra.get_compra_itens():
            if type(it) is Compraitem:
                self.tree.insert('', index + 1, values=(
                    it.get_item().get_descricao(),
                    it.get_item().get_texto_tipo_item(),
                    str(it.get_qtd()),
                    'R$ ' + str(it.get_valor())))
                index= index+1

    def bloqueiaEdicao(self):
        self.alterar_valor(self.compra.get_fornecedor().dadosPrincipais())
        self.txtvalortotal.config(state='readonly')
        self.btnbuscar.config(state='disabled')
        #self.btnRemover.config(state='disabled')
        self.btnNovo.config(state='disabled')
        self.menuSuperior.btnSalvar.config(state='disabled')
        self.menuSuperior.detalhae()
        self.menuSuperior.btnSalvar.config(command=self.btnExportar)

    def btnExportar(self):
        self.compra.Gerar_pdf()
    def item_selected(self, event):
        pass


class Consulta_Compra:
    def __init__(self, colheita=()):
        super().__init__()
        self.itens = []
        self.window = Toplevel()

        print(type(self.window))
        self.window.geometry('860x605')
        self.window.resizable(False,False)
        self.window.style = FuncoesAuxiliares().style
        self.window.title("Consulta Compra")

        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)

        tamanhofonte = 12
        self.menuSuperior = MenuSuperiorConsulta(self.window, 'blue')
        self.menuSuperior.btnNovo.config(command=self.clickNovo)
        self.menuSuperior.btnEditar.config(command=self.clickEditar)
        self.menuSuperior.btnDeletar.config(command=self.clickDeletar)

        self.tree = self.create_tree_widget()

        self.lbldescricao = Label(self.window, text="Descrição")
        self.lbldescricao.grid(column=0, row=2, sticky='EW', padx=(10, 0))
        self.txtdescricao = Entry(self.window, style='TEntry', font=('calibri', tamanhofonte, 'normal'))
        self.txtdescricao.grid(column=0, row=3, columnspan=7, sticky='EW', padx=(20, 0))
        self.txtdescricao.insert(0, "")

        self.photobuscar = PhotoImage(file="Imagens/lupa.png")
        self.photoimageBuscar = self.photobuscar.subsample(2, 2)
        self.btnBuscar = Button(self.window, text="Buscar", image=self.photoimageBuscar, width=40,
                                compound='top', command=self.clickBuscar)
        self.btnBuscar.grid(column=7, row=2, rowspan=2)

        self.menuInferior = MenuInferiorConsulta(self.window, 'blue')
        self.menuInferior.btnLimpar.config(command=self.clickLimpar)
        self.atualizar_tree()

    def clickNovo(self):
        Cadastro_Compra(self.window,Compra())

    def clickEditar(self):
        selected_item = self.tree.focus()
        if selected_item != '':
            details = self.tree.item(selected_item)
            Id = int(details.get("values")[0])
            lst = Compra().Buscar(Id)
            Cadastro_Compra(self.window,lst)

    def clickDeletar(self):
        try:
            selected_item = self.tree.focus()
            if selected_item != '':
                details = self.tree.item(selected_item)
                Id = int(details.get("values")[0])
                it = Compra().Listar(" WHERE IdCompra=" + str(Id))[0]
                msg_box = messagebox.askquestion('Confirma Exclusão',
                                                 'Deseja mesmo Excluir o Item \n ' + it.dados_principais() + ' ?')
                if msg_box:
                    strerro = it.Deletar()
                    if len(strerro) <= 0:
                        self.tree.delete(selected_item)
                    else:
                        messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(strerro))
        except Exception as erro:
            messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(erro))
        finally:
            self.window.focus_force()

    def create_tree_widget(self):
        columns = ('IdCompra', 'Fornecedor', 'ValorTotal')
        tree = Treeview(self.window, columns=columns, show='headings', height=14)

        # define headings
        tree.heading('IdCompra', text='código')
        tree.column('IdCompra', width=50, anchor=CENTER)
        tree.heading('Fornecedor', text='Fornecedor')
        tree.column('Fornecedor', width=500)
        tree.heading('ValorTotal', text='Valor Total')
        tree.column('ValorTotal', width=100, anchor=CENTER)
        tree.grid(row=1, column=0, columnspan=8, sticky=NSEW, padx=20, pady=10)
        return tree

    def clickBuscar(self):
        self.atualizar_tree()

    def clickLimpar(self):
        self.txtdescricao.delete(0, END)
        self.atualizar_tree()

    def atualizar_tree(self):

        for i in self.tree.get_children():
            self.tree.delete(i)

        string = ""
        self.itens=[]
        if (self.txtdescricao.get() != ""):
            string = " Where ta.descricao LIKE '%" + self.txtdescricao.get() + "%'"
            print(string)
        #self.itens = Compra().Listar()
        for it in Compra().Listar(""):
            if type(it) is Compra:
                if re.search(self.txtdescricao.get(),it.get_fornecedor().dadosPrincipais()):
                    self.itens.append(it)

        index = -1
        for i in self.tree.get_children():
            self.tree.delete(i)

        for it in self.itens:
            self.tree.insert('', index + 1, values=(
                it.get_id_compra(),
                it.get_fornecedor().dadosPrincipais(),
                "R$ " + str(it.get_valor_total())))


#Consulta_Compra().window.mainloop()