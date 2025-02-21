import datetime

from Banco.Conexao import Conexao
from Classes.tanques import Tanque


class Colheita:
    def __init__(self, idcolheita=0, data=datetime.datetime.now(), qtd=0, pesomedio=0.00, idtanque=0, tanque=Tanque()):
        self.__id_colheita = idcolheita
        self.__data_hora = data
        self.__qtd = qtd
        self.__peso_medio = pesomedio
        self.__tanque = tanque
        self.__idtanque = idtanque

    def get_id_colheita(self) -> int:
        return self.__id_colheita

    def set_id_colheita(self, valor: int):
        self.__id_colheita = valor

    def get_qtd(self) -> int:
        return self.__qtd

    def set_qtd(self, qtd: int):
        self.__qtd = qtd

    def get_peso_medio(self) -> float:
        return self.__peso_medio

    def set_peso_medio(self, peso: float):
        self.__peso_medio = peso

    def get_data_hora(self) -> datetime.datetime:
        return self.__data_hora

    def set_data_hora(self, item: datetime.datetime):
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
        return str(self.__data_hora) + '-' + self.__tanque.dados_principais()

    def salvar(self):
        strErro = self.validcao()
        if len(strErro) < 1:
            if self.get_id_colheita() > 0:
                sql = ("update COLHEITA set DataColheita=%s, Qtd=%s, PesoMedio=%s, IdTanque=%s where IdColheita="
                       + str(self.__id_colheita))
            else:
                sql = "INSERT into COLHEITA (`DataColheita`, `qtd`, `PesoMedio`,IdTanque) values(%s,%s,%s,%s);"
            registro = (self.__data_hora, self.__qtd, self.__peso_medio,self.__idtanque)
            print(sql, registro)
            strErro = Conexao().insere(sql, registro)
        return strErro
    def validcao(self):
        msgErro = ''
        if self.get_id_tanque() <= 0:
            msgErro += 'Selecione o Tanque \n'
        if self.get_qtd() <= 0:
            msgErro += 'Qtd deve ser MAIOR que ZERO\n'
        if self.get_peso_medio() <= 0:
            msgErro += 'Peso Medio deve ser MAIOR que ZERO\n'
        return msgErro

    def listar(self, where=""):
        sql = ("SELECT co.IdColheita, co.DataColheita, co.qtd, co.PesoMedio,ta.IdTanque,ta.descricao,ta.Volume "
               + "FROM COLHEITA AS co INNER JOIN tanques AS ta on co.IdTanque=ta.IdTanque ") + where + ";"
        print(sql)
        dados = Conexao().listar(sql)
        lista = []
        index = -1
        if dados is not None:
            for linha in dados:
                lista.insert(index + 1, Colheita(int(linha[0]),
                                                 datetime.datetime.strptime(str(linha[1]), '%Y-%m-%d %H:%M:%S'),
                                                 int(linha[2]), float(linha[3]), int(linha[4]),
                                                 Tanque(int(linha[4]),str(linha[5]),volume=float(linha[6]))))
        return lista

    def deletar(self, id: int):
        sql = "delete from COLHEITA where IdColheita=" + str(id)
        return str(Conexao().deletar(sql))


