class Professor:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def __getSalario(self):
        return float(self.salario)
    
    def getSalarioLiquido(self, id):
        return self.__getSalario() * 0.84 if id == '123' else 'acesso negado'
