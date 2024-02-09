import unittest
from main import agendar_consulta, Consulta


class TestAgendarConsulta(unittest.TestCase):

    def test_valida_duracao(self):
        consulta = Consulta(nome="João", data="2023-03-01",
                            hora="10:00", duracao=0)
        with self.assertRaises(Exception):
            agendar_consulta(consulta)

    def test_valida_data(self):
        consulta = Consulta(nome="Maria", data="01/01/2023",
                            hora="10:00", duracao=30)
        with self.assertRaises(Exception):
            agendar_consulta(consulta)

    def test_valida_hora(self):
        consulta = Consulta(nome="José", data="2023-01-01",
                            hora="10:00:00", duracao=30)
        with self.assertRaises(Exception):
            agendar_consulta(consulta)

    def test_verifica_disponibilidade(self):
        consulta1 = Consulta(nome="João", data="2023-01-01",
                             hora="10:00", duracao=30)
        consulta2 = Consulta(nome="Maria", data="2023-01-01",
                             hora="10:00", duracao=30)
        agendar_consulta(consulta1)
        with self.assertRaises(Exception):
            agendar_consulta(consulta2)

    def test_agenda_consulta(self):
        consulta = Consulta(nome="José", data="2023-01-02",
                            hora="15:00", duracao=60)
        response = agendar_consulta(consulta)
        self.assertEqual(response["message"], "Consulta agendada com sucesso!")


class TestAgendarConsulta(unittest.TestCase):

    def test_valida_duracao(self):
        consulta = Consulta(nome="João", data="2023-03-01",
                            hora="10:00", duracao=0)
        with self.assertRaises(Exception):
            agendar_consulta(consulta)

    def test_valida_data(self):
        consulta = Consulta(nome="Maria", data="01/01/2023",
                            hora="10:00", duracao=30)
        with self.assertRaises(Exception):
            agendar_consulta(consulta)

    def test_valida_hora(self):
        consulta = Consulta(nome="José", data="2023-01-01",
                            hora="10:00:00", duracao=30)
        with self.assertRaises(Exception):
            agendar_consulta(consulta)

    def test_verifica_disponibilidade(self):
        consulta1 = Consulta(nome="João", data="2023-01-01",
                             hora="10:00", duracao=30)
        consulta2 = Consulta(nome="Maria", data="2023-01-01",
                             hora="10:00", duracao=30)
        agendar_consulta(consulta1)
        with self.assertRaises(Exception):
            agendar_consulta(consulta2)

    def test_agenda_consulta(self):
        consulta = Consulta(nome="José", data="2023-01-02",
                            hora="15:00", duracao=60)
        response = agendar_consulta(consulta)
        self.assertEqual(response["message"], "Consulta agendada com sucesso!")
