import datetime

from Banco.Conexao import Conexao
from Classes.tanques import Tanque


class Horario_Alimentacao:
    def __init__(self,idhorario: int = 0, descricao: str = "", data: datetime = datetime.datetime.now(),
                 idtanque: int = 0, tanque: Tanque = Tanque()):
        self.__descricao = descricao
        self.__idhorario = idhorario
        self.__data_hora = data
        self.__idtanque = idtanque
        self.__tanque = tanque

    def get_id_horario(self) -> int:
        return self.__idhorario

    def set_id_horario(self, item: int):
        self.__idhorario = item

    def get_data_hora(self) -> datetime:
        return self.__data_hora

    def set_data_hora(self, item: datetime):
        self.__data_hora = item

    def get_descricao(self) -> str:
        return self.__descricao

    def set_descricao(self, item: str):
        self.__descricao = item
    def get_id_tanque(self) -> int:
        return self.__idtanque

    def set_id_tanque(self, item: int):
        self.__idtanque = item

    def get_tanque(self) -> Tanque:
        return self.__tanque

    def set_tanque(self, item: Tanque):
        self.__tanque = item

    def dados_principais(self):
        return str(self.__data_hora) + '-' + self.__tanque.dados_principais()

    def salvar(self):
        strErro = self.validcao()
        if len(strErro) < 1:
            if self.get_id_horario() > 0:
                sql = ("update horarioalimentacao set Hora=%s,Descricao=%s, IdTanque=%s where IdHorario="
                       + str(self.__idhorario))
            else:
                sql = "INSERT into horarioalimentacao (Hora,Descricao, IdTanque) values(%s,%s,%s);"
            registro = (self.__data_hora,self.__descricao, self.__idtanque)
            print(sql, registro)
            strErro = Conexao().insere(sql, registro)
        return strErro

    def validcao(self):
        msgErro = ''
        if self.get_id_tanque() <= 0:
            msgErro += 'Selecione o Tanque \n'
        return msgErro

    def listar(self, where=""):
        sql =("SELECT hor.IdHorario,hor.descricao, hor.Hora,ta.IdTanque,ta.descricao,ta.Volume "
               + " FROM horarioalimentacao AS hor INNER JOIN tanques AS ta on hor.IdTanque=ta.IdTanque ") + where + ";"
        print(sql)
        dados = Conexao().listar(sql)
        lista = []
        index = -1
        if dados is not None:
            for linha in dados:
                lista.insert(index + 1, Horario_Alimentacao(int(linha[0]),str(linha[1]),
                                         datetime.datetime.strptime(str(linha[2]), '%Y-%m-%d %H:%M:%S'),
                                         int(linha[3]),Tanque(int(linha[3]), str(linha[4]), volume=float(linha[5]))))
        return lista

    def deletar(self, id: int):
        sql = "delete from horarioalimentacao where IdHorario=" + str(id)
        return str(Conexao().deletar(sql))