from datetime import datetime, timedelta
import unittest
from main import agendar_consulta, Consulta

class TestAgendarConsulta(unittest.TestCase):

    def test_valida_nome_vazio(self):
        consulta = Consulta(nome="", data=datetime.now() + timedelta(days=1),
                            hora=datetime.now().time(), duracao=30)
        with self.assertRaises(Exception):
            agendar_consulta(consulta)

    def test_valida_data_passado(self):
        consulta = Consulta(nome="Maria", data=datetime.now() - timedelta(days=1),
                            hora=datetime.now().time(), duracao=30)
        with self.assertRaises(Exception):
            agendar_consulta(consulta)

    def test_valida_hora_passado(self):
        consulta = Consulta(nome="João", data=datetime.now(),
                            hora=datetime.now().time() - timedelta(hours=1), duracao=30)
        with self.assertRaises(Exception):
            agendar_consulta(consulta)

    def test_valida_duracao_negativa(self):
        consulta = Consulta(nome="José", data=datetime.now() + timedelta(days=1),
                            hora=datetime.now().time(), duracao=-30)
        with self.assertRaises(Exception):
            agendar_consulta(consulta)

if __name__ == '__main__':
    unittest.main()
