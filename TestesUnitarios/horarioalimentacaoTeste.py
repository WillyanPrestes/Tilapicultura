import unittest
import datetime
from Classes.tanques import Tanque
from Classes.horarioalimentacao import Horario_Alimentacao


class TestHorarioAlimentacao(unittest.TestCase):

    def setUp(self):
        self.tanque_teste = Tanque(idtanque=1, descricao="Tanque Teste", volume=100.0)
        self.horario_alimentacao = Horario_Alimentacao(
            idhorario=1,
            descricao="Horário Teste",
            data=datetime.datetime.now(),
            idtanque=1,
            tanque=self.tanque_teste
        )

    def test_get_id_horario(self):
        self.assertEqual(self.horario_alimentacao.get_id_horario(), 1)

    def test_set_id_horario(self):
        self.horario_alimentacao.set_id_horario(2)
        self.assertEqual(self.horario_alimentacao.get_id_horario(), 2)

    def test_get_data_hora(self):
        self.assertIsInstance(self.horario_alimentacao.get_data_hora(), datetime.datetime)

    def test_set_data_hora(self):
        new_date = datetime.datetime(2023, 1, 1, 12, 0, 0)
        self.horario_alimentacao.set_data_hora(new_date)
        self.assertEqual(self.horario_alimentacao.get_data_hora(), new_date)

    def test_get_descricao(self):
        self.assertEqual(self.horario_alimentacao.get_descricao(), "Horário Teste")

    def test_set_descricao(self):
        self.horario_alimentacao.set_descricao("Novo Horário")
        self.assertEqual(self.horario_alimentacao.get_descricao(), "Novo Horário")

    def test_get_id_tanque(self):
        self.assertEqual(self.horario_alimentacao.get_id_tanque(), 1)

    def test_set_id_tanque(self):
        self.horario_alimentacao.set_id_tanque(2)
        self.assertEqual(self.horario_alimentacao.get_id_tanque(), 2)

    def test_get_tanque(self):
        self.assertEqual(self.horario_alimentacao.get_tanque(), self.tanque_teste)

    def test_set_tanque(self):
        new_tanque = Tanque(idtanque=2, descricao="Novo Tanque", volume=150.0)
        self.horario_alimentacao.set_tanque(new_tanque)
        self.assertEqual(self.horario_alimentacao.get_tanque(), new_tanque)

    def test_dados_principais(self):
        expected_result = str(self.horario_alimentacao.get_data_hora()) + '-' + self.tanque_teste.dados_principais()
        self.assertEqual(self.horario_alimentacao.dados_principais(), expected_result)


if __name__ == '__main__':
    unittest.main()
