class Endereco:
    def __init__(self, rua, numero, cidade, estado="Desconhecido"):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

    def get_rua(self):
        return self.rua
    def set_rua(self, nova_rua):
        self.rua = nova_rua

    def get_numero(self):
        return self.numero
    def set_numero(self, novo_numero):
        self.numero = novo_numero

    def get_cidade(self):
        return self.cidade
    def set_cidade(self, nova_cidade):
        self.cidade = nova_cidade

    def get_estado(self):
        return self.estado
    def set_estado(self, novo_estado):
        self.estado = novo_estado

    def endereco_completo(self):
        return f"{self.rua}, {self.numero} - {self.cidade}, {self.estado}"

class Pessoa:
    def __init__(self, nome, idade, endereco: Endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_idade(self):
        return self.idade
    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def get_endereco(self):
        return self.endereco
    def set_endereco(self, novo_endereco: Endereco):
        self.endereco = novo_endereco
        
    def info_pessoa(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco.endereco_completo()}"

if __name__ == "__main__":
    e1 = Endereco("Rua A", 123, "Cidade A", "Estado A")
    e2 = Endereco("Rua B", 456, "Cidade B")
    e3 = Endereco("Rua C", 789, "Cidade C", "Estado C")

    pessoa1 = Pessoa("João", 30, e1)
    pessoa2 = Pessoa("Maria", 25, e2)
    pessoa3 = Pessoa("Carlos", 40, e3)

    print(pessoa1.info_pessoa())
    print(pessoa2.info_pessoa())
    print(pessoa3.info_pessoa())

    pessoa1.set_nome("João Silva")
    pessoa2.get_endereco().set_cidade("Nova Cidade B")

    print(pessoa1.info_pessoa())
    print(pessoa2.info_pessoa())
