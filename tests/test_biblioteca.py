import unittest
from src.biblioteca import Biblioteca


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.b = Biblioteca()
        self.b.cadastrar("Dom Casmurro", "Machado de Assis")

    def test_cadastro(self):
        self.assertEqual(self.b.livros[0]["id"], 1)

    def test_campos_obrigatorios(self):
        for titulo, autor in [(" ", "Autor"), ("Livro", " ")]:
            with self.assertRaises(ValueError):
                self.b.cadastrar(titulo, autor)
        self.assertEqual(len(self.b.livros), 1)

    def test_busca_titulo(self):
        self.assertEqual(len(self.b.buscar(" CASMURRO ")), 1)

    def test_sem_resultado(self):
        self.assertEqual(self.b.buscar("inexistente"), [])
