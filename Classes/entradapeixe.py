from datetime import datetime

from Banco.Conexao import Conexao
from Classes.tanques import Tanque


class EntradaPeixe:
    def __init__(self, IdEntradaPeixe= 0, data=datetime.now(), qtd=0, idtanque=0, tanque=Tanque()):
        self.__id_entrada_peixe = IdEntradaPeixe
        self.__data_hora = data
        self.__qtd = qtd
        self.__tanque = tanque
        self.__idtanque = idtanque

    def get_id_entrada_peixe(self) -> int:
        return self.__id_entrada_peixe

    def set_id_entrada_peixe(self, valor: int):
        self.__id_entrada_peixe = valor

    def get_qtd(self) -> int:
        return self.__qtd

    def set_qtd(self, qtd: int):
        self.__qtd = qtd


    def get_data_hora(self) -> datetime:
        return self.__data_hora

    def set_data_hora(self, item: datetime):
        self.__data_hora = item

    def get_tanque(self) -> Tanque:
        return self.__tanque

    def set_tanque(self, item: Tanque):
        self.__tanque = item

    def get_id_tanque(self) -> int:
        return self.__idtanque

    def set_id_tanque(self, item: int):
        self.__idtanque = item

    def dados_principais(self):
        return str(self.__data_hora) + '- QTD: '+str(self.__qtd)+' - ' + self.__tanque.dados_principais()+""

    def salvar(self):
        strErro = self.validcao()
        if len(strErro) < 1:
            if self.get_id_entrada_peixe() > 0:
                sql = ("update EntradaPeixe set DataEntrada=%s, Qtd=%s, IdTanque=%s where IdEntradaPeixe="
                       + str(self.__id_entrada_peixe))
            else:
                sql = "INSERT into EntradaPeixe (`DataEntrada`, `qtd`,IdTanque) values(%s,%s,%s);"
            registro = (self.__data_hora, self.__qtd, self.__idtanque)
            print(sql, registro)
            strErro = Conexao().insere(sql, registro)
        return strErro
    def validcao(self):
        msgErro = ''
        if self.get_id_tanque() <= 0:
            msgErro += 'Selecione o Tanque \n'
        if self.get_qtd() <= 0:
            msgErro += 'Qtd deve ser MAIOR que ZERO\n'
        return msgErro

    def listar(self, where=""):
        sql = ("SELECT ent.IdEntradaPeixe, ent.DataEntrada, ent.qtd, ta.IdTanque,ta.descricao,ta.Volume "
               "FROM EntradaPeixe AS ent INNER JOIN tanques AS ta on ent.IdTanque=ta.IdTanque ") + where + ";"
        print(sql)
        dados = Conexao().listar(sql)
        lista = []
        index = -1
        if dados is not None:
            for linha in dados:
                lista.insert(index + 1, EntradaPeixe(int(linha[0]),
                                                 datetime.strptime(str(linha[1]), '%Y-%m-%d %H:%M:%S'),
                                                 int(linha[2]), int(linha[3]),
                                                 Tanque(int(linha[3]), str(linha[4]),volume=float(linha[5]))))
        return lista

    def deletar(self, id: int):
        sql = "delete from EntradaPeixe where IdEntradaPeixe=" + str(id)
        return str(Conexao().deletar(sql))
