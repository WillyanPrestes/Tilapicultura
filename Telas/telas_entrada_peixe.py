import datetime

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from Classes.entradapeixe import EntradaPeixe
from Classes.tanques import Tanque
from Telas.Modulos import FuncoesAuxiliares, MenuSuperiorSalvar, MenuSuperiorConsulta, MenuInferiorConsulta
from Telas.telas_tanque import Seleciona_Tanque


class Cadastro_Entrada_Peixe:
    def __init__(self,tk:Tk, entrada =EntradaPeixe()):
        self.telaAnteior=tk
        self.window = Toplevel()
        self.entrada = entrada
        self.window.geometry('610x380')
        self.window.style = Style()
        self.window.title("Cadastro Entrada de Peixes")
        tamanhofonte = 12
        style =FuncoesAuxiliares().style

        self.menuSuperior = MenuSuperiorSalvar(self.window, 'blue')
        self.window.transient(self.telaAnteior)  # Marca como a janela anterior
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()

        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)

        self.lbltanque = Label(self.window, text="Tanque")
        self.lbltanque.grid(column=0, row=1, columnspan=2, sticky='EW')
        self.txttanque = Entry(self.window, style='TEntry', font=('calibri', tamanhofonte, 'normal'))
        self.txttanque.grid(column=0, row=2, columnspan=5, sticky='EW', padx=(10, 0))
        self.alterar_valor(entrada.get_tanque().dados_principais())
        self.btnbuscar = Button(self.window, text="Buscar")
        self.btnbuscar.grid(column=5, row=2, padx=5, pady=5)

        self.lblqtdpeixe = Label(self.window, text="Qtd Peixes")
        self.lblqtdpeixe.grid(row=3, sticky='EW')
        self.numqtdpeixe = Spinbox(self.window, from_=0, to=100000)
        self.numqtdpeixe.insert(10, entrada.get_qtd())
        self.numqtdpeixe.grid(row=4, sticky='EW', padx=(10, 5))


        self.lblData = Label(self.window, text="Data da Colheita")
        self.lblData.grid(row=5, sticky='EW')
        frame_data = Frame(self.window)
        frame_data.grid(row=6, column=0, padx=5, pady=5)

        self.sp_dia = Spinbox(frame_data, from_=1, to=31, width=2)
        self.sp_mes = Spinbox(frame_data, from_=1, to=12, width=2)
        self.sp_ano = Spinbox(frame_data, from_=1900, to=2100, width=4)

        self.sp_dia.insert(0, entrada.get_data_hora().day)
        self.sp_mes.insert(0, entrada.get_data_hora().month)
        self.sp_ano.insert(0, entrada.get_data_hora().year)

        self.sp_dia.grid(row=0, column=0, padx=5)
        self.sp_mes.grid(row=0, column=1, padx=2)
        self.sp_ano.grid(row=0, column=2, padx=2)

        self.menuSuperior.btnSalvar.config(command=self.clickSalvar)
        self.btnbuscar.config(command=self.clickBuscar)
        self.bloqueia_para_edicao()

    def clickSalvar(self):
        message = ''
        try:
            self.entrada.set_qtd(int(self.numqtdpeixe.get()))
            self.entrada.set_data_hora(datetime.date(int(self.sp_ano.get()),
                                                      int(self.sp_mes.get()), int(self.sp_dia.get())))

            message = self.entrada.salvar()
            if (str(message) != ""):
                messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(message))
            else:
                messagebox.showinfo('Salvo', "Salvo com sucesso")
                self.telaAnteior.focus_force()
                self.window.destroy()
        except Exception as erro:
            messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(erro))
        finally:
            pass
            #self.window.focus_force()


    def clickBuscar(self):
        tanque =Tanque()
        self.sel = Seleciona_Tanque(self.window, self.entrada.get_tanque())
        self.sel.menuSuperior.btnConfirmar.config(command=self.clickConfirmarTanque)


    def clickConfirmarTanque(self):
        selected_item = self.sel.tree.focus()
        if selected_item != '':
            details = self.sel.tree.item(selected_item)
            self.entrada.set_id_tanque(int(details.get("values")[0]))
            self.entrada.set_tanque(Tanque().listar(" WHERE IdTanque =" + str(self.entrada.get_id_tanque()))[0])

            print(self.entrada.get_tanque().dados_principais())
            self.alterar_valor(self.entrada.get_tanque().dados_principais())
            self.sel.window.destroy()
    def alterar_valor(self, message:str):
        self.txttanque.config(state='normal')  # Muda para o estado normal para alterar o valor
        self.txttanque.delete(0, 'end')  # Limpa o conteúdo atual do campo
        self.txttanque.insert(0, message)  # Insere um novo texto no campo
        self.txttanque.config(state='readonly')

    def bloqueia_para_edicao(self):
        if self.entrada.get_id_entrada_peixe() > 0:
            self.txttanque.config(state=DISABLED)
            self.numqtdpeixe.config(state=DISABLED)
            self.sp_dia.config(state=DISABLED)
            self.sp_mes.config(state=DISABLED)
            self.btnbuscar.config(state=DISABLED)
            self.menuSuperior.btnSalvar.config(state=DISABLED)
            self.sp_ano.config(state=DISABLED)


class Consulta_Entrada_Peixe:
    def __init__(self, entrada=()):
        super().__init__()
        self.itens = entrada
        self.window = Toplevel()

        print(type(self.window))
        self.window.geometry('860x605')
        self.window.resizable(False,False)
        self.window.style = FuncoesAuxiliares().style
        self.window.title("Consulta Entrada Peixe")

        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)

          # Marca como a janela anterior
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()

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
        self.btnBuscar = Button(self.window, text="Buscar", image=self.photoimageBuscar, width=20,
                                compound='top', command=self.clickBuscar)
        self.btnBuscar.grid(column=7, row=2, rowspan=2)

        self.menuInferior = MenuInferiorConsulta(self.window, 'blue')
        self.menuInferior.btnLimpar.config(command=self.clickLimpar)
        self.atualizar_tree()

    def clickNovo(self):
        Cadastro_Entrada_Peixe(self.window,EntradaPeixe())

    def clickEditar(self):
        selected_item = self.tree.focus()
        if selected_item != '':
            details = self.tree.item(selected_item)
            Id = int(details.get("values")[0])
            lst = EntradaPeixe().listar(" WHERE IdEntradaPeixe=" + str(Id))
            Cadastro_Entrada_Peixe(self.window, lst[0])


    def clickDeletar(self):
        try:
            selected_item = self.tree.focus()
            if selected_item != '':
                details = self.tree.item(selected_item)
                Id = int(details.get("values")[0])
                it = EntradaPeixe().listar(" WHERE IdEntradaPeixe=" + str(Id))[0]
                msg_box = messagebox.askquestion('Confirma Exclusão',
                                                 'Deseja mesmo Excluir o Item \n ' + it.dados_principais() + ' ?',
                                                 icon='warning')
                if msg_box == 'yes':
                    strerro = EntradaPeixe().deletar(int(details.get("values")[0]))
                    if len(strerro) <= 0:
                        self.tree.delete(selected_item)
                    else:
                        messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(strerro))
        except Exception as erro:
            messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(erro))
        finally:
            self.window.focus_force()

    def create_tree_widget(self):
        columns = ('IdEntrada', 'Tanque', 'Data/Hora', 'qtd')
        tree = Treeview(self.window, columns=columns, show='headings', height=14)

        # define headings
        tree.heading('IdEntrada', text='código')
        tree.column('IdEntrada', width=50, anchor=CENTER)
        tree.heading('Tanque', text='Tanque')
        tree.column('Tanque', width=250)
        tree.heading('Data/Hora', text='Data/Hora')
        tree.column('Data/Hora', width=50, anchor=CENTER)
        tree.heading('qtd', text='Qtd Unitária')
        tree.column('qtd', width=80, anchor=CENTER)
        tree.grid(row=1, column=0, columnspan=8, sticky=NSEW, padx=20, pady=10)
        return tree

    def clickBuscar(self):
        self.atualizar_tree()

    def clickLimpar(self):
        self.txtdescricao.delete(0, END)
        self.atualizar_tree()

    def atualizar_tree(self):
        string = ""
        if (self.txtdescricao.get() != ""):
            string = " Where ta.descricao LIKE '%" + self.txtdescricao.get() + "%'"
            print(string)
        self.itens = EntradaPeixe().listar(string)
        index = -1
        for i in self.tree.get_children():
            self.tree.delete(i)

        for it in self.itens:
            self.tree.insert('', index + 1, values=(
                it.get_id_entrada_peixe(),
                it.get_tanque().dados_principais(),
                str(it.get_data_hora()),
                str(it.get_qtd())))


