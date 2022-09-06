import pessoa as p
import quadrado as q
import professor as prof

pessoa1 = p.Pessoa('012.345.678-00','Maria', 40)
print(f'cpf: {pessoa1.cpf} \n nome: {pessoa1.nome} \n idade: {pessoa1.idade}')

pessoa_fisica = p.PessoaFisica('098.765.543-21', 'Paulo', 59)
print(f'cpf: {pessoa_fisica.cpf} \n nome: {pessoa_fisica.nome} \n idade: {pessoa_fisica.idade}')
print(pessoa_fisica.criarMEI())

pessoa_juridica = p.PessoaJurica('Empresa SA', 2, '123456789')
print(f'nome: {pessoa_juridica.nome} \n idade: {pessoa_juridica.idade} \n cnpj: {pessoa_juridica.getCNPJ()}')

professor = prof.Professor('Pedro', 26, 4862)
print(f'salário líquido: {professor.getSalarioLiquido("123")}')

quadrado = q.Quadrado(5)
print(f' àrea do quadrado: {quadrado.area()} \n perímetro do quadrado: {quadrado.perimetro()}')


