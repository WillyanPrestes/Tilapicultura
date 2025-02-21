from tkinter import *
from tkinter.ttk import *

from tkinter import messagebox

from Classes.tanques import Tanque
from Telas import Modulos
from Telas.Modulos import MenuSuperiorSalvar, FuncoesAuxiliares, MenuSuperiorConsulta, MenuInferiorConsulta, \
    MenuSuperiorConfirmar


class Consulta_Tanque:
    def __init__(self, item=()):
        self.IdTanque = 0
        self.itens = item
        self.window = Toplevel()
        self.window.geometry('860x605')
        #self.window.resizable(False,False)
        self.window.style = FuncoesAuxiliares().style
        self.window.title("Consulta Tanques")
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
        self.atualizar_tree()

        self.menuInferior.btnExportar.config(state='normal', command=self.clickExportar)

    def clickExportar(self):
        Tanque().Gerar_pdf(self.itens)
    def clickNovo(self):
       Cadastro_Tanque(self.window,Tanque())

    def clickEditar(self):
        selected_item = self.tree.focus()
        if selected_item != '':
            details = self.tree.item(selected_item)
            Id = int(details.get("values")[0])
            lst = Tanque().listar(" WHERE IdTanque="+ str(Id))
            Cadastro_Tanque(self.window, lst[0])

        pass
    def clickDeletar(self):
        try:
            selected_item = self.tree.focus()
            if selected_item != '':
                details = self.tree.item(selected_item)
                Id = int(details.get("values")[0])
                it = Tanque().listar(" WHERE IdTanque=" + str(Id))[0]
                msg_box = messagebox.askquestion('Confirma Exclusão',
                                                 'Deseja mesmo Excluir o Item \n '+it.dados_principais()+' ?',
                                                    icon='warning')
                if msg_box == 'yes':
                    strerro =Tanque().deletar(int(details.get("values")[0]))
                    if len(strerro) <=0:
                        self.tree.delete(selected_item)
                    else:
                        messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(strerro))
        except Exception as erro:
            messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(erro))
        finally:
            self.window.focus_force()
    def create_tree_widget(self):
        columns = ('IdItem', 'descricao', 'qtdPeixe', 'ph', 'temperatura','volume','fase_desenvolvimento')
        tree = Treeview(self.window, columns=columns, show='headings', height=14)

        # define headings
        tree.heading('IdItem', text='código')
        tree.column('IdItem', width=50, anchor=CENTER)
        tree.heading('descricao', text='Descrição')
        tree.column('descricao', width=200)
        tree.heading('qtdPeixe', text='Quantidade')
        tree.column('qtdPeixe', width=50, anchor=CENTER)
        tree.heading('ph', text='PH')
        tree.column('ph', width=50, anchor=CENTER)
        tree.heading('temperatura', text='Temperatura')
        tree.column('temperatura', width=50, anchor=CENTER)
        tree.heading('volume', text='Volume')
        tree.column('volume', width=50, anchor=CENTER)
        tree.heading('fase_desenvolvimento', text='Fase desen.')
        tree.column('fase_desenvolvimento', width=50, anchor=CENTER)

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
        self.itens = Tanque().listar(string)
        index = -1
        for i in self.tree.get_children():
            self.tree.delete(i)

        for it in self.itens:
            self.tree.insert('', index+1, values=(
                        it.get_id_tanque(),
                        it.get_descricao(),
                        it.get_qtd_peixe(),
                        it.get_ph(),
                        it.get_temperatura(),
                        it.get_volume(),
                        it.texto_fase_desenvolvimento()))
    def item_selected(self, event):
        pass


class Cadastro_Tanque:
    def __init__(self, tela: Tk, tanque=Tanque()):
        self.telaAnterior = tela
        self.tanque = tanque
        self.window = Toplevel()
        self.window.geometry('620x320')
        self.window.resizable(False, False)
        self.window.style = FuncoesAuxiliares().style
        self.window.transient(tela)  # Marca como a janela anterior
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()  # Bloqueia a janela anterior

        self.window.title("Cadastro Tanque")
        tamanhofonte = 12
        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)
        self.menuSuperior = MenuSuperiorSalvar(self.window, 'blue')



        self.lbldescricao = Label(self.window,  text="Descrição")
        self.lbldescricao.grid(column=0, row=1, sticky='EW')
        self.txtdescricao = Entry(self.window, style='TEntry', font=('calibri', tamanhofonte, 'normal'))
        self.txtdescricao.grid(column=0, row=2, columnspan=5, sticky='EW', padx=(10, 5))
        self.txtdescricao.insert(0, tanque.get_descricao())

        self.lblqtdpeixe = Label(self.window, text="Qtd Peixes")
        self.lblqtdpeixe.grid(row=3, sticky='EW')
        self.numqtdpeixe = Spinbox(self.window, from_=0, to=100000)
        self.numqtdpeixe.insert(10,tanque.get_qtd_peixe())
        self.numqtdpeixe.grid(row=4, sticky='EW', padx=(10, 5))

        self.lbltemperatura = Label(self.window, text="Temperatura (Cº)")
        self.lbltemperatura.grid(row=3, column=1, sticky='EW')
        self.txttemperatura = Entry(self.window, font=('calibri', tamanhofonte, 'normal'))
        self.txttemperatura.grid(row=4, column=1, sticky='EW', padx=(10, 5))
        self.txttemperatura.insert(0,tanque.get_temperatura())

        self.lblph = Label(self.window, text="PH")
        self.lblph.grid(row=3, column=2, sticky='EW')
        self.txtph = Entry(self.window, width=15, font=('calibri', tamanhofonte, 'normal'))
        self.txtph.grid(row=4, column=2, sticky='EW', padx=(10, 5))
        self.txtph.insert(0,tanque.get_ph())

        self.lblvolume = Label(self.window, text="Volume (mt³)")
        self.lblvolume.grid(row=5, column=0, sticky='EW')
        self.txtvolume = Entry(self.window, font=('calibri', tamanhofonte, 'normal'))
        self.txtvolume.grid(row=6, column=0, sticky='EW', padx=(10, 5))
        self.txtvolume.insert(0,tanque.get_volume())

        self.lblfasedesenvolvimento = Label(self.window, text="Fase Desenvolvimento")
        self.lblfasedesenvolvimento.grid(row=5, column=1, sticky='EW')
        self.combofase = Combobox(self.window, font=('calibri', tamanhofonte, 'normal'))
        self.combofase['values'] = ("Alevino", "Juvenil", "Adulto")
        self.combofase.current(tanque.get_fase_desenvolvimento())
        self.combofase.grid(row=6, column=1, sticky='EW', padx=(10, 5))

        self.menuSuperior.btnSalvar.config(command=self.clickSalvar)
        self.bloqueia_para_edicao()

    def bloqueia_para_edicao(self):
        if self.tanque.get_id_tanque() > 0:
            self.numqtdpeixe.config(state=DISABLED)
    def clickSalvar(self):
        message = ''
        try:
            self.tanque.set_descricao(self.txtdescricao.get())
            self.tanque.set_ph(float(self.txtph.get()))
            self.tanque.set_volume(float(self.txtvolume.get()))
            self.tanque.set_temperatura(float(self.txttemperatura.get()))
            self.tanque.set_qtd_peixe(int(self.numqtdpeixe.get()))
            self.tanque.set_fase_desenvolvimento(int(self.combofase.current()))

            message = self.tanque.salvar()

            if(str(message)!=""):
                messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(message))
            else:
                messagebox.showinfo('Salvo', "Salvo com sucesso")
                self.telaAnterior.focus_force()
                self.window.destroy()
        except Exception as erro:
            messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(message) + "\n" + str(erro))
            print(str(erro))


class Seleciona_Tanque:
    def __init__(self, tela,cadastro_colheita, item=()):
        super().__init__()
        self.item = Tanque()
        self.cadastro_colheita = cadastro_colheita
        self.itens = item
        self.window = Toplevel()
        self.window.geometry('860x605')
        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)
        self.window.style = FuncoesAuxiliares().style
        self.window.title("Seleciona Tanque")
        self.window.transient(tela)  # Marca como a janela anterior
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()

        tamanhofonte = 12

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
        columns = ('IdItem','descricao', 'qtdPeixe', 'ph', 'temperatura','volume','fase_desenvolvimento')
        tree = Treeview(self.window, columns=columns, show='headings', height=14)

        # define headings
        tree.heading('IdItem', text='código')
        tree.column('IdItem', width=50, anchor=CENTER)
        tree.heading('descricao', text='Descrição')
        tree.column('descricao', width=300)
        tree.heading('qtdPeixe', text='Quantidade')
        tree.column('qtdPeixe', width=50, anchor=CENTER)
        tree.heading('ph', text='PH')
        tree.column('ph', width=50, anchor=CENTER)
        tree.heading('temperatura', text='Temperatura')
        tree.column('temperatura', width=50, anchor=CENTER)
        tree.heading('volume', text='Volume')
        tree.column('volume', width=50, anchor=CENTER)
        tree.heading('fase_desenvolvimento', text='Fase desen.')
        tree.column('fase_desenvolvimento', width=50, anchor=CENTER)

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
        self.itens = Tanque().listar(string)
        index = -1
        for i in self.tree.get_children():
            self.tree.delete(i)

        for it in self.itens:
            self.tree.insert('', index+1, values=(
                        it.get_id_tanque(),
                        it.get_descricao(),
                        it.get_qtd_peixe(),
                        it.get_ph(),
                        it.get_temperatura(),
                        it.get_volume(),
                        it.texto_fase_desenvolvimento()))
    def item_selected(self, event):
        pass


#Cadastro_Tanque(Tk()).window,mainloop()
