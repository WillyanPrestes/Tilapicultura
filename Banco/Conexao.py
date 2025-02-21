import mysql
from mysql.connector import connect




class Conexao:
    def __init__(self):
        self.messageErro=""
        self.__con = connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='12345678',
            database='dbtilapicultura'
        )
        pass


    @staticmethod
    def executa_sql(sql):
        con = connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='12345678',
            database='dbtilapicultura'
        )
        cur = con.cursor()
        cur.execute(sql)
        con.close()

    def __conecta(self):
        config = {}
        """with open('Banco/stringConexao.txt', 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                chave, valor = linha.strip().split('=')
                config[chave] = valor
        self.__con = connect(
            host=str(config['host']),
            port=3306,
            user=str(config['usuario']),
            passwd=str(config['senha']),
            database=str(config['banco'])
        )"""
    """def __conecta(self):
        self.__con = connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='12345678',
            database='dbtilapicultura'
        )"""
    __cur = 0

    def insere(self, sql, registros):
        try:
            self.messageErro = ""
            self.__conecta()
            self.__cur = self.__con.cursor()
            self.__cur.execute(sql, registros)
            self.__con.commit()
            self.__con.close()
        except mysql.connector.Error as err:
            from mysqlx import errorcode
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.messageErro = "Erro de acesso negado: Verifique as credenciais de conexão."
                print(self.messageErro)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.messageErro="Banco de dados não existe."
                print(self.messageErro)
            else:
                self.messageErro="Erro MySQL: {}".format(err)
                print(self.messageErro)
        else:
            print("Inserção de dados bem-sucedida.")
        finally:
            if self.__con.is_connected():
                self.__cur.close()
                self.__con.close()
            return self.messageErro

    def insereCompra(self,compra):
        try:
            idCompra = 0
            self.messageErro = ""
            self.__conecta()
            self.__cur = self.__con.cursor()
            if compra.get_id_compra() <= 0:
                sqlCompra="insert into compra (IdFornecedor ,ValorTotal,DataHora) values (%s, %s, %s);"
                registros=(compra.get_fornecedor().get_id_fornecedor(), compra.get_valor_total(), compra.get_data_hora())
                self.__cur.execute(sqlCompra, registros)
                idCompra = self.__cur.lastrowid

                for item in compra.get_compra_itens():
                    sqlCompraItem="insert into compraitem (IdCompra,IdItem,Valor,Qtd) values (%s,%s,%s,%s);"
                    registros=(str(idCompra), item.get_id_item(),item.get_valor(),item.get_qtd())
                    self.__cur.execute(sqlCompraItem, registros)
            self.__con.commit()
            self.__con.close()
        except mysql.connector.Error as err:
            from mysqlx import errorcode
            print(self.messageErro)
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.messageErro = "Erro de acesso negado: Verifique as credenciais de conexão."
                print(self.messageErro)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.messageErro = "Banco de dados não existe."
                print(self.messageErro)
            else:
                self.messageErro = "Erro MySQL: {}".format(err)
                print(self.messageErro)
        else:
            print("Inserção de dados bem-sucedida.")
        finally:
            if self.__con.is_connected():
                self.__cur.close()
                self.__con.close()
            return self.messageErro
    def insereFornecedor(self, fornecedor):
        try:
            idEndereco= 0
            IdPessoa = 0
            self.messageErro = ""
            self.__conecta()
            self.__cur = self.__con.cursor()
            if fornecedor.get_id_pessoa() <= 0:
                sqlEndereco="insert into Endereco(IdMunicipio,Logradouro,Bairro,Numero,Cep) values (%s,%s,%s,%s,%s);"
                registros=(fornecedor.get_pessoa().get_endereco().get_id_municipio(),
                           fornecedor.get_pessoa().get_endereco().get_logradouro(),
                           fornecedor.get_pessoa().get_endereco().get_bairro(),
                           fornecedor.get_pessoa().get_endereco().get_numero(),
                           fornecedor.get_pessoa().get_endereco().get_cep())
                self.__cur.execute(sqlEndereco, registros)
                idEndereco = self.__cur.lastrowid

                sqlPessoa=""
                if fornecedor.get_pessoa().get_tipo() == 0:
                    registros = (idEndereco,fornecedor.get_pessoa().get_nome(),fornecedor.get_pessoa().get_apelido(),
                               fornecedor.get_pessoa().get_rg(),fornecedor.get_pessoa().get_cpf())
                    sqlPessoa = "insert into Pessoa(IdEndereco,Nome,Apelido,RG,CPF,tipoObjeto) values (%s,%s,%s,%s,%s,0);"
                else:
                    registros = (idEndereco, fornecedor.get_pessoa().get_razao_social(), fornecedor.get_pessoa().get_nome_fantasia(),
                                 fornecedor.get_pessoa().get_cnpj(), fornecedor.get_pessoa().get_ie())
                    sqlPessoa = "insert into Pessoa(IdEndereco,RazaoSocial,NomeFantasia,Cnpj,InscricaoEstadual,tipoObjeto) values (%s,%s,%s,%s,%s,1);"
                self.__cur.execute(sqlPessoa, registros)
                IdPessoa = self.__cur.lastrowid

                self.__cur.execute('insert into fornecedor (IdPessoa) values('+str(IdPessoa)+');')
            else:
                if fornecedor.get_pessoa().get_tipo() == 0:
                    registros = (fornecedor.get_pessoa().get_nome(),
                                 fornecedor.get_pessoa().get_apelido(),
                                 fornecedor.get_pessoa().get_rg(),
                                 fornecedor.get_pessoa().get_cpf())
                    sql="update pessoa set Nome=%s, Apelido=%s, Rg=%s,CPF=%s WHERE IdPessoa="+str(fornecedor.get_id_pessoa())+";"
                    self.__cur.execute(sql, registros)
                else:
                    registros = (fornecedor.get_pessoa().get_razao_social(),
                                 fornecedor.get_pessoa().get_nome_fantasia(),
                                 fornecedor.get_pessoa().get_cnpj(),
                                 fornecedor.get_pessoa().get_ie())
                    sql = ("update pessoa set RazaoSocial=%s, NomeFantasia=%s, Cnpj=%s,InscricaoEstadual=%s "
                           "WHERE IdPessoa=" + str(fornecedor.get_id_pessoa()) + ";")
                    self.__cur.execute(sql, registros)

                registros = (fornecedor.get_pessoa().get_endereco().get_id_municipio(),
                             fornecedor.get_pessoa().get_endereco().get_logradouro(),
                             fornecedor.get_pessoa().get_endereco().get_bairro(),
                             fornecedor.get_pessoa().get_endereco().get_numero(),
                             fornecedor.get_pessoa().get_endereco().get_cep())
                sql = (" update endereco set IdMunicipio=%s, Logradouro=%s, Bairro=%s, Numero=%s, Cep=%s WHERE IdEndereco="
                      + str(fornecedor.get_pessoa().get_id_endereco()))
                self.__cur.execute(sql, registros)

            self.__con.commit()
            self.__con.close()
        except mysql.connector.Error as err:
            from mysqlx import errorcode
            print(self.messageErro)
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.messageErro = "Erro de acesso negado: Verifique as credenciais de conexão."
                print(self.messageErro)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.messageErro="Banco de dados não existe."
                print(self.messageErro)
            else:
                self.messageErro="Erro MySQL: {}".format(err)
                print(self.messageErro)
        else:
            print("Inserção de dados bem-sucedida.")
        finally:
            if self.__con.is_connected():
                self.__cur.close()
                self.__con.close()
            return self.messageErro

    def deletar(self, sql):
        try:
            self.__conecta()
            self.messageErro = ""
            self.__cur = self.__con.cursor()
            self.__cur.execute(sql)
            self.__con.commit()
            self.__con.close()
        except mysql.connector.Error as err:
            from mysqlx import errorcode
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.messageErro = "Erro de acesso negado: Verifique as credenciais de conexão."
                print(self.messageErro)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.messageErro = "Banco de dados não existe."
                print(self.messageErro)
            else:
                self.messageErro = "Erro MySQL: {}".format(err)
                print(self.messageErro)
        else:
            print("Exclusao de dados bem-sucedida.")
        finally:
            if self.__con.is_connected():
                self.__cur.close()
                self.__con.close()
            return self.messageErro

    def listar(self, sql):
        try:
            self.__conecta()
            self.__cur = self.__con.cursor()
            self.__cur.execute(sql)
            listaDados = self.__cur.fetchall()
            self.__cur.close()
            self.__con.close()

        except mysql.connector.Error as err:
            from mysqlx import errorcode
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Erro de acesso negado: Verifique as credenciais de conexão.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe.")
            else:
                print("Erro MySQL: {}".format(err))
        else:
            return listaDados
            print("Consulta de dados bem-sucedida.")
        finally:
            if self.__con.is_connected():
                self.__cur.close()
                self.__con.close()


