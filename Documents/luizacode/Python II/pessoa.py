class Pessoa:
    def __init__ (self, cpf, nome, idade):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade

    def isFumante(self, tipo):
        if tipo.upper == 'F':
            return 'fumante'
        if tipo.upper == 'N':
            return "não fumante"
        else:
            return 'não especificado'

class PessoaFisica(Pessoa):
    def criarMEI(self):
        return 'MEI criado com sucesso'

class PessoaJurica(Pessoa):
    def __init__ (self, nome, idade, cnpj):
        self.cnpj = cnpj
        super().__init__(self, nome, idade)

    def getCNPJ(self):
        return self.cnpj