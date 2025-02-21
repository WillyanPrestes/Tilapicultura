import unittest
from Classes.tanques import Tanque

class TestTanque(unittest.TestCase):

    def setUp(self):
        self.tanque = Tanque(
            idtanque=1,
            descricao="Tanque de Teste",
            qtdpeixe=100,
            ph=7.0,
            temperatura=25.0,
            volume=200.0,
            fasedesenvolvimento=1
        )

    def test_get_id_tanque(self):
        self.assertEqual(self.tanque.get_id_tanque(), 1)

    def test_set_id_tanque(self):
        self.tanque.set_id_tanque(2)
        self.assertEqual(self.tanque.get_id_tanque(), 2)

    def test_get_descricao(self):
        self.assertEqual(self.tanque.get_descricao(), "Tanque de Teste")

    def test_set_descricao(self):
        self.tanque.set_descricao("Novo Tanque")
        self.assertEqual(self.tanque.get_descricao(), "Novo Tanque")

    def test_get_qtd_peixe(self):
        self.assertEqual(self.tanque.get_qtd_peixe(), 100)

    def test_set_qtd_peixe(self):
        self.tanque.set_qtd_peixe(150)
        self.assertEqual(self.tanque.get_qtd_peixe(), 150)

    def test_get_ph(self):
        self.assertEqual(self.tanque.get_ph(), 7.0)

    def test_set_ph(self):
        self.tanque.set_ph(6.5)
        self.assertEqual(self.tanque.get_ph(), 6.5)

    def test_get_temperatura(self):
        self.assertEqual(self.tanque.get_temperatura(), 25.0)

    def test_set_temperatura(self):
        self.tanque.set_temperatura(28.0)
        self.assertEqual(self.tanque.get_temperatura(), 28.0)

    def test_get_volume(self):
        self.assertEqual(self.tanque.get_volume(), 200.0)

    def test_set_volume(self):
        self.tanque.set_volume(250.0)
        self.assertEqual(self.tanque.get_volume(), 250.0)

    def test_get_fase_desenvolvimento(self):
        self.assertEqual(self.tanque.get_fase_desenvolvimento(), 1)

    def test_set_fase_desenvolvimento(self):
        self.tanque.set_fase_desenvolvimento(2)
        self.assertEqual(self.tanque.get_fase_desenvolvimento(), 2)

    def test_texto_fase_desenvolvimento(self):
        self.assertEqual(self.tanque.texto_fase_desenvolvimento(), "Juvenil")

    def test_dados_principais(self):
        expected_result = "1-Tanque de Teste de 200.0 mt³"
        self.assertEqual(self.tanque.dados_principais(), expected_result)

    def test_salvar(self):
        self.assertEqual(self.tanque.salvar(), '')

    def test_validacao(self):
        self.tanque.set_ph(0)
        self.assertEqual(self.tanque.validcao(), 'PH deve ser Maior que ZERO \n')

        self.tanque.set_ph(7.0)  # Restaurando o pH
        self.tanque.set_descricao("")
        self.assertEqual(self.tanque.validcao(), 'Descrição é Obrigatório\n')

        self.tanque.set_descricao("Tanque de Teste")  # Restaurando a descrição
        self.tanque.set_volume(0)
        self.assertEqual(self.tanque.validcao(), 'Volume deve ser MAIOR que ZERO')

        self.tanque.set_volume(200.0)  # Restaurando o volume
        self.tanque.set_temperatura(0)
        self.assertEqual(self.tanque.validcao(), 'Temperatura deve ser MAIOR que ZERO')

    def test_listar(self):
        result = self.tanque.listar()
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Tanque)

    def test_deletar(self):
        self.assertEqual(self.tanque.deletar(1), '')


if __name__ == '__main__':
    unittest.main()
