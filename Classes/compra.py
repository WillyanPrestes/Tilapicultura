import datetime
import os
from Banco.Conexao import Conexao
from Classes.compraitem import Compraitem
from Classes.item import Item
from Classes.pessoa import Fornecedor
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class Compra:
    def __init__(self, idcompra: int = 0, valortotal: float = 0.00, qtdkilo: float = 0.00,
                 datahora=datetime.datetime.now(), idfor: int = 0, fornecedor: Fornecedor = Fornecedor(),
                 compraitens = None):
        if compraitens is None:
            compraitens = []
        self.__id_compra = idcompra
        self.__valor_total = valortotal
        self.__qtd_kilo_peixe = qtdkilo
        self.__datahora = datahora
        self.__compraitens = compraitens
        self.__fornecedor = fornecedor
        self.__id_fornecedor = idfor

    def get_id_compra(self) -> int:
        return self.__id_compra

    def set_id_compra(self, idcompra: int):
        self.__id_compra = idcompra

    def get_valor_total(self) -> float:
        return self.__valor_total

    def set_valor_total(self, valortotal: float):
        self.__valor_total = valortotal

    def get_qtd_kilo_peixe(self) -> float:
        return self.__qtd_kilo_peixe

    def set_qtd_kilo_peixe(self, qtdkilo: float):
        self.__qtd_kilo_peixe = qtdkilo

    def get_data_hora(self) -> datetime.datetime:
        return self.__datahora

    def set_data_hora(self, datahora: datetime.datetime):
        self.__datahora = datahora

    def get_compra_itens(self) -> list:
        return self.__compraitens

    def set_compra_itens(self, compraitens: list):
        self.__compraitens = compraitens

    def get_fornecedor(self) -> Fornecedor:
        return self.__fornecedor

    def set_fornecedor(self, fornecedor: Fornecedor):
        self.__fornecedor = fornecedor

    def get_id_fornecedor(self) -> int:
        return self.__id_fornecedor

    def set_id_fornecedor(self, idfor: int):
        self.__id_fornecedor = idfor

    def dados_principais(self):
        if type(self.get_fornecedor()) is Fornecedor:
            return self.get_fornecedor().dadosPrincipais()+" - "+str(self.get_valor_total())

    def Salvar(self):
        con = Conexao()
        strErro = con.insereCompra(self)
        if len(strErro)<=0:
            self.Gerar_pdf()
        return strErro


    def Deletar(self):
        text = ""
        sql = "delete from compraitem where IdCompra=" + str(self.get_id_compra()) + ";"
        str(Conexao().deletar(sql))
        sql = "delete from compra where IdCompra=" + str(self.get_id_compra()) + ";"
        return str(Conexao().deletar(sql))

    def Buscar(self, id):
        obj = self.Listar(" WHERE Idcompra="+str(id))[0]
        sql = "SELECT IdItem,IdCompra,Valor,Qtd FROM compraitem WHERE IdCompra="+str(id)+";"
        dados = Conexao().listar(sql)
        index = -1
        if dados is not None:
            for linha in dados:
                compra = Compraitem(int(linha[0]), int(linha[1]), float(linha[2]), int(linha[3]))
                compra.set_item(Item().listar(" WHERE IdITem="+str(linha[0])+";")[0])
                obj.get_compra_itens().insert(index + 1, compra)
        return  obj

    def Listar(self,where):
        sql = "SELECT IdCompra,IdFornecedor,ValorTotal,DataHora FROM compra " + where + ";"
        print(sql)
        dados = Conexao().listar(sql)
        lista = []
        index = -1
        if dados is not None:
            for linha in dados:
                compra = Compra(int(linha[0]), idfor=int(linha[1]), valortotal=float(linha[2]))
                compra.set_fornecedor(Fornecedor().Buscar(" WHERE pe.IdPessoa="+str(linha[1])))
                compra.set_id_fornecedor(compra.get_id_fornecedor())
                lista.insert(index + 1, compra)
        return lista

    def Mm2p(self,milimetros):
        return milimetros / 0.352777

    def Gerar_pdf(self):
        colunas=[]

        #caminho_completo = os.path.join(os.path.dirname(__file__), "..","Relatorios", "Relatorio_compra.pdf")
        cnv = canvas.Canvas("Relatorio_compra.pdf")

        cnv.drawString(0,0,' ')
        margem = 20
        linha = 280
        somaQtd = 0
        somaValor = 0.00

        cnv.setFont('Helvetica-Bold', 15)


        cnv.drawImage("Imagens/logo_fundo_branco.png",50,self.Mm2p(260),width=100, height=100)

        cnv.drawString(self.Mm2p(70), self.Mm2p(linha), "Tilapicultura do BERNARDÃO  ss ")
        linha -= 7
        cnv.drawString(self.Mm2p(70), self.Mm2p(linha), "Sitio Bica de Pedra - Itapuí, SP")
        linha -= 7
        cnv.drawString(self.Mm2p(75), self.Mm2p(linha), " CNPJ: 72.132.707/0001-62")
        linha -=2
        cnv.line(0, self.Mm2p(linha), self.Mm2p(15000), self.Mm2p(linha))
        linha -= 10
        cnv.drawString(self.Mm2p(75), self.Mm2p(linha), " Relátorio da Compra")
        cnv.setFont('Helvetica-Bold', 14)
        linha-=10
        cnv.drawString(self.Mm2p(margem), self.Mm2p(linha), "Fornecedor: "+ self.__fornecedor.dadosPrincipais())
        linha -= 10
        cnv.drawString(self.Mm2p(margem), self.Mm2p(linha), "Data da Compra: " + self.get_data_hora().strftime("%d/%m/%Y"))
        linha -= 15
        cnv.drawString(self.Mm2p(margem), self.Mm2p(linha), "Descrição")
        cnv.drawString(self.Mm2p(150), self.Mm2p(linha), "Qtd")
        cnv.drawString(self.Mm2p(170), self.Mm2p(linha), "Valor Total")
        linha -=2
        cnv.line(0,self.Mm2p(linha),self.Mm2p(15000),self.Mm2p(linha))
        linha = linha - 5
        cnv.setFont('Helvetica', 12)
        for it in self.__compraitens:
            cnv.drawString(self.Mm2p(margem), self.Mm2p(linha), str(it.get_item().get_descricao()))
            cnv.drawString(self.Mm2p(150), self.Mm2p(linha), str(it.get_qtd()))
            cnv.drawString(self.Mm2p(170), self.Mm2p(linha)," R$ " + str(it.get_valor()))
            linha-=3
            cnv.line(0, self.Mm2p(linha), self.Mm2p(15000), self.Mm2p(linha))
            somaQtd += it.get_qtd()
            somaValor += it.get_valor()
            linha = linha-4
        cnv.drawString(self.Mm2p(136), self.Mm2p(linha),"Total:   " + str(somaQtd))
        cnv.drawString(self.Mm2p(170), self.Mm2p(linha), " R$ " + str(somaValor))
        cnv.save()
        os.startfile("Relatorio_compra.pdf")



"""con = Compra().Buscar(8)
con.Gerar_pdf()"""