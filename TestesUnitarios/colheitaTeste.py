import unittest
from datetime import datetime
from Classes.colheita import Colheita
from Classes.tanques import Tanque


class TestColheita(unittest.TestCase):

    def setUp(self):
        self.tanque_teste = Tanque(idtanque=1, descricao="Tanque de Teste", volume=100.0)
        self.colheita = Colheita(
            idcolheita=1,
            data=datetime.now(),
            qtd=50,
            pesomedio=2.5,
            idtanque=1,
            tanque=self.tanque_teste
        )

    def test_dados_principais(self):
        expected_result = f"{self.colheita.get_data_hora()}-{self.tanque_teste.dados_principais()}"
        self.assertEqual(self.colheita.dados_principais(), expected_result)

    def test_validacao(self):
        self.assertEqual(self.colheita.validcao(), '')

        self.colheita.set_id_tanque(0)
        self.assertEqual(self.colheita.validcao(), 'Selecione o Tanque \n')

        self.colheita.set_id_tanque(1)  # Restaura o tanque
        self.colheita.set_qtd(0)
        self.assertEqual(self.colheita.validcao(), 'Qtd deve ser MAIOR que ZERO\n')

        self.colheita.set_qtd(50)  # Restaura a quantidade
        self.colheita.set_peso_medio(0)
        self.assertEqual(self.colheita.validcao(), 'Peso Medio deve ser MAIOR que ZERO\n')


if __name__ == '__main__':
    unittest.main()
