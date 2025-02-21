from Banco.Conexao import Conexao


class EstadoFederal:
    def __init__(self, idestado="", uf="", nome=""):
        self.__id_estado = idestado
        self.__uf = uf
        self.__nome = nome

    def get_id_estado(self) -> str:
        return self.__id_estado

    def set_id_estado(self, id_estado: str):
        self.__id_estado = id_estado

    def get_uf(self) -> str:
        return self.__uf

    def set_uf(self, uf: str):
        self.__uf = uf

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def listar(self, where=""):
        sql = "SELECT IdEstado,Uf,nome FROM estadofederal " + where + ";"
        print(sql)
        dados = Conexao().listar(sql)
        lista = []
        index = -1
        if dados is not None:
            for linha in dados:
                lista.insert(index + 1, EstadoFederal(str(linha[0]), str(linha[1]), str(linha[2])))
        return lista


class Municipio:
    def __init__(self, idmunicipio="", idestado="", nome="", estado=EstadoFederal()):
        self.__id_municipio = idmunicipio
        self.__id_estado = idestado
        self.__estado_federal = estado
        self.__nome = nome

    def get_id_municipio(self) -> str:
        return self.__id_municipio

    def set_id_municipio(self, id_municipio: str):
        self.__id_municipio = id_municipio

    def get_id_estado(self) -> str:
        return self.__id_estado

    def set_id_estado(self, id_estado: str):
        self.__id_estado = id_estado

    def get_estado_federal(self) -> EstadoFederal:
        return self.__estado_federal

    def set_estado_federal(self, estado: EstadoFederal):
        self.__estado_federal = estado

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def listar(self, where=""):
        sql = ("SELECT IdMunicipio,ma.IdEstado,ma.Nome,UF FROM municipio AS ma INNER JOIN estadofederal AS es " +
               "ON ma.IdEstado=es.IdEstado ") + where + ";"
        print(sql)
        dados = Conexao().listar(sql)
        lista = []
        index = -1
        if dados is not None:
            for linha in dados:
                lista.insert(index + 1, Municipio(str(linha[0]), str(linha[1]), str(linha[2])))
        return lista


class Endereco:
    def __init__(self, idendereco=0, logradouro="", bairro="",
                 numero=0, cep=0, id_municipio="", municipio=Municipio()):
        self.__id_endereco = idendereco
        self.__logradouro = logradouro
        self.__bairro = bairro
        self.__numero = numero
        self.__cep = cep
        self.__id_municipio = id_municipio
        self.__municipio = municipio

    def get_id_endereco(self) -> int:
        return self.__id_endereco

    def set_id_endereco(self, id_endereco: int):
        self.__id_endereco = id_endereco

    def get_logradouro(self) -> str:
        return self.__logradouro

    def set_logradouro(self, logra: str):
        self.__logradouro = logra

    def get_bairro(self) -> str:
        return self.__bairro

    def set_bairro(self, logra: str):
        self.__bairro = logra

    def get_cep(self) -> int:
        return self.__cep

    def set_cep(self, logra: int):
        self.__cep = logra

    def get_numero(self) -> int:
        return self.__numero

    def set_numero(self, num: int):
        self.__numero = num

    def get_id_municipio(self) -> str:
        return self.__id_municipio

    def set_id_municipio(self, id_municipio: str):
        self.__id_municipio = id_municipio

    def get_municipio(self) -> Municipio:
        return self.__municipio

    def set_municipio(self, muni: Municipio):
        self.__municipio = muni
