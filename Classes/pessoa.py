from Banco.Conexao import Conexao
from Classes.endereco import Endereco, Municipio, EstadoFederal


class Pessoa:
    def __init__(self,tipo, id_pessoa=0, id_endereco=0, endereco=Endereco(), telefone=""):
        self.__id_pessoa = id_pessoa
        self.__id_endereco = id_endereco
        self.__endereco = endereco
        self.__telefone = telefone,
        self.__tipo = tipo

    def get_id_pessoa(self) -> int:
        return self.__id_pessoa

    def set_id_pessoa(self, id_pessoa: int):
        self.__id_pessoa = id_pessoa

    def get_id_endereco(self) -> int:
        return self.__id_endereco

    def set_id_endereco(self, id_endereco: int):
        self.__id_endereco = id_endereco

    def get_endereco(self) -> Endereco:
        return self.__endereco

    def set_endereco(self, endereco: Endereco):
        self.__endereco = endereco

    def get_telefone(self) -> str:
        return self.__telefone

    def set_telefone(self, telefone: str):
        self.__telefone = telefone

    def get_tipo(self) -> int:
        return self.__tipo

    def set_tipo(self, tipo: int):
        self.__tipo = tipo

    def Deletar(self):
        text=""
        sql = "delete from Fornecedor where IdPessoa=" + str(self.get_id_pessoa()) + ";"
        str(Conexao().deletar(sql))
        sql = "delete from pessoa where IdPessoa=" + str(self.get_id_pessoa()) + ";"
        str(Conexao().deletar(sql))
        sql = "delete from endereco where IdEndereco=" + str(self.get_id_endereco())+ ";"
        return str(Conexao().deletar(sql))

class PessoaFisica(Pessoa):
    def __init__(self, id_pessoa=0, id_endereco=0, endereco=Endereco(),
                 telefone="", nome="", apelido="", rg="", cpf=""):
        super().__init__(0, id_pessoa, id_endereco, endereco, telefone)
        self.__nome = nome
        self.__apelido = apelido
        self.__rg = rg
        self.__cpf = cpf

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_apelido(self) -> str:
        return self.__apelido

    def set_apelido(self, nome: str):
        self.__apelido = nome

    def get_rg(self) -> str:
        return self.__rg

    def set_rg(self, rg: str):
        self.__rg = rg

    def get_cpf(self) -> str:
        return self.__cpf

    def set_cpf(self, nome: str):
        self.__cpf = nome

    def dados_principais(self):
        return str(self.get_id_pessoa()) + "-" + self.__nome + " - " + str(self.__apelido) + ""

class PessoaJuridica(Pessoa):
    def __init__(self, id_pessoa=0, id_endereco=0, endereco=Endereco(),
                 telefone="", razao_social="", nome_fantasia="", cnpj="", ie=""):
        super().__init__(1,id_pessoa, id_endereco, endereco, telefone)
        self.__razao_social = razao_social
        self.__nome_fantasia = nome_fantasia
        self.__cnpj = cnpj
        self.__ie = ie

    def get_razao_social(self) -> str:
        return self.__razao_social

    def set_razao_social(self, razao_social: str):
        self.__razao_social = razao_social

    def get_nome_fantasia(self) -> str:
        return self.__nome_fantasia

    def set_nome_fantasia(self, nome_fantasia: str):
        self.__nome_fantasia = nome_fantasia

    def get_cnpj(self) -> str:
        return self.__cnpj

    def set_cnpj(self, cnpj: str):
        self.__cnpj = cnpj

    def get_ie(self) -> str:
        return self.__ie

    def set_ie(self, ie: str):
        self.__ie = ie

    def dados_principais(self):
        return str(self.get_id_pessoa()) + "-" + self.__razao_social + " - " + str(self.__cnpj)

class Fornecedor:
    def __init__(self, idfornecedor: int = 0, idpessoa: int = 0, pessoa: Pessoa = PessoaJuridica()):
        self.__idfornecedor = idfornecedor
        self.__pessoa = pessoa
        self.__idpessoa = idpessoa

    def get_id_fornecedor(self):
        return self.__idfornecedor

    def set_id_fornecedor(self,idfo: int):
        self.__idfornecedor = idfo

    def get_id_pessoa(self):
        return self.__idpessoa

    def set_id_pessoa(self, idpe: int):
        self.__idpessoa = idpe

    def get_pessoa(self) -> Pessoa:
        return self.__pessoa

    def set_pessoa(self, pessoa: Pessoa):
        self.__pessoa = pessoa

    def dadosPrincipais(self):
        if type(self.get_pessoa()) is PessoaJuridica:
            return self.get_pessoa().get_razao_social()+" - "+self.get_pessoa().get_cnpj()
        else:
            return self.get_pessoa().get_nome()

    def Salvar(self):
        con = Conexao()
        strErro = con.insereFornecedor(self)
        return strErro

    def Deletar(self):
        sql = ("delete from endereco where IdEndereco=" +str(self.get_pessoa().get_id_endereco())+
               "delete from pessoa where IdPessoa=" + str(self.get_id_pessoa())+
               "delete from Forncecedor where IdPessoa=" + str(self.get_id_pessoa()))
        return str(Conexao().deletar(sql))


    def Buscar(self,where):
        forne = self.Listar(where)[0]
        return Fornecedor(forne.get_id_pessoa(),forne.get_id_pessoa(),forne)
    def Listar(self, where):
        sql = ("select tipoObjeto,IdPessoa,pe.Nome,Apelido,RG,CPF,RazaoSocial,NomeFantasia,Cnpj,InscricaoEstadual,"
               "pe.IdEndereco,mu.IdMunicipio,Logradouro,Bairro,Numero,Cep,mu.Nome,mu.IdEstado,est.uf,est.nome from pessoa "
               "AS pe INNER JOIN endereco AS en ON pe.IdEndereco=en.IdEndereco "
               "INNER JOIN municipio as mu ON mu.IdMunicipio=en.IdMunicipio "
               " INNER JOIN estadofederal as est ON est.IdEstado=mu.IdEstado ") + where + ";"
        print(sql)
        dados = Conexao().listar(sql)
        lista = []
        index = -1
        if dados is not None:
            for linha in dados:
                muni = Municipio(str(linha[11]), str(linha[17]), str(linha[16]), EstadoFederal(str(linha[16]),
                                                                                    str(linha[17]), str(linha[18])))
                endereco = Endereco(int(linha[10]), str(linha[12]), str(linha[13]), str(linha[14]), str(linha[15]),
                                                                                    str(linha[11]), muni)
                pessoa = Pessoa
                if int(linha[0]) == 0:
                    pessoa = PessoaFisica(int(linha[1]), int(linha[10]), endereco, "", str(linha[2]),
                                          str(linha[3]), str(linha[4]), str(linha[5]))
                else:
                    pessoa = PessoaJuridica(int(linha[1]), int(linha[10]), endereco,"", str(linha[6]),
                                            str(linha[7]), str(linha[8]), str(linha[9]))
                lista.insert(index + 1,pessoa)
        return lista

