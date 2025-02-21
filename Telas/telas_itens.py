from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


from Classes.item import Item
from Telas.Modulos import MenuSuperiorConsulta, MenuInferiorConsulta, FuncoesAuxiliares, MenuSuperiorSalvar, \
    MenuSuperiorConfirmar


#from Telas.telas_colheita import *


class Consulta_Item:
    def __init__(self, item=()):
        super().__init__()
        self.itens = item
        self.window = Toplevel()
        self.window.geometry('860x605')
        self.window.resizable(False,False)
        self.window.style = FuncoesAuxiliares().style
        self.window.title("Consulta Item")
        tamanhofonte = 12

        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)

        self.menuSuperior = MenuSuperiorConsulta(self.window, 'blue')
        self.menuSuperior.btnNovo.config(command=self.clickNovo)
        self.menuSuperior.btnEditar.config(command=self.clickEditar)
        self.menuSuperior.btnDeletar.config(command=self.clickDeletar)

        self.tree = self.create_tree_widget()

        self.lbldescricao = Label(self.window, text="Descrição")
        self.lbldescricao.grid(column=0, row=2, sticky='EW', padx=(10, 0))
        self.txtdescricao = Entry(self.window, style='TEntry', font=('calibri', tamanhofonte, 'normal'))
        self.txtdescricao.grid(column=0, row=3, columnspan=7, sticky='EW', padx=(20,0))
        self.txtdescricao.insert(0, "")

        self.photobuscar = PhotoImage(file="Imagens/lupa.png")
        self.photoimageBuscar = self.photobuscar.subsample(2, 2)
        self.btnBuscar = Button(self.window, text="Buscar", image=self.photoimageBuscar, width=20,
                                compound='top', command=self.clickBuscar)
        self.btnBuscar.grid(column=7, row=2, rowspan=2)

        self.menuInferior = MenuInferiorConsulta(self.window, 'blue')
        self.menuInferior.btnLimpar.config(command=self.clickLimpar)
        self.menuInferior.btnExportar.config(state='normal', command=self.clickExportar)
        self.atualizar_tree()

    def clickExportar(self):
        Item().Gerar_pdf(self.itens)

    def clickNovo(self):
        Cadastro_Item(self.window, Item())

    def clickEditar(self):
        selected_item = self.tree.focus()
        if selected_item != '':
            details = self.tree.item(selected_item)
            Id = int(details.get("values")[0])
            lst = Item().listar(" WHERE IdItem="+ str(Id))
            Cadastro_Item(self.window,lst[0])

        pass
    def clickDeletar(self):
        try:
            selected_item = self.tree.focus()
            if selected_item != '':
                details = self.tree.item(selected_item)
                Id = int(details.get("values")[0])
                it = Item().listar(" WHERE IdItem=" + str(Id))[0]
                msg_box = messagebox.askquestion('Confirma Exclusão',
                                                 'Deseja mesmo Excluir o Item \n '+it.dados_principais()+' ?',
                                                    icon='warning')
                if msg_box == 'yes':
                    Item().deletar(int(details.get("values")[0]))
                    self.tree.delete(selected_item)
        except Exception as erro:
            messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(erro))
        finally:
            self.window.focus_force()
    def create_tree_widget(self):
        columns = ('IdItem','descricao','tipo', 'qtd', 'preco')
        tree = Treeview(self.window, columns=columns, show='headings', height=14)

        # define headings
        tree.heading('IdItem', text='código')
        tree.column('IdItem', width=50, anchor=CENTER)
        tree.heading('descricao', text='Descrição')
        tree.column('descricao', width=250)
        tree.heading('tipo', text='Tipo')
        tree.column('tipo', width=90, anchor=CENTER)
        tree.heading('qtd', text='Quantidade')
        tree.column('qtd', width=50, anchor=CENTER)
        tree.heading('preco', text='Preço da Unidade'.format("R$ 0.000"))
        tree.column('preco', width=70, anchor=CENTER)
        tree.grid(row=1, column=0, columnspan=8, sticky=NSEW, padx=20,pady=10)
        tree.bind('<<TreeviewSelect>>', self.item_selected)
        return tree
    def clickBuscar(self):
        self.atualizar_tree()
    def clickLimpar(self):
        self.txtdescricao.delete(0, END)
        self.atualizar_tree()
    def atualizar_tree(self):
        string = ""
        if(self.txtdescricao.get() != ""):
            string = " Where descricao LIKE '%"+self.txtdescricao.get()+"%'"
            print(string)
        self.itens = Item().listar(string)
        index = -1
        for i in self.tree.get_children():
            self.tree.delete(i)

        for it in self.itens:
            self.tree.insert('', index+1, values=(
                        it.get_id_item(),
                        it.get_descricao(),
                        it.get_texto_tipo_item(),
                        it.get_qtd(),
                        'R$ ' + str(it.get_preco())))
    def item_selected(self, event):
        pass


class Cadastro_Item:

    def __init__(self, tela: Tk, item=Item()):
        self.telaAnterior = tela
        self.item = item
        self.window = Toplevel()
        self.window.geometry('620x320')
        self.window.resizable(False, False)
        self.window.style = FuncoesAuxiliares().style
        self.window.transient(tela) #Marca como a janela anterior
        self.window.focus_force() #Marca a janela atual como Focus
        self.window.grab_set() #Bloqueia a janela anterior

        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)

        self.window.title("Cadastro Item")
        tamanhofonte = 12

        self.menuSuperior = MenuSuperiorSalvar(self.window, 'blue')

        self.lbldescricao = Label(self.window, text="Descrição")
        self.lbldescricao.grid(column=0, row=1, sticky='EW')
        self.txtdescricao = Entry(self.window,style='TEntry', font=('calibri', tamanhofonte, 'normal'))
        self.txtdescricao.grid(column=0, row=2, columnspan=7, sticky='EW', padx=(10, 5))
        self.txtdescricao.insert(0, item.get_descricao())

        self.lblqtd = Label(self.window, text="Quantidades")
        self.lblqtd.grid(row=3, sticky='EW')
        self.numqtd = Spinbox(self.window, from_=0, to=100000)
        self.numqtd.insert(10, item.get_qtd())
        self.numqtd.grid(row=4, sticky='EW', padx=(10, 5))
        self.menuSuperior.btnSalvar.config(command=self.btnSalvarClick)

        self.lblpreco = Label(self.window, text="Preço (R$)")
        self.lblpreco.grid(row=3, column=1, sticky='EW')
        self.txtpreco = Entry(self.window, font=('calibri', tamanhofonte, 'normal'))
        self.txtpreco.grid(row=4, column=1, sticky='EW', padx=(10, 5))
        self.txtpreco.insert(0, str(item.get_preco()))

        self.lbltipo = Label(self.window, text="Tipo de Item")
        self.lbltipo.grid(row=5, column=0, sticky='EW')
        self.comboitem = Combobox(self.window, font=('calibri', tamanhofonte, 'normal'))
        self.comboitem['values'] = ("Alimentos", "Manutenção Item", "Veterinário","Outros")
        self.comboitem.current(item.get_tipo())
        self.comboitem.grid(row=6, column=0, sticky='EW', padx=(10, 5))
        self.bloqueia_para_edicao()

    def bloqueia_para_edicao(self):
        if self.item.get_id_item()>0:
            self.numqtd.config(state=DISABLED)
            self.comboitem.config(state=DISABLED)

    def btnSalvarClick(self):
        try:
            self.item.set_descricao(self.txtdescricao.get())
            self.item.set_preco(float(self.txtpreco.get()))
            self.item.set_qtd(int(self.numqtd.get()))
            self.item.set_tipo(int(self.comboitem.current()))
            self.item.salvar()
            messagebox.showinfo('Salvo', "Salvo com sucesso")
            self.window.destroy()
        except Exception as erro:
            messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(erro))


class Seleciona_Item:
    def __init__(self, item=()):
        super().__init__()
        self.item = Item()
        self.itens = item
        self.window = Toplevel()
        self.window.geometry('860x605')
        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)
        self.window.style = FuncoesAuxiliares().style
        self.window.title("Seleciona Item")
        tamanhofonte = 12
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()

        self.menuSuperior = MenuSuperiorConfirmar(self.window, 'blue')


        self.tree = self.create_tree_widget()

        self.lbldescricao = Label(self.window, text="Descrição")
        self.lbldescricao.grid(column=0, row=2, sticky='EW', padx=(10, 0))
        self.txtdescricao = Entry(self.window, style='TEntry', font=('calibri', tamanhofonte, 'normal'))
        self.txtdescricao.grid(column=0, row=3, columnspan=7, sticky='EW', padx=(20,0))
        self.txtdescricao.insert(0, "")

        self.photobuscar = PhotoImage(file="Imagens/lupa.png")
        self.photoimageBuscar = self.photobuscar.subsample(2, 2)
        self.btnBuscar = Button(self.window, text="Buscar", image=self.photoimageBuscar, width=20,
                                compound='top', command=self.clickBuscar)
        self.btnBuscar.grid(column=7, row=2, rowspan=2)

        self.menuInferior = MenuInferiorConsulta(self.window, 'blue')
        self.menuInferior.btnLimpar.config(command=self.clickLimpar)
        self.atualizar_tree()

    def create_tree_widget(self):
        columns = ('IdItem', 'descricao', 'tipo', 'qtd', 'preco')
        tree = Treeview(self.window, columns=columns, show='headings', height=14)

        # define headings
        tree.heading('IdItem', text='código')
        tree.column('IdItem', width=50, anchor=CENTER)
        tree.heading('descricao', text='Descrição')
        tree.column('descricao', width=250)
        tree.heading('tipo', text='Tipo')
        tree.column('tipo', width=90, anchor=CENTER)
        tree.heading('qtd', text='Quantidade')
        tree.column('qtd', width=50, anchor=CENTER)
        tree.heading('preco', text='Preço da Unidade'.format("R$ 0.000"))
        tree.column('preco', width=70, anchor=CENTER)
        tree.grid(row=1, column=0, columnspan=8, sticky=NSEW, padx=20, pady=10)
        tree.bind('<<TreeviewSelect>>', self.item_selected)
        return tree
    def clickBuscar(self):
        self.atualizar_tree()
    def clickLimpar(self):
        self.txtdescricao.delete(0, END)
        self.atualizar_tree()

    def atualizar_tree(self):
        string = ""
        if (self.txtdescricao.get() != ""):
            string = " Where descricao LIKE '%" + self.txtdescricao.get() + "%'"
            print(string)
        self.itens = Item().listar(string)
        index = -1
        for i in self.tree.get_children():
            self.tree.delete(i)

        for it in self.itens:
            self.tree.insert('', index + 1, values=(
                it.get_id_item(),
                it.get_descricao(),
                it.get_texto_tipo_item(),
                it.get_qtd(),
                'R$ ' + str(it.get_preco())))
    def item_selected(self, event):
        pass