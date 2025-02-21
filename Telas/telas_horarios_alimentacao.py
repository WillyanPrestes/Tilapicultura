
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from Classes.horarioalimentacao import Horario_Alimentacao
from Classes.tanques import Tanque
from Telas.Modulos import FuncoesAuxiliares, MenuSuperiorSalvar, MenuSuperiorConsulta, MenuInferiorConsulta
from Telas.telas_tanque import Seleciona_Tanque


class Cadastro_Horario_Alimentacao:
    def __init__(self,tela:Tk,  horario_alimentacao=Horario_Alimentacao()):
        self.telaAnterior = tela
        self.window = Toplevel()
        self.horario_alimentacao = horario_alimentacao
        self.window.geometry('620x320')
        self.window.style = FuncoesAuxiliares().style
        self.window.title("Cadastro Hórario Alimentação")
        tamanhofonte = 12
        self.window.transient(tela)  # Marca como a janela anterior
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()

        self.menuSuperior = MenuSuperiorSalvar(self.window, 'blue')

        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)

        self.lbldescricao = Label(self.window, text="Descrição")
        self.lbldescricao.grid(column=0, row=1, sticky='EW')
        self.txtdescricao = Entry(self.window, style='TEntry', font=('calibri', tamanhofonte, 'normal'), width=60)
        self.txtdescricao.grid(column=0, row=2, columnspan=2, sticky='EW', padx=(10, 5))
        self.txtdescricao.insert(0, horario_alimentacao.get_descricao())

        self.lbltanque = Label(self.window, text="Tanque")
        self.lbltanque.grid(column=0, row=3, columnspan=2, sticky='EW')
        self.txttanque = Entry(self.window, style='TEntry', font=('calibri', tamanhofonte, 'normal'))
        self.txttanque.grid(column=0, row=4, columnspan=2, sticky='EW', padx=(10, 5))
        self.txttanque.insert(0, horario_alimentacao.get_tanque().get_descricao())
        self.btnbuscar = Button(self.window, text="Buscar")
        self.btnbuscar.grid(column=2, row=4, pady=5)
        self.btnbuscar.config(command=self.clickBuscar)

        self.lblData = Label(self.window, text="Horas e minutos")
        self.lblData.grid(row=5, sticky='EW')
        frame_data = Frame(self.window)
        frame_data.grid(row=6, column=0, padx=(15,380), pady=5)

        self.sp_hour = Spinbox(frame_data, from_=1, to=31, width=2)
        self.sp_minute = Spinbox(frame_data, from_=1, to=12, width=2)

        self.sp_hour.insert(0, horario_alimentacao.get_data_hora().hour)
        self.sp_minute.insert(0, horario_alimentacao.get_data_hora().minute)

        self.sp_hour.grid(row=0, column=0, padx=5)
        self.sp_minute.grid(row=0, column=1, padx=10)

        self.menuSuperior.btnSalvar.config(command=self.clickSalvar)
        self.btnbuscar.config(command=self.clickBuscar)

    def clickSalvar(self):
        try:
            dataa = datetime.now()
            dataa.replace(hour=int(self.sp_hour.get()), minute=int(self.sp_minute.get()))
            self.horario_alimentacao.set_descricao(str(self.txtdescricao.get()))
            self.horario_alimentacao.set_data_hora(dataa)

            message = self.horario_alimentacao.salvar()
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
        horario_alimentacao = Horario_Alimentacao()
        self.sel = Seleciona_Tanque(self.window, self.horario_alimentacao.get_tanque())
        self.sel.menuSuperior.btnConfirmar.config(command=self.clickConfirmarTanque)

    def clickConfirmarTanque(self):
        selected_item = self.sel.tree.focus()
        if selected_item != '':
            details = self.sel.tree.item(selected_item)
            self.horario_alimentacao.set_id_tanque(int(details.get("values")[0]))
            self.horario_alimentacao.set_tanque(Tanque().listar(" WHERE IdTanque =" + str(self.horario_alimentacao.get_id_tanque()))[0])

            print(self.horario_alimentacao.get_tanque().dados_principais())
            self.alterar_valor(self.horario_alimentacao.get_tanque().dados_principais())
            self.sel.window.destroy()

    def alterar_valor(self, message: str):
        self.txttanque.config(state='normal')  # Muda para o estado normal para alterar o valor
        self.txttanque.delete(0, 'end')  # Limpa o conteúdo atual do campo
        self.txttanque.insert(0, message)  # Insere um novo texto no campo
        self.txttanque.config(state='readonly')


class Consulta_Horario_Alimentacao:
    def __init__(self, horario_alimentacao=()):
        super().__init__()
        self.itens = horario_alimentacao
        self.window = Toplevel()
        print(type(self.window))
        self.window.geometry('860x605')
        self.window.resizable(False,False)
        self.window.style = FuncoesAuxiliares().style
        self.window.title("Consulta Horário Alimentação")

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
        self.btnBuscar = Button(self.window, text="Buscar", image=self.photoimageBuscar, width=20,
                                compound='top', command=self.clickBuscar)
        self.btnBuscar.grid(column=7, row=2, rowspan=2)

        self.menuInferior = MenuInferiorConsulta(self.window, 'blue')
        self.menuInferior.btnLimpar.config(command=self.clickLimpar)
        self.atualizar_tree()

    def clickNovo(self):
        Cadastro_Horario_Alimentacao(self.window)

    def clickEditar(self):
        selected_item = self.tree.focus()
        if selected_item != '':
            details = self.tree.item(selected_item)
            Id = int(details.get("values")[0])
            lst = Horario_Alimentacao().listar(" WHERE IdHorario=" + str(Id))
            Cadastro_Horario_Alimentacao(self.window, lst[0])


    def clickDeletar(self):
        try:
            selected_item = self.tree.focus()
            if selected_item != '':
                details = self.tree.item(selected_item)
                Id = int(details.get("values")[0])
                it = Horario_Alimentacao().listar(" WHERE IdHorario=" + str(Id))[0]
                msg_box = messagebox.askquestion('Confirma Exclusão',
                                                 'Deseja mesmo Excluir o Item \n ' + it.dados_principais() + ' ?',
                                                 icon='warning')
                if msg_box == 'yes':
                    strerro = Horario_Alimentacao().deletar(int(details.get("values")[0]))
                    if len(strerro) <= 0:
                        self.tree.delete(selected_item)
                    else:
                        messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(strerro))
        except Exception as erro:
            messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(erro))
        finally:
            self.window.focus_force()

    def create_tree_widget(self):
        columns = ('IdHorario','Descricao', 'Tanque', 'Hora/minuto')
        tree = Treeview(self.window, columns=columns, show='headings', height=14)

        # define headings
        tree.heading('IdHorario', text='código')
        tree.column('IdHorario', width=50, anchor=CENTER)
        tree.heading('Descricao', text='Descrição')
        tree.column('Descricao', width=250)
        tree.heading('Tanque', text='Tanque')
        tree.column('Tanque', width=250, anchor=CENTER)
        tree.heading('Hora/minuto', text='Hora/minuto')
        tree.column('Hora/minuto', width=80, anchor=CENTER)
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
            string = " Where hor.descricao LIKE '%" + self.txtdescricao.get() + "%'"
            print(string)
        self.itens = Horario_Alimentacao().listar(string)
        index = -1
        for i in self.tree.get_children():
            self.tree.delete(i)

        for it in self.itens:
            self.tree.insert('', index + 1, values=(
                it.get_id_horario(),
                it.get_descricao(),
                it.get_tanque().dados_principais(),
                str(it.get_data_hora().hour)+ ":" +str(it.get_data_hora().minute)))


#Consulta_Horario_Alimentacao().window.mainloop()