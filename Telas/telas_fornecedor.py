from tkinter import Tk, Toplevel, Entry, Label, PhotoImage, CENTER, END, NSEW, messagebox
from tkinter.ttk import *

from Classes.endereco import EstadoFederal, Municipio
from Classes.pessoa import PessoaFisica, Fornecedor, PessoaJuridica
from Telas.Modulos import FuncoesAuxiliares, MenuSuperiorSalvar, MenuSuperiorConsulta, MenuInferiorConsulta, \
    MenuSuperiorConfirmar


class Cadastro_Pessoa_Fisica:
    def __init__(self,tela:Tk, fornecedor=Fornecedor()):
        self.fornecedor = fornecedor
        if type(fornecedor) is PessoaFisica:
            self.fornecedor = Fornecedor(fornecedor.get_id_pessoa(), fornecedor.get_id_pessoa(), fornecedor)


        self.window = Toplevel()
        self.window.geometry('620x560')
        self.window.resizable(False, False)
        self.window.style = FuncoesAuxiliares().style
        self.window.transient(tela)  # Marca como a janela anterior
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()  # Bloqueia a janela anterior

        self.lstEstado = EstadoFederal().listar(" order by uf DESC")
        self.lstMunicipio = []


        self.window.title("Cadastro Fornecedor")
        tamanhofonte = 12
        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)
        self.menuSuperior = MenuSuperiorSalvar(self.window, 'blue')
        self.menuSuperior.btnSalvar.config(command=self.btnSalvar)

        self.nome = Label(self.window, text="Nome")
        self.nome.grid(row=1, column=0, sticky="new", padx=(5,10))

        self.nome_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.nome_entry.grid(row=2, column=0, columnspan=4, sticky="new",  padx=10)
        self.nome_entry.insert(0, self.fornecedor.get_pessoa().get_nome())

        self.apelido = Label(self.window, text="Apelido")
        self.apelido.grid(row=3, column=0, sticky="new",  padx=(5,10))

        self.apelido_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.apelido_entry.grid(row=4, column=0, columnspan=4, sticky="new",  padx=10)
        self.apelido_entry.insert(0, self.fornecedor.get_pessoa().get_apelido())

        self.rg = Label(self.window, text="RG")
        self.rg.grid(row=5, column=0, sticky="new",  padx=(5, 10))

        self.rg_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.rg_entry.grid(row=6, column=0, sticky="new",  padx=10)
        self.rg_entry.insert(0, self.fornecedor.get_pessoa().get_rg())

        self.cpf = Label(self.window, text="CPF")
        self.cpf.grid(row=5, column=1, sticky="new",  padx=(5,10))

        self.cpf_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.cpf_entry.grid(row=6, column=1, sticky="new",  padx=10)
        self.cpf_entry.insert(0, self.fornecedor.get_pessoa().get_cpf())

        self.logradouro = Label(self.window, text="Logradouro")
        self.logradouro.grid(row=7, column=0, sticky="new",  padx=(5,10))

        self.logradouro_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.logradouro_entry.grid(row=8, column=0, sticky="new",  padx=10)
        self.logradouro_entry.insert(0, self.fornecedor.get_pessoa().get_endereco().get_logradouro())

        self.numero = Label(self.window, text="Número")
        self.numero.grid(row=7, column=1, sticky="new",  padx=(5,10))

        self.numero_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.numero_entry.grid(row=8, column=1, sticky="new",  padx=10)
        self.numero_entry.insert(0, self.fornecedor.get_pessoa().get_endereco().get_numero())

        self.bairro = Label(self.window, text="Bairro")
        self.bairro.grid(row=9, column=0, sticky="new",  padx=(5,10))

        self.bairro_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.bairro_entry.grid(row=10, column=0, sticky="new",  padx=10)
        self.bairro_entry.insert(0, self.fornecedor.get_pessoa().get_endereco().get_bairro())

        self.cep = Label(self.window, text="CEP")
        self.cep.grid(row=9, column=1, sticky="new",  padx=(5,10))

        self.cep_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.cep_entry.grid(row=10, column=1, sticky="new",  padx=10)
        self.cep_entry.insert(0, self.fornecedor.get_pessoa().get_endereco().get_cep())

        self.cidade = Label(self.window, text="Cidade")
        self.cidade.grid(row=11, column=0, sticky="new",  padx=(5,10))

        self.comboMunicipio = Combobox(self.window, font=('calibri', 15, 'normal'), state="readonly")
        self.comboMunicipio.grid(row=12, column=0, sticky="new",  padx=10)

        self.estado = Label(self.window, text="UF")
        self.estado.grid(row=11, column=1, sticky="new",  padx=(5,10))

        self.comboEstado = Combobox(self.window, font=('calibri', 15, 'normal'), state="readonly")
        self.comboEstado.grid(row=12, column=1, sticky="new",  padx=10)
        self.comboEstado.bind('<<ComboboxSelected>>', self.carregaMunicipioComoboBox)

        self.carregaEstadoComoboBox()

        self.window.columnconfigure((0, 1), weight=1)


    def btnSalvar(self):
        message = ''
        try:
            self.fornecedor.get_pessoa().set_rg(self.rg_entry.get())
            self.fornecedor.get_pessoa().set_cpf(self.cpf_entry.get())
            self.fornecedor.get_pessoa().set_nome(self.nome_entry.get())
            self.fornecedor.get_pessoa().set_apelido(self.apelido_entry.get())
            self.fornecedor.get_pessoa().get_endereco().set_cep(int(self.cep_entry.get()))
            self.fornecedor.get_pessoa().get_endereco().set_bairro(self.bairro_entry.get())
            self.fornecedor.get_pessoa().get_endereco().set_logradouro(self.logradouro_entry.get())
            self.fornecedor.get_pessoa().get_endereco().set_id_municipio(self.lstMunicipio[int(self.comboMunicipio.current())].get_id_municipio())
            self.fornecedor.get_pessoa().get_endereco().set_numero(int(self.numero_entry.get()))
            if len(self.nome_entry.get()) > 0:
                self.fornecedor.Salvar()
            else:
                message="Nome é Obrigátorio"
            if (str(message) != ""):
                messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(message))
            else:
                messagebox.showinfo('Salvo', "Salvo com sucesso")
                self.window.destroy()
        except Exception as erro:
            messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(message) + "\n" + str(erro))
            print(str(erro))
    def carregaEstadoComoboBox(self):
        values = []
        cont = 0
        contfinal = 0
        for est in self.lstEstado:
            values.append(est.get_uf())
            if self.fornecedor.get_pessoa().get_endereco().get_municipio().get_id_estado() == est.get_id_estado():
                contfinal = cont
            else:
                cont = cont + 1
        self.comboEstado['values'] = values
        if self.fornecedor.get_id_pessoa() > 0:
            self.comboEstado.current(contfinal)
            self.carregaMunicipioComoboBox()

    def carregaMunicipioComoboBox(self, event=''):
        UF = self.lstEstado[int(self.comboEstado.current())].get_uf()
        self.lstMunicipio = Municipio().listar("WHERE es.UF='" + UF + "' ORDER BY ma.nome DESC")
        values = []
        cont = 0
        contfinal = 0
        for est in self.lstMunicipio:
            values.append(est.get_nome())
            if self.fornecedor.get_pessoa().get_endereco().get_municipio().get_id_municipio() == est.get_id_municipio():
                contfinal = cont
            else:
                cont = cont + 1
        self.comboMunicipio['values'] = values
        if self.fornecedor.get_id_pessoa() > 0:
            self.comboMunicipio.current(contfinal)


class Cadastro_Pessoa_Juridica:
    def __init__(self,tela:Tk, fornecedor =Fornecedor()):

        self.fornecedor = fornecedor
        if type(fornecedor) is PessoaJuridica:
            self.fornecedor=Fornecedor(fornecedor.get_id_pessoa(),fornecedor.get_id_pessoa(),fornecedor)
        self.window = Toplevel()
        self.window.geometry('620x560')
        self.window.resizable(False, False)
        self.window.style = FuncoesAuxiliares().style
        self.window.transient(tela)  # Marca como a janela anterior
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()  # Bloqueia a janela anterior

        self.lstEstado = EstadoFederal().listar(" order by uf DESC")
        self.lstMunicipio = []


        self.window.title("Cadastro Fornecedor")
        tamanhofonte = 12
        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)
        self.menuSuperior = MenuSuperiorSalvar(self.window, 'blue')
        self.menuSuperior.btnSalvar.config(command=self.btnSalvar)

        self.razaosocial = Label(self.window, text="Razão Social")
        self.razaosocial.grid(row=1, column=0, sticky="new", padx=(5,10))

        self.razaosocial_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.razaosocial_entry.grid(row=2, column=0, columnspan=4, sticky="new",  padx=10)
        self.razaosocial_entry.insert(0, self.fornecedor.get_pessoa().get_razao_social())

        self.fantasia = Label(self.window, text="Nome Fantasia")
        self.fantasia.grid(row=3, column=0, sticky="new",  padx=(5,10))

        self.fantasia_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.fantasia_entry.grid(row=4, column=0, columnspan=4, sticky="new",  padx=10)
        self.fantasia_entry.insert(0, self.fornecedor.get_pessoa().get_nome_fantasia())

        self.cnpj = Label(self.window, text="CNPJ")
        self.cnpj.grid(row=5, column=0, sticky="new",  padx=(5, 10))

        self.cnpj_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.cnpj_entry.grid(row=6, column=0, sticky="new",  padx=10)
        self.cnpj_entry.insert(0, self.fornecedor.get_pessoa().get_cnpj())

        self.ie = Label(self.window, text="Inscrição Estadual")
        self.ie.grid(row=5, column=1, sticky="new",  padx=(5,10))

        self.ie_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.ie_entry.grid(row=6, column=1, sticky="new",  padx=10)
        self.ie_entry.insert(0,self.fornecedor.get_pessoa().get_ie())

        self.logradouro = Label(self.window, text="Logradouro")
        self.logradouro.grid(row=7, column=0, sticky="new",  padx=(5,10))

        self.logradouro_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.logradouro_entry.grid(row=8, column=0, sticky="new",  padx=10)
        self.logradouro_entry.insert(0,self.fornecedor.get_pessoa().get_endereco().get_logradouro())

        self.numero = Label(self.window, text="Número")
        self.numero.grid(row=7, column=1, sticky="new",  padx=(5,10))

        self.numero_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.numero_entry.grid(row=8, column=1, sticky="new",  padx=10)
        self.numero_entry.insert(0, self.fornecedor.get_pessoa().get_endereco().get_numero())

        self.bairro = Label(self.window, text="Bairro")
        self.bairro.grid(row=9, column=0, sticky="new",  padx=(5,10))

        self.bairro_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.bairro_entry.grid(row=10, column=0, sticky="new",  padx=10)
        self.bairro_entry.insert(0,self.fornecedor.get_pessoa().get_endereco().get_bairro())

        self.cep = Label(self.window, text="CEP")
        self.cep.grid(row=9, column=1, sticky="new",  padx=(5,10))

        self.cep_entry = Entry(self.window, style='TEntry', font=('calibri', 15))
        self.cep_entry.grid(row=10, column=1, sticky="new",  padx=10)
        self.cep_entry.insert(0, self.fornecedor.get_pessoa().get_endereco().get_cep())

        self.cidade = Label(self.window, text="Cidade")
        self.cidade.grid(row=11, column=0, sticky="new",  padx=(5,10))

        self.comboMunicipio = Combobox(self.window, font=('calibri', 15, 'normal'), state="readonly")
        self.comboMunicipio.grid(row=12, column=0, sticky="new",  padx=10)

        self.estado = Label(self.window, text="UF")
        self.estado.grid(row=11, column=1, sticky="new",  padx=(5,10))

        self.comboEstado = Combobox(self.window, font=('calibri', 15, 'normal'), state="readonly")
        self.comboEstado.grid(row=12, column=1, sticky="new",  padx=10)
        self.comboEstado.bind('<<ComboboxSelected>>', self.carregaMunicipioComoboBox)

        self.carregaEstadoComoboBox()

        self.window.columnconfigure((0, 1), weight=1)

    def btnSalvar(self):
        message = ''
        try:
            self.fornecedor.get_pessoa().set_ie(self.ie_entry.get())
            self.fornecedor.get_pessoa().set_cnpj(self.cnpj_entry.get())
            self.fornecedor.get_pessoa().set_razao_social(self.razaosocial_entry.get())
            self.fornecedor.get_pessoa().set_nome_fantasia(self.fantasia_entry.get())
            self.fornecedor.get_pessoa().get_endereco().set_cep(int(self.cep_entry.get()))
            self.fornecedor.get_pessoa().get_endereco().set_bairro(self.bairro_entry.get())
            self.fornecedor.get_pessoa().get_endereco().set_logradouro(self.logradouro_entry.get())
            self.fornecedor.get_pessoa().get_endereco().set_id_municipio(self.lstMunicipio[int(self.comboMunicipio.current())].get_id_municipio())
            self.fornecedor.get_pessoa().get_endereco().set_numero(int(self.numero_entry.get()))
            if len(self.fornecedor.get_pessoa().get_razao_social()) > 0:
                self.fornecedor.Salvar()
            else:
                message="Razao Social é Obrigátorio"
            if (str(message) != ""):
                messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(message))
            else:
                messagebox.showinfo('Salvo', "Salvo com sucesso")
                self.window.destroy()
        except Exception as erro:
            messagebox.showerror('Erro', "Verifique a formatação dos campos \n\n" + str(message) + "\n" + str(erro))
            print(str(erro))
    def carregaEstadoComoboBox(self):
        values = []
        cont = 0
        contfinal = 0
        for est in self.lstEstado:
            values.append(est.get_uf())
            if self.fornecedor.get_pessoa().get_endereco().get_municipio().get_id_estado() == est.get_id_estado():
                contfinal = cont
            else:
                cont = cont + 1
        self.comboEstado['values'] = values
        if self.fornecedor.get_id_pessoa() > 0:
            self.comboEstado.current(contfinal)
            self.carregaMunicipioComoboBox()

    def carregaMunicipioComoboBox(self, event=''):
        UF = self.lstEstado[int(self.comboEstado.current())].get_uf()
        self.lstMunicipio = Municipio().listar("WHERE es.UF='" + UF + "' ORDER BY ma.nome DESC")
        values = []
        cont = 0
        contfinal = 0
        for est in self.lstMunicipio:
            values.append(est.get_nome())
            if self.fornecedor.get_pessoa().get_endereco().get_municipio().get_id_municipio() == est.get_id_municipio():
                contfinal = cont
            else:
                cont = cont + 1
        self.comboMunicipio['values'] = values
        if self.fornecedor.get_id_pessoa() > 0:
            self.comboMunicipio.current(contfinal)


class Seleciona_Pessoa:
    def __init__(self):

        self.window = Toplevel()
        self.window.geometry('620x560')
        self.window.resizable(False, False)
        self.window.style = FuncoesAuxiliares().style
        # self.window.transient(tela)  # Marca como a janela anterior
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()
        self.window.title("Seleciona Tipo de Pessoa")
        self.window.geometry('500x200')
        tamanhofonte = 12

        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)


        self.menuSuperior = MenuSuperiorConfirmar(self.window, 'blue',50)
        self.menuSuperior.btnConfirmar.config(command=self.btnConfirmar)

        self.lbltipo = Label(self.window, text="Tipo de Pessoa")
        self.lbltipo.grid(row=1, sticky='EW')
        self.comboitem = Combobox(self.window, font=('calibri', 15, 'normal'))
        self.comboitem['values'] = ("Pessoa Fisíca", "Pessoa Jurídica")
        self.comboitem.grid(row=2, sticky='EW', padx=(10, 5))

    def btnConfirmar(self):
        fechou= False
        if int(self.comboitem.current()) == 0:
            forn =Fornecedor(pessoa=PessoaFisica())
            Cadastro_Pessoa_Fisica(self.window,forn)
            fechou = True
        if int(self.comboitem.current()) == 1:
            forn = Fornecedor(pessoa=Cadastro_Pessoa_Juridica())
            Cadastro_Pessoa_Juridica(self.window, forn)
            fechou = True
        if fechou:
            self.window.destroy()
class Consulta_Fornecedor:
    def __init__(self, item=()):
        self.IdTanque = 0
        self.itens = item
        self.window = Toplevel()
        self.window.geometry('860x605')
        self.window.resizable(False,False)
        self.window.style = FuncoesAuxiliares().style
        self.window.title("Consulta Fornecedor")
        tamanhofonte = 12

        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)

        self.menuSuperior = MenuSuperiorConsulta(self.window, 'blue')
        self.menuSuperior.btnNovo.config(command=self.clickNovo)
        self.menuSuperior.btnEditar.config(command=self.clickEditar)
        self.menuSuperior.btnDeletar.config(command=self.clickDeletar)

        self.tree = self.create_tree_widget()

        self.lbldescricao = Label(self.window, text="Nome")
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
        Seleciona_Pessoa()

    def clickEditar(self):
        selected_item = self.tree.focus()
        if selected_item != '':
            details = self.tree.item(selected_item)
            Id = int(details.get("values")[0])
            lst = Fornecedor().Listar(" WHERE IdPessoa=" + str(Id))
            if len(lst) >0:
                if lst[0].get_tipo() == 0:
                    Cadastro_Pessoa_Fisica(self.window,lst[0])
                if lst[0].get_tipo() == 1:
                    Cadastro_Pessoa_Juridica(self.window,lst[0])

    def clickDeletar(self):
        try:
            selected_item = self.tree.focus()
            if selected_item != '':
                details = self.tree.item(selected_item)
                Id = int(details.get("values")[0])
                it = Fornecedor().Listar(" WHERE IdPessoa=" + str(Id))[0]
                msg_box = messagebox.askquestion('Confirma Exclusão',
                                                 'Deseja mesmo Excluir o Item \n ' + it.dados_principais() + ' ?',
                                                 icon='warning')
                if msg_box == 'yes':
                    strerro =it.Deletar()
                    if len(strerro) <= 0:
                        self.tree.delete(selected_item)
                    else:
                        messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(strerro))
        except Exception as erro:
            messagebox.showerror('Erro', "ERRO ao deletar! Atualize a pagina\n\n" + str(erro))
        finally:
            self.window.focus_force()

    def create_tree_widget(self):
        columns = ('IdPessoa', 'Nome/RazaoSocial', 'Apelido/Fantasia', 'Cpf/Cnpj')
        tree = Treeview(self.window, columns=columns, show='headings', height=14)

        # define headings
        tree.heading('IdPessoa', text='código')
        tree.column('IdPessoa', width=50, anchor=CENTER)
        tree.heading('Nome/RazaoSocial', text='Nome/Razão Social')
        tree.column('Nome/RazaoSocial', width=300)
        tree.heading('Apelido/Fantasia', text='Apelido/Fantasia')
        tree.column('Apelido/Fantasia', width=300, anchor=CENTER)
        tree.heading('Cpf/Cnpj', text='Cpf/Cnpj')
        tree.column('Cpf/Cnpj', width=100, anchor=CENTER)

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
            string = (" Where nome LIKE '%" + self.txtdescricao.get() + "%' OR RazaoSocial LIKE '%"+
                      self.txtdescricao.get()+"%' OR Apelido LIKE '%" + self.txtdescricao.get()+"%' OR"+
                      " NomeFantasia LIKE '%"+self.txtdescricao.get()+"%';")
            print(string)
        self.itens = Fornecedor().Listar(string)
        index = -1
        for i in self.tree.get_children():
            self.tree.delete(i)

        for it in self.itens:
            if it.get_tipo()==1:
                self.tree.insert('', index + 1, values=(
                    it.get_id_pessoa(),
                    it.get_razao_social(),
                    it.get_nome_fantasia(),
                    it.get_cnpj()))
            else:
                self.tree.insert('', index+1,values=(
                    it.get_id_pessoa(),
                    it.get_nome(),
                    it.get_apelido(),
                    it.get_cpf()
                ))

    def item_selected(self, event):
        pass


class Seleciona_Fornecedor:
    def __init__(self, tela, cadastro_compra, item=()):
        super().__init__()
        self.item = Fornecedor()
        self.cadastro_compra = cadastro_compra
        self.itens = item
        self.window = Toplevel()
        self.window.geometry('860x605')
        cor_fundo = '#C0C0C0'
        self.window.configure(bg=cor_fundo)
        self.window.style = FuncoesAuxiliares().style
        self.window.title("Seleciona Tanque")
        tamanhofonte = 12
        self.window.focus_force()  # Marca a janela atual como Focus
        self.window.grab_set()  # Bloqueia a janela anterior
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
        columns = ('IdPessoa', 'Nome/RazaoSocial', 'Apelido/Fantasia', 'Cpf/Cnpj')
        tree = Treeview(self.window, columns=columns, show='headings', height=14)

        # define headings
        tree.heading('IdPessoa', text='código')
        tree.column('IdPessoa', width=50, anchor=CENTER)
        tree.heading('Nome/RazaoSocial', text='Nome/Razão Social')
        tree.column('Nome/RazaoSocial', width=300)
        tree.heading('Apelido/Fantasia', text='Apelido/Fantasia')
        tree.column('Apelido/Fantasia', width=300, anchor=CENTER)
        tree.heading('Cpf/Cnpj', text='Cpf/Cnpj')
        tree.column('Cpf/Cnpj', width=100, anchor=CENTER)

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
            string = (" Where nome LIKE '%" + self.txtdescricao.get() + "%' OR RazaoSocial LIKE '%"+
                      self.txtdescricao.get()+"%' OR Apelido LIKE '%" + self.txtdescricao.get()+"%' OR"+
                      " NomeFantasia LIKE '%"+self.txtdescricao.get()+"%';")
            print(string)
        self.itens = Fornecedor().Listar(string)
        index = -1
        for i in self.tree.get_children():
            self.tree.delete(i)

        for it in self.itens:
            if it.get_tipo()==1:
                self.tree.insert('', index + 1, values=(
                    it.get_id_pessoa(),
                    it.get_razao_social(),
                    it.get_nome_fantasia(),
                    it.get_cnpj()))
            else:
                self.tree.insert('', index+1,values=(
                    it.get_id_pessoa(),
                    it.get_nome(),
                    it.get_apelido(),
                    it.get_cpf()
                ))

    def item_selected(self, event):
        pass
#Consulta_Pessoa().window.mainloop()