import unittest
from Classes.endereco import Endereco, EstadoFederal, Municipio


class TestEstadoFederal(unittest.TestCase):

    def setUp(self):
        self.estado = EstadoFederal(idestado="SP", uf="São Paulo", nome="São Paulo")

    def test_get_id_estado(self):
        self.assertEqual(self.estado.get_id_estado(), "SP")

    def test_set_id_estado(self):
        self.estado.set_id_estado("RJ")
        self.assertEqual(self.estado.get_id_estado(), "RJ")

    def test_get_uf(self):
        self.assertEqual(self.estado.get_uf(), "São Paulo")

    def test_set_uf(self):
        self.estado.set_uf("Rio de Janeiro")
        self.assertEqual(self.estado.get_uf(), "Rio de Janeiro")

    def test_get_nome(self):
        self.assertEqual(self.estado.get_nome(), "São Paulo")

    def test_set_nome(self):
        self.estado.set_nome("Rio de Janeiro")
        self.assertEqual(self.estado.get_nome(), "Rio de Janeiro")


class TestMunicipio(unittest.TestCase):

    def setUp(self):
        self.estado_teste = EstadoFederal(idestado="SP", uf="São Paulo", nome="São Paulo")
        self.municipio = Municipio(idmunicipio="1", idestado="SP", nome="Campinas", estado=self.estado_teste)

    def test_get_id_municipio(self):
        self.assertEqual(self.municipio.get_id_municipio(), "1")

    def test_set_id_municipio(self):
        self.municipio.set_id_municipio("2")
        self.assertEqual(self.municipio.get_id_municipio(), "2")

    def test_get_id_estado(self):
        self.assertEqual(self.municipio.get_id_estado(), "SP")

    def test_set_id_estado(self):
        self.municipio.set_id_estado("RJ")
        self.assertEqual(self.municipio.get_id_estado(), "RJ")

    def test_get_estado_federal(self):
        self.assertEqual(self.municipio.get_estado_federal(), self.estado_teste)

    def test_set_estado_federal(self):
        new_estado = EstadoFederal(idestado="RJ", uf="Rio de Janeiro", nome="Rio de Janeiro")
        self.municipio.set_estado_federal(new_estado)
        self.assertEqual(self.municipio.get_estado_federal(), new_estado)

    def test_get_nome(self):
        self.assertEqual(self.municipio.get_nome(), "Campinas")

    def test_set_nome(self):
        self.municipio.set_nome("São Paulo")
        self.assertEqual(self.municipio.get_nome(), "São Paulo")


class TestEndereco(unittest.TestCase):

    def setUp(self):
        self.estado_teste = EstadoFederal(idestado="SP", uf="São Paulo", nome="São Paulo")
        self.municipio_teste = Municipio(idmunicipio="1", idestado="SP", nome="Campinas", estado=self.estado_teste)
        self.endereco = Endereco(
            idendereco=1,
            logradouro="Rua Teste",
            bairro="Bairro Teste",
            numero=123,
            cep=12345678,
            id_municipio="1",
            municipio=self.municipio_teste
        )

    def test_get_id_endereco(self):
        self.assertEqual(self.endereco.get_id_endereco(), 1)

    def test_set_id_endereco(self):
        self.endereco.set_id_endereco(2)
        self.assertEqual(self.endereco.get_id_endereco(), 2)

    def test_get_logradouro(self):
        self.assertEqual(self.endereco.get_logradouro(), "Rua Teste")

    def test_set_logradouro(self):
        self.endereco.set_logradouro("Avenida Teste")
        self.assertEqual(self.endereco.get_logradouro(), "Avenida Teste")

    def test_get_bairro(self):
        self.assertEqual(self.endereco.get_bairro(), "Bairro Teste")

    def test_set_bairro(self):
        self.endereco.set_bairro("Novo Bairro")
        self.assertEqual(self.endereco.get_bairro(), "Novo Bairro")

    def test_get_cep(self):
        self.assertEqual(self.endereco.get_cep(), 12345678)

    def test_set_cep(self):
        self.endereco.set_cep(87654321)
        self.assertEqual(self.endereco.get_cep(), 87654321)

    def test_get_numero(self):
        self.assertEqual(self.endereco.get_numero(), 123)

    def test_set_numero(self):
        self.endereco.set_numero(456)
        self.assertEqual(self.endereco.get_numero(), 456)

    def test_get_id_municipio(self):
        self.assertEqual(self.endereco.get_id_municipio(), "1")

    def test_set_id_municipio(self):
        self.endereco.set_id_municipio("2")
        self.assertEqual(self.endereco.get_id_municipio(), "2")

    def test_get_municipio(self):
        self.assertEqual(self.endereco.get_municipio(), self.municipio_teste)

    def test_set_municipio(self):
        new_municipio = Municipio(idmunicipio="2", idestado="SP", nome="São Paulo", estado=self.estado_teste)
        self.endereco.set_municipio(new_municipio)
        self.assertEqual(self.endereco.get_municipio(), new_municipio)


if __name__ == '__main__':
    unittest.main()
