import datetime
import os

from reportlab.pdfgen import canvas

from Banco.Conexao import Conexao


class Item:
    def __init__(self, iditem=0, descricao="", qtd=0, preco=0.00, tipo=0):
        self.__id_item = iditem
        self.__descricao = descricao
        self.__qtd = qtd
        self.__preco = preco
        self.__tipo = tipo

    def get_id_item(self) -> int:
        return self.__id_item

    def set_id_item(self, id_item: int):
        self.__id_item = id_item

    def get_descricao(self) -> str:
        return self.__descricao

    def set_descricao(self, desc: str):
        self.__descricao = desc

    def get_qtd(self) -> int:
        return self.__qtd

    def set_qtd(self, valor: int):
        self.__qtd = valor

    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, preco: float):
        self.__preco = preco

    def get_tipo(self) -> int:
        return self.__tipo

    def set_tipo(self, tipo: int):
        self.__tipo = tipo

    def get_texto_tipo_item(self) -> str:
        if self.__tipo == 0:
            return "Alimentos"
        if self.__tipo == 1:
            return "Manutenção Tanque"
        if self.__tipo == 2:
            return "Veterinário"
        return "Outros"

    def dados_principais(self):
        return str(self.__id_item) + "-" + self.__descricao+"-" + self.get_texto_tipo_item()

    def salvar(self):
        if self.get_id_item() > 0:
            sql = "update ITEM set descricao=%s, qtd=%s, preco=%s,tipo=%s where IdITEM=" + str(self.__id_item)
        else:
            sql = "INSERT into ITEM (`descricao`, `qtd`, `preco`,tipo) values(%s,%s,%s,%s);"
        registro = (self.__descricao, self.__qtd, self.__preco,self.__tipo)
        print(sql,registro)
        Conexao().insere(sql, registro)

    def listar(self, where=""):
        sql = "SELECT IdItem,descricao,qtd,preco,tipo FROM item " + where + ";"
        print(sql)
        dados = Conexao().listar(sql)
        lista = []
        index = -1
        if dados is not None:
            for linha in dados:
                lista.insert(index + 1, Item(int(linha[0]), str(linha[1]), int(linha[2]), float(linha[3]), int(linha[4])))
        return lista

    def deletar(self, id: int):
        sql = "delete from item where IdItem=" + str(id)
        Conexao().deletar(sql)

    def Mm2p(self,milimetros):
        return milimetros / 0.352777

    def Gerar_pdf(self, lst):
        colunas = []
        #caminho_completo = os.path.join(os.path.dirname(__file__), "..", "Relatorios", "Relatorio_compra.pdf")
        cnv = canvas.Canvas("Relatorio_item.pdf")
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
        cnv.drawString(self.Mm2p(75), self.Mm2p(linha), " Relátorio dos Itens em Estoque")
        cnv.setFont('Helvetica-Bold', 14)
        linha -= 10
        cnv.drawString(self.Mm2p(margem), self.Mm2p(linha),
                       "Data do Relatorio: " + datetime.datetime.now().strftime("%d/%m/%Y"))
        linha -= 15
        cnv.drawString(self.Mm2p(margem), self.Mm2p(linha), "Descrição")
        cnv.drawString(self.Mm2p(120), self.Mm2p(linha), "Tipo")
        cnv.drawString(self.Mm2p(170), self.Mm2p(linha), "Qtd")
        linha -= 2
        cnv.line(0, self.Mm2p(linha), self.Mm2p(15000), self.Mm2p(linha))
        linha = linha - 5
        cnv.setFont('Helvetica', 12)
        for it in lst:
            cnv.drawString(self.Mm2p(margem), self.Mm2p(linha), it.__descricao)
            cnv.drawString(self.Mm2p(120), self.Mm2p(linha), it.get_texto_tipo_item())
            cnv.drawString(self.Mm2p(170), self.Mm2p(linha), str(it.get_qtd()))
            linha -= 3
            cnv.line(0, self.Mm2p(linha), self.Mm2p(15000), self.Mm2p(linha))
            somaQtd += it.get_qtd()
            linha = linha - 4

        cnv.drawString(self.Mm2p(156), self.Mm2p(linha), "Total:  " + str(somaQtd))
        cnv.save()
        os.system("Relatorio_item.pdf")


"""its = Item().listar()
Item().Gerar_pdf(its)
##it = Item(descricao="Celular", qtd=10, preco=51.52)
#it.salvar()
"""