import unittest
from datetime import datetime
from Classes.ajusteitem import AjusteItem
from Classes.item import Item

class TestAjusteItem(unittest.TestCase):

    def setUp(self):
        self.item = Item(iditem=1, descricao="Item de Teste", tipo=1)
        self.ajuste_item = AjusteItem(
            idajuste=1,
            descricao="Ajuste de Teste",
            datahora=datetime.now(),
            qtdatual=10,
            qtdmovimentacao=5,
            qtdnova=15,
            iditem=self.item.get_id_item(),
            item=self.item
        )

    def test_get_id_ajuste(self):
        self.assertEqual(self.ajuste_item.get_id_ajuste(), 1)

    def test_set_id_ajuste(self):
        self.ajuste_item.set_id_ajuste(2)
        self.assertEqual(self.ajuste_item.get_id_ajuste(), 2)

    def test_get_qtd_atual(self):
        self.assertEqual(self.ajuste_item.get_qtd_atual(), 10)

    def test_set_qtd_atual(self):
        self.ajuste_item.set_qtd_atual(20)
        self.assertEqual(self.ajuste_item.get_qtd_atual(), 20)

    def test_get_qtd_nova(self):
        self.assertEqual(self.ajuste_item.get_qtd_nova(), 15)

    def test_set_qtd_nova(self):
        self.ajuste_item.set_qtd_nova(25)
        self.assertEqual(self.ajuste_item.get_qtd_nova(), 25)

    def test_get_qtd_movimentacao(self):
        self.assertEqual(self.ajuste_item.get_qtd_movimentacao(), 5)

    def test_set_qtd_movimentacao(self):
        self.ajuste_item.set_qtd_movimentacao(10)
        self.assertEqual(self.ajuste_item.get_qtd_movimentacao(), 10)

    def test_get_id_item(self):
        self.assertEqual(self.ajuste_item.get_id_item(), 1)

    def test_set_id_item(self):
        self.ajuste_item.set_id_item(3)
        self.assertEqual(self.ajuste_item.get_id_item(), 3)

    def test_get_item(self):
        self.assertEqual(self.ajuste_item.get_item(), self.item)

    def test_set_item(self):
        new_item = Item(iditem=2, descricao="Novo Item", tipo=2)
        self.ajuste_item.set_item(new_item)
        self.assertEqual(self.ajuste_item.get_item(), new_item)

    def test_set_descricao(self):
        self.ajuste_item.set_descricao("Nova Descrição")
        self.assertEqual(self.ajuste_item.get_descricao(), "Nova Descrição")

    def test_get_descricao(self):
        self.assertEqual(self.ajuste_item.get_descricao(), "Ajuste de Teste")

    def test_validacao(self):
        self.ajuste_item.set_id_item(0)
        self.assertEqual(self.ajuste_item.validcao(), 'Item deve ser Selecionado \n')

        self.ajuste_item.set_id_item(1)  # Restaurando o id_item
        self.ajuste_item.set_descricao("")
        self.assertEqual(self.ajuste_item.validcao(), 'Descrição é Obrigatório\n')

        self.ajuste_item.set_descricao("Ajuste de Teste")  # Restaurando a descrição
        self.ajuste_item.set_qtd_movimentacao(0)
        self.assertEqual(self.ajuste_item.validcao(), 'Movimentacao deve ser DIFERENTE de ZERO \n')

    def test_salvar(self):
        self.assertEqual(self.ajuste_item.salvar(), '')

    def test_listar(self):
        result = self.ajuste_item.listar()
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, AjusteItem)

    def test_deletar(self):
        self.assertEqual(self.ajuste_item.deletar(1), '')


if __name__ == '__main__':
    unittest.main()
