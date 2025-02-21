import datetime

from Banco.Conexao import Conexao
from Classes.item import Item


class AjusteItem:

    def __init__(self, idajuste=0,descricao: str = "", datahora=datetime.datetime.today(), qtdatual: int = 0,
                 qtdmovimentacao: int = 0, qtdnova: int = 0, iditem=0, item=Item()):
        self.__id_ajuste = idajuste
        self.__descricao = descricao
        self.__qtd_atual = qtdatual
        self.__qtd_movimentacao = qtdmovimentacao
        self.__qtd_nova = qtdnova
        self.__data_hora = datahora
        self.__id_item = iditem
        self.__item = item

    def get_id_ajuste(self) -> int:
        return self.__id_ajuste

    def set_id_ajuste(self, idaju: int):
        self.__id_ajuste = idaju

    def get_qtd_atual(self) -> int:
        return self.__qtd_atual

    def set_qtd_atual(self, qtd: int):
        self.__qtd_atual = qtd

    def get_qtd_nova(self) -> int:
        return self.__qtd_nova

    def set_qtd_nova(self, qtd: int):
        self.__qtd_nova = qtd

    def get_qtd_movimentacao(self) -> int:
        return self.__qtd_movimentacao

    def set_qtd_movimentacao(self, qtd: int):
        self.__qtd_movimentacao = qtd

    def get_id_item(self) -> int:
        return self.__id_item

    def set_id_item(self, iditem: int):
        self.__id_item = iditem

    def get_item(self) -> Item:
        return self.__item

    def set_item(self, item: Item):
        self.__item = item

    def set_descricao(self, desc: str):
        self.__descricao = desc

    def get_descricao(self) -> str:
        return self.__descricao

    def dados_principais(self):
        return str(self.__id_ajuste) + "-" + self.__descricao+"-" + self.get_item().dados_principais()
    def validcao(self):
        msgErro = ''
        if self.get_id_item() <= 0:
            msgErro += 'Item deve ser Selecionado \n'
        if len(self.get_descricao()) <= 0:
            msgErro += 'Descrição é Obrigatório\n'
        if self.get_qtd_movimentacao() == 0:
            msgErro += 'Movimentacao deve ser DIFERENTE de ZERO \n'
        return msgErro
    def salvar(self):
        strErro = self.validcao()
        sql = ""
        if len(strErro) < 1:
            if self.__id_ajuste <= 0:
                sql = "INSERT into ajusteitem (Iditem,Descricao,DataHora, QtdAtual, QtdMovimentacao,QtdNova) values(%s,%s,%s,%s,%s,%s);"
            registro = (self.__id_item, self.__descricao, self.__data_hora, self.__qtd_atual,self.__qtd_movimentacao,self.__qtd_nova)
            print(sql, registro)
            strErro = Conexao().insere(sql, registro)
        return strErro

    def listar(self, where=""):
        sql = ("SELECT IdAjuste,aj.Descricao,DataHora,QtdAtual,QtdMovimentacao,QtdNova,ta.Iditem,ta.descricao,ta.Tipo "
                + "FROM ajusteitem AS aj INNER JOIN item  AS ta ON ta.Iditem=aj.Iditem" ) + where + ";"
        print(sql)
        dados = Conexao().listar(sql)
        lista = []
        index = -1
        if dados is not None:
            for linha in dados:
                lista.insert(index + 1, AjusteItem(int(linha[0]), str(linha[1]),
                                               datetime.datetime.strptime(str(linha[2]), '%Y-%m-%d %H:%M:%S'),
                                               int(linha[3]), int(linha[4]),int(linha[5]), int(linha[6]),
                                                Item(int(linha[6]),str(linha[7]), tipo=int(linha[8]))))
        return lista

    def deletar(self, id: int):
        sql = "delete from ajusteitem where IdAjuste=" + str(id)
        return str(Conexao().deletar(sql))