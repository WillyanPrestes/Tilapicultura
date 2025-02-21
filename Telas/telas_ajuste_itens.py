from tkinter import Toplevel, Label, Spinbox, Entry, DISABLED, messagebox, Button, PhotoImage, CENTER, NSEW, END, Tk
from tkinter.ttk import *
from Classes.ajusteitem import AjusteItem
from Classes.item import Item
from Telas.Modulos import FuncoesAuxiliares, MenuSuperiorSalvar, MenuSuperiorConsulta, MenuInferiorConsulta
from Telas.telas_itens import Seleciona_Item


class Cadastro_Ajuste_Item:
    def __init__(self,tela:Tk, ajuste_item=AjusteItem()):
        self.window = Toplevel()
        self.telaAnterior = tela
        self.ajuste_item = ajuste_item
        self.window.geometry('620x320')
        self.window.style = FuncoesAuxiliares().style
        self.window.transient(tela)  # Marca como a janela anterior
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()
        self.window.title("Cadastro Ajuste Item")
        tamanhofonte = 12

        self.menuSuperior = MenuSuperiorSalvar(self.window, 'blue')

        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)

        self.lbldescricao = Label(self.window, text="Descrição")
        self.lbldescricao.grid(column=0, row=1, sticky='EW')
        self.txtdescricao = Entry(self.window, style='TEntry', font=('calibri', tamanhofonte, 'normal'))
        self.txtdescricao.grid(column=0, row=2, columnspan=5, sticky='EW', padx=(10, 5))
        self.txtdescricao.insert(0, ajuste_item.get_descricao())

        self.lblitem = Label(self.window, text="Item")
        self.lblitem.grid(column=0, row=3, columnspan=2, sticky='EW')
        self.txtitem = Entry(self.window, style='TEntry', font=('calibri', tamanhofonte, 'normal'))
        self.txtitem.grid(column=0, row=4, columnspan=2, sticky='EW', padx=(10, 5))
        self.txtitem.insert(0, ajuste_item.get_item().dados_principais())
        self.btnbuscar = Button(self.window, text="Buscar")
        self.btnbuscar.grid(column=2, row=4, pady=5)
        self.btnbuscar.config(command=self.clickBuscar)

        self.lblqtdAnterior = Label(self.window, text="Qtd Atual")
        self.lblqtdAnterior.grid(row=5, sticky='EW')
        self.numqtdAnterior = Spinbox(self.window, from_=0, to=100000)
        self.numqtdAnterior.insert(10, ajuste_item.get_qtd_atual())
        self.numqtdAnterior.grid(row=6, sticky='EW', padx=(10, 5))


        self.lblqtdMovimentacao = Label(self.window, text="Qtd Movimentação",font=('calibri', 12, 'bold'))
        self.lblqtdMovimentacao.grid(row=5, column=1, sticky='EW')
        self.numqtdMovimentacao = Spinbox(self.window, from_=-100000, to=100000,command=self.fazMovimentacao)
        self.numqtdMovimentacao.insert(10, ajuste_item.get_qtd_movimentacao())
        self.numqtdMovimentacao.grid(row=6, column=1,sticky='EW', padx=(10, 5))

        self.lblqtdNova = Label(self.window, text="Qtd Nova")
        self.lblqtdNova.grid(row=5, column=2, sticky='EW')
        self.numqtdNova = Spinbox(self.window, from_=0, to=100000)
        self.numqtdNova.insert(10, ajuste_item.get_qtd_nova())
        self.numqtdNova.grid(row=6, column=2, sticky='EW', padx=(10, 5))

        self.menuSuperior.btnSalvar.config(command=self.clickSalvar)
        self.bloqueia_para_edicao()

        self.numqtdNova.config(state='disable')
        self.numqtdAnterior.config(state='disable')

    def fazMovimentacao(self):
        if self.ajuste_item.get_id_ajuste() <=0:
            nova = self.ajuste_item.get_item().get_qtd() + int(self.numqtdMovimentacao.get())
            self.numqtdNova.config(state='normal')
            self.numqtdNova.delete(0, 'end')  # Limpa o conteúdo atual do campo
            self.numqtdNova.insert(0, str(nova))
            self.numqtdNova.config(state='disable')

    def bloqueia_para_edicao(self):
        if self.ajuste_item.get_id_ajuste() > 0:
            self.txtdescricao.config(state=DISABLED)
            self.numqtdNova.config(state=DISABLED)
            self.numqtdAnterior.config(state=DISABLED)
            self.numqtdMovimentacao.config(state=DISABLED)
            self.btnbuscar.config(state=DISABLED)
            self.menuSuperior.btnSalvar.config(state=DISABLED)
            self.txtitem.config(state=DISABLED)
    def clickSalvar(self):
        try:
            qtdAnterior = int(self.numqtdAnterior.get())
            qtdMovimentacao = int(self.numqtdMovimentacao.get())

            self.ajuste_item.set_descricao(str(self.txtdescricao.get()))
            self.ajuste_item.set_qtd_nova(qtdAnterior+qtdMovimentacao)
            self.ajuste_item.set_qtd_atual(qtdAnterior)
            self.ajuste_item.set_qtd_movimentacao(qtdMovimentacao)
            message = self.ajuste_item.salvar()
            if (str(message) != ""):
                messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(message))
                self.window.focus_force()
            else:
                messagebox.showinfo('Salvo', "Salvo com sucesso")
                self.telaAnterior.focus_force()
                self.window.destroy()
        except Exception as erro:
            messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(erro))
            self.window.focus_force()

    def clickBuscar(self):
        item = Item()
        self.sel = Seleciona_Item(self.ajuste_item.get_item())
        self.sel.menuSuperior.btnConfirmar.config(command=self.clickConfirmarItem)

    def clickConfirmarItem(self):
        selected_item = self.sel.tree.focus()
        if selected_item != '':
            details = self.sel.tree.item(selected_item)
            self.ajuste_item.set_id_item(int(details.get("values")[0]))
            self.ajuste_item.set_item(Item().listar(" WHERE IdItem =" + str(self.ajuste_item.get_id_item()))[0])

            print(self.ajuste_item.get_item().dados_principais())
            self.alterar_valor(self.ajuste_item.get_item().dados_principais())
            self.sel.window.destroy()

            self.numqtdAnterior.config(state='normal')
            self.numqtdAnterior.delete(0, 'end')  # Limpa o conteúdo atual do campo
            self.numqtdAnterior.insert(0, str(self.ajuste_item.get_item().get_qtd()))
            self.numqtdAnterior.config(state='disable')

            self.numqtdNova.config(state='normal')
            self.numqtdNova.delete(0, 'end')  # Limpa o conteúdo atual do campo
            self.numqtdNova.insert(0, str(self.ajuste_item.get_item().get_qtd()))
            self.numqtdNova.config(state='disable')
    def alterar_valor(self, message: str):
        self.txtitem.config(state='normal')  # Muda para o estado normal para alterar o valor
        self.txtitem.delete(0, 'end')  # Limpa o conteúdo atual do campo
        self.txtitem.insert(0, message)  # Insere um novo texto no campo
        self.txtitem.config(state='readonly')
        

class Consulta_Ajuste_Item:
    def __init__(self, item=()):
        super().__init__()
        self.window = Toplevel()
        self.IdAjuste_Item = 0
        self.itens = item
        self.window.geometry('860x605')
        self.window.resizable(False,False)
        self.window.style = FuncoesAuxiliares().style
        self.window.title("Consulta Ajuste Item")
        tamanhofonte = 12

        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)

        self.menuSuperior = MenuSuperiorConsulta(self.window, 'blue')
        self.menuSuperior.btnNovo.config(command=self.clickNovo)
        self.menuSuperior.btnEditar.config(command=self.clickEditar)
        self.menuSuperior.btnDeletar.config(command=self.clickDeletar)

        self.tree = self.create_tree_widget()

        self.lbldescricao = Label(self.window, text="Descrição")
        self.lbldescricao.grid(column=0, row=2, sticky='SW', padx=(10, 0))
        self.txtdescricao = Entry(self.window, style='TEntry', font=('calibri', tamanhofonte, 'normal'),width=80)
        self.txtdescricao.grid(column=0, row=3, columnspan=2, sticky='SW', padx=(20,0))
        self.txtdescricao.insert(0, "")

        self.photobuscar = PhotoImage(file="Imagens/lupa.png")
        self.photoimageBuscar = self.photobuscar.subsample(2, 2)
        self.btnBuscar = Button(self.window, text="Buscar", image=self.photoimageBuscar, width=20,
                                compound='top', command=self.clickBuscar)
        self.btnBuscar.grid(column=2, row=2, rowspan=2)

        self.menuInferior = MenuInferiorConsulta(self.window, 'blue')
        self.menuInferior.btnLimpar.config(command=self.clickLimpar)
        self.atualizar_tree()

    def clickNovo(self):
       Cadastro_Ajuste_Item(self.window,AjusteItem())

    def clickEditar(self):
        selected_item = self.tree.focus()
        if selected_item != '':
            details = self.tree.item(selected_item)
            Id = int(details.get("values")[0])
            lst = AjusteItem().listar(" WHERE IdAjuste="+ str(Id))
            Cadastro_Ajuste_Item(self.window, lst[0])

        pass
    def clickDeletar(self):
        try:
            selected_item = self.tree.focus()
            if selected_item != '':
                details = self.tree.item(selected_item)
                Id = int(details.get("values")[0])
                it = AjusteItem().listar(" WHERE IdAjuste=" + str(Id))[0]
                msg_box = messagebox.askquestion('Confirma Exclusão',
                                                 'Deseja mesmo Excluir o Item \n '+it.dados_principais()+' ?',
                                                    icon='warning')
                if msg_box == 'yes':
                    strerro = AjusteItem().deletar(int(details.get("values")[0]))
                    if len(strerro) <= 0:
                        self.tree.delete(selected_item)
                    else:
                        messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(strerro))
        except Exception as erro:
            messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(erro))
        finally:
            self.window.focus_force()
    def create_tree_widget(self):
        columns = ('idajuste', 'descricao','Item', 'qtdanterior', 'qtdmovimentacao', 'qtdnova')
        tree = Treeview(self.window, columns=columns, show='headings', height=14)

        # define headings
        tree.heading('idajuste', text='código')
        tree.column('idajuste', width=80, anchor=CENTER)
        tree.heading('descricao', text='Descrição')
        tree.column('descricao', width=220)
        tree.heading('Item', text='Item')
        tree.column('Item', width=210)
        tree.heading('qtdanterior', text='Qtd Anterior')
        tree.column('qtdanterior', width=100, anchor=CENTER)
        tree.heading('qtdmovimentacao', text='Movimentação')
        tree.column('qtdmovimentacao', width=120, anchor=CENTER)
        tree.heading('qtdnova', text='Qtd Nova')
        tree.column('qtdnova', width=100, anchor=CENTER)

        tree.grid(row=1, column=0, columnspan=3, sticky=NSEW, padx=20,pady=10)
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
            string = " Where aj.descricao LIKE '%"+self.txtdescricao.get()+"%'"
            print(string)
        self.itens = AjusteItem().listar(string)
        index = -1
        for i in self.tree.get_children():
            self.tree.delete(i)
        columns = ('idajuste', 'descricao', 'Item', 'qtdanterior', 'qtdmovimentacao', 'qtdnova')
        for it in self.itens:
            self.tree.insert('', index+1, values=(
                        it.get_id_ajuste(),
                        it.get_descricao(),
                        it.get_item().dados_principais(),
                        it.get_qtd_atual(),
                        it.get_qtd_movimentacao(),
                        it.get_qtd_nova()))
    def item_selected(self, event):
        pass

        
#Consulta_Ajuste_Item().window.mainloop()