import unittest
from Classes.pessoa import Pessoa, PessoaFisica, PessoaJuridica, Fornecedor, Endereco, Municipio, EstadoFederal
import datetime


class TestPessoa(unittest.TestCase):

    def setUp(self):
        self.endereco_teste = Endereco(idendereco=1, logradouro="Rua Teste", bairro="Centro",
                                       numero=10, cep=12345678, id_municipio="1")
        self.pessoa_teste = Pessoa(id_pessoa=1, id_endereco=1, endereco=self.endereco_teste, telefone="123456789", tipo=0)

    def test_get_id_pessoa(self):
        self.assertEqual(self.pessoa_teste.get_id_pessoa(), 1)

    def test_set_id_pessoa(self):
        self.pessoa_teste.set_id_pessoa(2)
        self.assertEqual(self.pessoa_teste.get_id_pessoa(), 2)

    def test_get_id_endereco(self):
        self.assertEqual(self.pessoa_teste.get_id_endereco(), 1)

    def test_set_id_endereco(self):
        self.pessoa_teste.set_id_endereco(2)
        self.assertEqual(self.pessoa_teste.get_id_endereco(), 2)

    def test_get_endereco(self):
        self.assertEqual(self.pessoa_teste.get_endereco(), self.endereco_teste)

    def test_set_endereco(self):
        endereco_novo = Endereco(idendereco=2, logradouro="Rua Nova", bairro="Centro",
                                 numero=20, cep=87654321, id_municipio="2")
        self.pessoa_teste.set_endereco(endereco_novo)
        self.assertEqual(self.pessoa_teste.get_endereco(), endereco_novo)

    def test_set_telefone(self):
        self.pessoa_teste.set_telefone("987654321")
        self.assertEqual(self.pessoa_teste.get_telefone(), "987654321")

    def test_get_tipo(self):
        self.assertEqual(self.pessoa_teste.get_tipo(), 0)

    def test_set_tipo(self):
        self.pessoa_teste.set_tipo(1)
        self.assertEqual(self.pessoa_teste.get_tipo(), 1)


class TestPessoaFisica(unittest.TestCase):

    def setUp(self):
        self.endereco_teste = Endereco(idendereco=1, logradouro="Rua Teste", bairro="Centro",
                                       numero=10, cep=12345678, id_municipio="1")
        self.pessoa_fisica_teste = PessoaFisica(
            id_pessoa=1, id_endereco=1, endereco=self.endereco_teste,
            telefone="123456789", nome="Fulano", apelido="Fulano Apelido", rg="123456", cpf="987654321"
        )

    def test_get_nome(self):
        self.assertEqual(self.pessoa_fisica_teste.get_nome(), "Fulano")

    def test_set_nome(self):
        self.pessoa_fisica_teste.set_nome("Ciclano")
        self.assertEqual(self.pessoa_fisica_teste.get_nome(), "Ciclano")

    def test_get_apelido(self):
        self.assertEqual(self.pessoa_fisica_teste.get_apelido(), "Fulano Apelido")

    def test_set_apelido(self):
        self.pessoa_fisica_teste.set_apelido("Ciclano Apelido")
        self.assertEqual(self.pessoa_fisica_teste.get_apelido(), "Ciclano Apelido")

    def test_get_rg(self):
        self.assertEqual(self.pessoa_fisica_teste.get_rg(), "123456")

    def test_set_rg(self):
        self.pessoa_fisica_teste.set_rg("789012")
        self.assertEqual(self.pessoa_fisica_teste.get_rg(), "789012")

    def test_get_cpf(self):
        self.assertEqual(self.pessoa_fisica_teste.get_cpf(), "987654321")

    def test_set_cpf(self):
        self.pessoa_fisica_teste.set_cpf("123456789")
        self.assertEqual(self.pessoa_fisica_teste.get_cpf(), "123456789")

    def test_dados_principais(self):
        expected_result = "1-Fulano - Fulano Apelido"
        self.assertEqual(self.pessoa_fisica_teste.dados_principais(), expected_result)


class TestPessoaJuridica(unittest.TestCase):

    def setUp(self):
        self.endereco_teste = Endereco(idendereco=1, logradouro="Rua Teste", bairro="Centro",
                                       numero=10, cep=12345678, id_municipio="1")
        self.pessoa_juridica
