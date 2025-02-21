import datetime

from Banco.Conexao import Conexao
from Classes.tanques import Tanque


class AjusteTanque:

    def __init__(self, idajuste=0,descricao="", qtdanterior=0, qtdmovimentacao=0,
                 qtdnova=0, idtanque=0, tanque=Tanque()):
        self.__id_ajuste = idajuste
        self.__qtd_anterior = qtdanterior
        self.__qtd_movimentacao = qtdmovimentacao
        self.__qtd_nova = qtdnova
        self.__id_tanque = idtanque
        self.__tanque = tanque
        self.__descricao = descricao

    def get_id_ajuste(self) -> int:
        return self.__id_ajuste

    def set_id_ajuste(self, idaju: int):
        self.__id_ajuste = idaju

    def get_descricao(self) -> str:
        return self.__descricao

    def set_descricao(self, desc: str):
        self.__descricao = desc
    def get_qtd_anterior(self) -> int:
        return self.__qtd_anterior

    def set_qtd_anterior(self, qtd: int):
        self.__qtd_anterior = qtd

    def get_qtd_nova(self) -> int:
        return self.__qtd_nova

    def set_qtd_nova(self, qtd: int):
        self.__qtd_nova = qtd

    def get_qtd_movimentacao(self) -> int:
        return self.__qtd_movimentacao

    def set_qtd_movimentacao(self, qtd: int):
        self.__qtd_movimentacao = qtd

    def get_id_tanque(self) -> int:
        return self.__id_tanque

    def set_id_tanque(self, idtanque: int):
        self.__id_tanque = idtanque

    def get_tanque(self) -> Tanque:
        return self.__tanque

    def set_tanque(self, tanque: Tanque):
        self.__tanque = tanque

    def dados_principais(self):
        return str(self.__descricao) + "-" + self.__tanque.dados_principais()

    def validcao(self):
        msgErro = ''
        if self.get_id_tanque() <= 0:
            msgErro += 'Tanque deve ser Selecionado \n'
        if len(self.get_descricao()) <= 0:
            msgErro += 'Descrição é Obrigatório\n'
        if self.get_qtd_movimentacao() == 0:
            msgErro += 'Movimentacao deve ser DIFERENTE de zero \n'
        return msgErro
    def salvar(self):
        strErro = self.validcao()
        if len(strErro) < 1:
            if self.__id_ajuste > 0:
                sql = ("update ajustetanque set IdTanque=%s, descricao=%s, QtdAtual=%s, QtdMovimentacao=%s, QtdNova=%s"
                       +" where IdAjusteEstoque=") + str(self.__id_ajuste)
            else:
                sql = "INSERT into ajustetanque (IdTanque,Descricao, QtdAtual, QtdMovimentacao,QtdNova) values(%s,%s,%s,%s,%s);"
            registro = (self.__id_tanque, self.__descricao, self.__qtd_anterior,self.__qtd_movimentacao,self.__qtd_nova)
            print(sql, registro)
            strErro = Conexao().insere(sql, registro)
        return strErro

    def listar(self, where=""):
        sql = ("SELECT IdAjusteEstoque,aj.Descricao,QtdAtual,QtdMovimentacao,QtdNova,ta.Idtanque,ta.descricao,ta.volume "
               "FROM ajustetanque AS aj INNER JOIN tanques  AS ta ON ta.IdTanque=aj.IdTanque ") + where + ";"
        print(sql)
        dados = Conexao().listar(sql)
        lista = []
        index = -1
        if dados is not None:
            for linha in dados:
                lista.insert(index + 1, AjusteTanque(int(linha[0]), str(linha[1]), int(linha[2]), int(linha[3]),
                             int(linha[4]), idtanque=int(linha[5]),
                             tanque=Tanque(idtanque=int(linha[5]), descricao=str(linha[6]), volume=float(linha[7]))))
        return lista

    def deletar(self, id: int):
        sql = "delete from ajustetanque where IdAjusteEstoque=" + str(id)
        return str(Conexao().deletar(sql))