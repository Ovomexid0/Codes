from abc import ABC, abstractmethod

# Interface Supermercado
class Supermercado(ABC):
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def print_items(self):
        pass

    @abstractmethod
    def delete(self, index):
        pass

# Implementação de Supermercado Array
class SupermercadoArray(Supermercado):
    def __init__(self):
        self.items = []  # Lista sem limite de tamanho

    def add(self, item):
        self.items.append(item)
        print(f"Item '{item}' adicionado.")

    def print_items(self):
        print("##################")
        if not self.items:
            print("Lista de supermercado vazia")
        else:
            for i, item in enumerate(self.items):
                print(f"{i + 1} - {item}")
        print("##################")

    def delete(self, index):
        if 0 <= index < len(self.items):
            removed_item = self.items.pop(index)
            print(f"Item '{removed_item}' na posição {index + 1} removido.")
        else:
            print(f"Erro: índice inválido ({index + 1})")

# Função principal de execução
def main():
    supermercado = SupermercadoArray()

    while True:
        print("\nLista de compras")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Remover")
        print("4 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: Por favor, insira um número válido (1, 2, 3 ou 4).")
            continue

        if opcao == 1:
            item = input("Digite o item a ser inserido: ")
            supermercado.add(item)
        elif opcao == 2:
            supermercado.print_items()
        elif opcao == 3:
            try:
                index = int(input("Digite a posição do item a ser removido: ")) - 1
                supermercado.delete(index)
            except ValueError:
                print("Erro: Por favor, insira um número válido para a posição.")
        elif opcao == 4:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
