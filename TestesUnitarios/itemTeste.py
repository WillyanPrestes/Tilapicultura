import unittest
from Classes.item import Item


class TestItem(unittest.TestCase):

    def setUp(self):
        self.item_teste = Item(
            iditem=1,
            descricao="Teste",
            qtd=10,
            preco=51.52,
            tipo=0
        )

    def test_get_id_item(self):
        self.assertEqual(self.item_teste.get_id_item(), 1)

    def test_set_id_item(self):
        self.item_teste.set_id_item(2)
        self.assertEqual(self.item_teste.get_id_item(), 2)

    def test_get_descricao(self):
        self.assertEqual(self.item_teste.get_descricao(), "Teste")

    def test_set_descricao(self):
        self.item_teste.set_descricao("Novo Teste")
        self.assertEqual(self.item_teste.get_descricao(), "Novo Teste")

    def test_get_qtd(self):
        self.assertEqual(self.item_teste.get_qtd(), 10)

    def test_set_qtd(self):
        self.item_teste.set_qtd(20)
        self.assertEqual(self.item_teste.get_qtd(), 20)

    def test_get_preco(self):
        self.assertEqual(self.item_teste.get_preco(), 51.52)

    def test_set_preco(self):
        self.item_teste.set_preco(60.0)
        self.assertEqual(self.item_teste.get_preco(), 60.0)

    def test_get_tipo(self):
        self.assertEqual(self.item_teste.get_tipo(), 0)

    def test_set_tipo(self):
        self.item_teste.set_tipo(1)
        self.assertEqual(self.item_teste.get_tipo(), 1)

    def test_get_texto_tipo_item(self):
        self.assertEqual(self.item_teste.get_texto_tipo_item(), "Alimentos")

    def test_dados_principais(self):
        expected_result = "1-Teste-Alimentos"
        self.assertEqual(self.item_teste.dados_principais(), expected_result)


if __name__ == '__main__':
    unittest.main()
