import os
from datetime import datetime

from reportlab.pdfgen import canvas

from Banco.Conexao import Conexao


class Tanque:
    def __init__(self, idtanque=0, descricao="", qtdpeixe=0, ph=0.00, temperatura=0.00, volume=0.00,
                 fasedesenvolvimento=0):
        self.__id_tanque = idtanque
        self.__descricao = descricao
        self.__qtd_peixe = qtdpeixe
        self.__ph = ph
        self.__temperatura = temperatura
        self.__volume = volume
        self.__fase_desenvolvimento = fasedesenvolvimento

    def get_id_tanque(self) -> int:
        return self.__id_tanque

    def set_id_tanque(self, idtanque: int):
        self.__id_tanque = idtanque

    def get_descricao(self) -> str:
        return self.__descricao

    def set_descricao(self, desc: str):
        self.__descricao = desc

    def get_qtd_peixe(self) -> int:
        return self.__qtd_peixe

    def set_qtd_peixe(self, qtd: int):
        self.__qtd_peixe = qtd

    def get_ph(self) -> float:
        return self.__ph

    def set_ph(self, ph: float):
        self.__ph = ph

    def get_temperatura(self) -> float:
        return self.__temperatura

    def set_temperatura(self, temp: float):
        self.__temperatura = temp

    def get_volume(self) -> float:
        return self.__volume

    def set_volume(self, vol: float):
        self.__volume = vol

    def get_fase_desenvolvimento(self) -> int:
        return self.__fase_desenvolvimento

    def set_fase_desenvolvimento(self, fase: int):
        self.__fase_desenvolvimento = fase

    def texto_fase_desenvolvimento(self) -> str:
        if self.get_fase_desenvolvimento() == 0:
            return 'Alevino'
        if self.get_fase_desenvolvimento() == 1:
            return 'Juvenil'
        if self.get_fase_desenvolvimento() == 2:
            return 'Adulto'
    def dados_principais(self):

        return str(self.__id_tanque) + "-" + self.__descricao + " de " + str(self.__volume)+" mt³"

    def salvar(self):
        strErro = self.validcao()
        if len(strErro) < 1:
            if self.get_id_tanque() > 0:
                sql = ("update Tanques set descricao=%s, QtdPeixe=%s, PH=%s, Temperatura=%s, "+
                       "Volume=%s, FaseDesenvolvimento=%s where IdTanque=") + str(self.__id_tanque)
            else:
                sql = ("INSERT into Tanques (descricao, QtdPeixe, PH,Temperatura,Volume,FaseDesenvolvimento) "
                       "values(%s,%s,%s,%s,%s,%s);")
            registro = (self.__descricao, self.__qtd_peixe, self.__ph,self.__temperatura,self.__volume,self.__fase_desenvolvimento)
            print(sql, registro)
            con = Conexao()
            strErro = con.insere(sql, registro)
        return strErro

    def validcao(self):
        msgErro = ''
        if self.get_ph()<=0:
            msgErro += 'PH deve ser Maior que ZERO \n'
        if len(self.get_descricao()) <= 0:
            msgErro += 'Descrição é Obrigatório\n'
        if self.get_volume() <= 0:
            msgErro += 'Volume deve ser MAIOR que ZERO'
        if self.get_temperatura() <= 0:
            msgErro += 'Temperatura deve ser MAIOR que ZERO'
        return msgErro

    def listar(self, where=""):
        sql = "SELECT IdTanque,descricao,QtdPeixe,PH,Temperatura,Volume,FaseDesenvolvimento FROM Tanques " + where + ";"
        print(sql)
        dados = Conexao().listar(sql)
        lista = []
        index = -1
        if dados is not None:
            for linha in dados:
                lista.insert(index + 1, Tanque(int(linha[0]), str(linha[1]), int(linha[2]),
                                               float(linha[3]), float(linha[4]), float(linha[5]), int(linha[6])))
        return lista

    def deletar(self, id: int):
        sql = "delete from Tanques where IdTanque=" + str(id)
        return str(Conexao().deletar(sql))

    def Mm2p(self,milimetros):
        return milimetros / 0.352777

    def Gerar_pdf(self, lst):
        colunas = []
        #caminho_completo = os.path.join(os.path.dirname(__file__), "..", "Relatorios", "Relatorio_tanques.pdf")
        cnv = canvas.Canvas('Relatorio_tanques.pdf')
        cnv.drawString(0, 0, ' ')
        margem = 20
        linha = 280
        somaQtd = 0

        cnv.setFont('Helvetica-Bold', 15)

        cnv.drawImage("Imagens/logo_fundo_branco.png", 50, self.Mm2p(260), width=100, height=100)

        cnv.drawString(self.Mm2p(70), self.Mm2p(linha), "Tilapicultura do BERNARDÃO  ss ")
        linha -= 7
        cnv.drawString(self.Mm2p(70), self.Mm2p(linha), "Sitio Bica de Pedra - Itapuí, SP")
        linha -= 7
        cnv.drawString(self.Mm2p(75), self.Mm2p(linha), " CNPJ: 72.132.707/0001-62")
        linha -= 2
        cnv.line(0, self.Mm2p(linha), self.Mm2p(15000), self.Mm2p(linha))
        linha -= 10
        cnv.drawString(self.Mm2p(75), self.Mm2p(linha), " Relátorio dos Tanques")
        cnv.setFont('Helvetica-Bold', 14)
        linha -= 10
        cnv.drawString(self.Mm2p(margem), self.Mm2p(linha),
                       "Data do Relatorio: " + datetime.now().strftime("%d/%m/%Y"))
        linha -= 15
        cnv.drawString(self.Mm2p(margem), self.Mm2p(linha), "Descrição")
        cnv.drawString(self.Mm2p(80), self.Mm2p(linha), "Fase")
        cnv.drawString(self.Mm2p(100), self.Mm2p(linha), "Temperatura")
        cnv.drawString(self.Mm2p(140), self.Mm2p(linha), "PH")
        cnv.drawString(self.Mm2p(160), self.Mm2p(linha), "Volume")
        cnv.drawString(self.Mm2p(180), self.Mm2p(linha), "Qtd")
        linha -= 2
        cnv.line(0, self.Mm2p(linha), self.Mm2p(15000), self.Mm2p(linha))
        linha = linha - 5
        cnv.setFont('Helvetica', 12)

        for it in lst:
            cnv.drawString(self.Mm2p(margem), self.Mm2p(linha), it.get_descricao())
            cnv.drawString(self.Mm2p(80), self.Mm2p(linha), it.texto_fase_desenvolvimento())
            cnv.drawString(self.Mm2p(105), self.Mm2p(linha), str(it.get_temperatura())+" ºC")
            cnv.drawString(self.Mm2p(140), self.Mm2p(linha), str(it.get_ph()))
            cnv.drawString(self.Mm2p(160), self.Mm2p(linha), str(it.get_volume()))
            cnv.drawString(self.Mm2p(180), self.Mm2p(linha), str(it.get_qtd_peixe()))
            linha -= 3
            cnv.line(0, self.Mm2p(linha), self.Mm2p(15000), self.Mm2p(linha))
            somaQtd += it.get_qtd_peixe()
            linha = linha - 4

        cnv.drawString(self.Mm2p(167), self.Mm2p(linha), "Total:  " + str(somaQtd))
        cnv.save()
        os.system('Relatorio_tanques.pdf')


#Tanque().Gerar_pdf(Tanque().listar())