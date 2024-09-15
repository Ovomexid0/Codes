class Cliente(object):
    def __init__(self, cpf, nome=""):
        self.cpf = cpf
        self.nome = nome

    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def __str__(self):
        return f"{self.get_cpf()}, {self.get_nome()}"
    
class CarrinhoCompra(object):
    def __init__(self, num_pedido, o_cliente):
        self.num_pedido = num_pedido
        self.o_cliente = o_cliente
        self.l_produtos = []

    def get_pedido(self):
        return self.num_pedido
    def set_pedido(self, novo_pedido):
        self.num_pedido = novo_pedido

    def get_cliente(self):
        return self.o_cliente
    def set_cliente(self, novo_cliente):
        self.o_cliente = novo_cliente

    def get_produtos(self):
        return self.l_produtos
    def adiciona_produto(self, novo_produto):
        self.l_produtos.append(novo_produto)
    def mostra_carrinho(self):
     if not self.l_produtos:
        print("Carrinho vazio")
     else:
        print("Produtos no carrinho:")
        for produto in self.l_produtos:
            print(produto.get_nome())

class Produto(object):
    def __init__(self, idt, nome, preco=0.0, qtd=1):
        self.idt = idt
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def get_idt(self):
        return self.idt
    def set_idt(self, novo_idt):
        self.idt = novo_idt

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_preco(self):
        return self.preco
    def set_preco(self, novo_preco):
        self.preco = novo_preco

    def get_qtd(self):
        return self.qtd
    def set_qtd(self, nova_qtd):
        self.qtd = nova_qtd
    def __str__(self):
        return f"{self.get_idt()}, {self.get_nome()}, {self.get_preco()}, {self.get_qtd()}"

if __name__ == "__main__":
    Cliente1 = Cliente("123")
    print("Cpf do Cliente:", Cliente1.get_cpf())
    Cliente2 = Cliente("224", "Jorge")
    print(Cliente2)
    print("Nome alterado:", Cliente2.get_nome())
    Carrinho1 = CarrinhoCompra("12", Cliente2)
    print("Carrinho de compra: Número:", Carrinho1.get_pedido())
    p1_arroz = Produto("1", "arroz", 30.0)
    print(p1_arroz)
    p2_feijao = Produto("2", "feijão", 9.00, 3)
    print("Nome do cliente:", Carrinho1.get_cliente())
    Carrinho1.adiciona_produto(p1_arroz)
    Carrinho1.adiciona_produto(p2_feijao)
    print("Produtos no carrinho:")
    for produto in Carrinho1.get_produtos():
        print(produto)
    Cliente1.set_cpf("456")
    print("Novo CPF do Cliente1:", Cliente1.get_cpf())
    Carrinho1.set_pedido("99")
    print("Novo número de pedido:", Carrinho1.get_pedido())
    p1_arroz.set_nome("arroz integral")
    p1_arroz.set_preco(35.0)
    p1_arroz.set_qtd(2)
    print("Produto modificado:", p1_arroz)
    Carrinho1.mostra_carrinho()
