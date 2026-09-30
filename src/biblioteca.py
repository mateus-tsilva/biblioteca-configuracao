class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar(self, titulo, autor):
        livro = {"id": len(self.livros) + 1, "titulo": titulo, "autor": autor}
        self.livros.append(livro)
        return livro.copy()

    def buscar(self, termo):
        termo = termo.strip().casefold()
        return [livro.copy() for livro in self.livros
                if termo in livro["titulo"].casefold()]
