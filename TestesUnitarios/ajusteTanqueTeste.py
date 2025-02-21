import unittest
from datetime import datetime
from Classes.ajustetanque import AjusteTanque
from Classes.tanques import Tanque

class TestAjusteTanque(unittest.TestCase):

    def setUp(self):
        self.tanque = Tanque(idtanque=1, descricao="Tanque de Teste", volume=100.0)
        self.ajuste_tanque = AjusteTanque(
            idajuste=1,
            descricao="Ajuste de Teste",
            qtdanterior=50,
            qtdmovimentacao=20,
            qtdnova=70,
            idtanque=self.tanque.get_id_tanque(),
            tanque=self.tanque
        )

    def test_get_id_ajuste(self):
        self.assertEqual(self.ajuste_tanque.get_id_ajuste(), 1)

    def test_set_id_ajuste(self):
        self.ajuste_tanque.set_id_ajuste(2)
        self.assertEqual(self.ajuste_tanque.get_id_ajuste(), 2)

    def test_get_descricao(self):
        self.assertEqual(self.ajuste_tanque.get_descricao(), "Ajuste de Teste")

    def test_set_descricao(self):
        self.ajuste_tanque.set_descricao("Novo Ajuste")
        self.assertEqual(self.ajuste_tanque.get_descricao(), "Novo Ajuste")

    def test_get_qtd_anterior(self):
        self.assertEqual(self.ajuste_tanque.get_qtd_anterior(), 50)

    def test_set_qtd_anterior(self):
        self.ajuste_tanque.set_qtd_anterior(60)
        self.assertEqual(self.ajuste_tanque.get_qtd_anterior(), 60)

    def test_get_qtd_nova(self):
        self.assertEqual(self.ajuste_tanque.get_qtd_nova(), 70)

    def test_set_qtd_nova(self):
        self.ajuste_tanque.set_qtd_nova(80)
        self.assertEqual(self.ajuste_tanque.get_qtd_nova(), 80)

    def test_get_qtd_movimentacao(self):
        self.assertEqual(self.ajuste_tanque.get_qtd_movimentacao(), 20)

    def test_set_qtd_movimentacao(self):
        self.ajuste_tanque.set_qtd_movimentacao(30)
        self.assertEqual(self.ajuste_tanque.get_qtd_movimentacao(), 30)

    def test_get_id_tanque(self):
        self.assertEqual(self.ajuste_tanque.get_id_tanque(), 1)

    def test_set_id_tanque(self):
        self.ajuste_tanque.set_id_tanque(3)
        self.assertEqual(self.ajuste_tanque.get_id_tanque(), 3)

    def test_get_tanque(self):
        self.assertEqual(self.ajuste_tanque.get_tanque(), self.tanque)

    def test_set_tanque(self):
        new_tanque = Tanque(idtanque=2, descricao="Novo Tanque", volume=150.0)
        self.ajuste_tanque.set_tanque(new_tanque)
        self.assertEqual(self.ajuste_tanque.get_tanque(), new_tanque)

    def test_validacao(self):
        self.ajuste_tanque.set_id_tanque(0)
        self.assertEqual(self.ajuste_tanque.validcao(), 'Tanque deve ser Selecionado \n')

        self.ajuste_tanque.set_id_tanque(1)
        self.ajuste_tanque.set_descricao("")
        self.assertEqual(self.ajuste_tanque.validcao(), 'Descrição é Obrigatório\n')

        self.ajuste_tanque.set_descricao("Ajuste de Teste")
        self.ajuste_tanque.set_qtd_movimentacao(0)
        self.assertEqual(self.ajuste_tanque.validcao(), 'Movimentacao deve ser maior que zero \n')

    def test_salvar(self):
        self.assertEqual(self.ajuste_tanque.salvar(), '')

    def test_listar(self):
        result = self.ajuste_tanque.listar()
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, AjusteTanque)

    def test_deletar(self):
        self.assertEqual(self.ajuste_tanque.deletar(1), '')


if __name__ == '__main__':
    unittest.main()
