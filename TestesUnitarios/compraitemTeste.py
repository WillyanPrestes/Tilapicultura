import unittest
from Classes.compraitem import Compraitem
from Classes.item import Item

class TestCompraitem(unittest.TestCase):

    def setUp(self):
        self.item_teste = Item(iditem=1, descricao="Item de Teste", preco=10.0)
        self.compraitem = Compraitem(
            iditem=1,
            idcompra=1,
            valor=100.0,
            qtd=5,
            item=self.item_teste
        )

    def test_get_id_item(self):
        self.assertEqual(self.compraitem.get_id_item(), 1)

    def test_set_id_item(self):
        self.compraitem.set_id_item(2)
        self.assertEqual(self.compraitem.get_id_item(), 2)

    def test_get_id_compra(self):
        self.assertEqual(self.compraitem.get_id_compra(), 1)

    def test_set_id_compra(self):
        self.compraitem.set_id_compra(2)
        self.assertEqual(self.compraitem.get_id_compra(), 2)

    def test_get_valor(self):
        self.assertEqual(self.compraitem.get_valor(), 100.0)

    def test_set_valor(self):
        self.compraitem.set_valor(150.0)
        self.assertEqual(self.compraitem.get_valor(), 150.0)

    def test_get_qtd(self):
        self.assertEqual(self.compraitem.get_qtd(), 5)

    def test_set_qtd(self):
        self.compraitem.set_qtd(10)
        self.assertEqual(self.compraitem.get_qtd(), 10)

    def test_get_item(self):
        self.assertEqual(self.compraitem.get_item(), self.item_teste)

    def test_set_item(self):
        new_item = Item(iditem=2, descricao="Novo Item", preco=20.0)
        self.compraitem.set_item(new_item)
        self.assertEqual(self.compraitem.get_item(), new_item)

if __name__ == '__main__':
    unittest.main()
