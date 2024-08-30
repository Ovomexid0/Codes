from abc import ABC, abstractmethod   

class Funcionario(ABC):
    def __init__(self, nome, cpf, salario=1500):
        self.nome = nome 
        self.cpf = cpf
        self.salario = salario

    def get_nome(self):    
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf

    def get_salario(self):
        return self.salario

    def set_salario(self, novo_salario):
        self.salario = novo_salario

    @abstractmethod 
    def bonus(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, cpf, departamento, salario=1500):
        super().__init__(nome, cpf, salario)
        self.departamento = departamento

    def get_departamento(self):
        return self.departamento

    def set_departamento(self, novo_departamento):
        self.departamento = novo_departamento

    def bonus(self):
        self.salario += 500  # Atualizando o salário com o bônus

class Faxineiro(Funcionario):
    def __init__(self, nome, cpf, turno, salario=1500):
        super().__init__(nome, cpf, salario)
        self.turno = turno

    def get_turno(self):
        return self.turno

    def set_turno(self, novo_turno):
        self.turno = novo_turno

    def bonus(self):
        self.salario += 100  # Atualizando o salário com o bônus

# Testando as classes no main
def main():
    gerente = Gerente("Carlos", "12345678900", "Financeiro")
    faxineiro = Faxineiro("Maria", "98765432100", "Noturno")

    # Testando os métodos
    print(gerente.get_nome(), gerente.get_salario())
    gerente.bonus()
    print("Salário após bônus:", gerente.get_salario())

    print(faxineiro.get_nome(), faxineiro.get_salario())
    faxineiro.bonus()
    print("Salário após bônus:", faxineiro.get_salario())

if __name__ == "__main__":
    main()
