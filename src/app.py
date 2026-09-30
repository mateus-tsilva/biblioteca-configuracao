from src.biblioteca import Biblioteca


def main():
    biblioteca = Biblioteca()
    while True:
        opcao = input("\n1 - Cadastrar | 2 - Consultar | 0 - Sair: ").strip()
        if opcao == "0":
            break
        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            try:
                print("Cadastrado:", biblioteca.cadastrar(titulo, autor))
            except ValueError as erro:
                print("Erro:", erro)
        elif opcao == "2":
            print(biblioteca.buscar(input("Busca: ")))
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
