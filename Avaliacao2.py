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

    def aumento(self, porcentagem):
        self.salario += self.salario * (porcentagem / 100)

    def info_funcionario(self): 
        return f"Nome: {self.nome}, CPF: {self.cpf}, Salário: {self.salario}"       

    @abstractmethod 
    def bonus(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, cpf, departamento, salario=10000):
        super().__init__(nome, cpf, salario)
        self.departamento = departamento

    def get_departamento(self):
        return self.departamento

    def set_departamento(self, novo_departamento):
        self.departamento = novo_departamento

    def bonus(self):
        self.salario += 500  

    def info_funcionario(self):
        return f"Gerente - {super().info_funcionario()}, Departamento: {self.departamento}"

class Faxineiro(Funcionario):
    def __init__(self, nome, cpf, turno, salario=3500):
        super().__init__(nome, cpf, salario)
        self.turno = turno

    def get_turno(self):
        return self.turno

    def set_turno(self, novo_turno):
        self.turno = novo_turno

    def bonus(self):
        self.salario += 100 

    def info_funcionario(self):
        return f"Faxineiro - {super().info_funcionario()}, Turno: {self.turno}"

class Estagiario(Funcionario):
    def __init__(self, nome, cpf, carga_horaria, salario=1500):
        super().__init__(nome, cpf, salario)
        self.carga_horaria = carga_horaria

    def get_horas_estagio(self):
        return self.carga_horaria
    
    def set_carga_horaria(self, novo_horario):
        self.carga_horaria = novo_horario

    def bonus(self):
        self.salario += 100

    def info_funcionario(self):
        return f"Estagiário - {super().info_funcionario()}, Horas de estágio: {self.carga_horaria}"

def main():
    gerente = Gerente("Carlos", "12345678900", "Financeiro")
    faxineiro = Faxineiro("Maria", "98765432100", "Noturno")
    estagiario = Estagiario("João", "11122233344", 20)

    print(gerente.info_funcionario())
    gerente.bonus()
    print("Salário após bônus:", gerente.get_salario())
    
    print(faxineiro.info_funcionario())
    faxineiro.bonus()
    print("Salário após bônus:", faxineiro.get_salario())

    print(estagiario.info_funcionario())
    estagiario.bonus()
    print("Salário após bônus:", estagiario.get_salario())

if __name__ == "__main__":
    main()
