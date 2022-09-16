from datetime import date
data_atual = date.today().year

dados = dict()

dados['Nome'] = str (input('Nome:')).upper()
dados['Ano de nascimento'] = int(input('Ano de nascimento:'))

idade = data_atual-dados['Ano de nascimento']

dados['CTPS'] = int(input('Carteira de trabalho[0 não tem]'))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação:'))
    dados['Salário'] = int(input('Salário:'))
    dados['Sexo'] = str(input('Sexo:')).upper()

    if dados['Sexo'] == 'M' or 'm':
        if idade >=61:
            print('Vc tem idade para se aposentar')
        else:
            tempo_restante = 61 - idade
            print(dados['Nome'],'faltam',tempo_restante,'anos para se aposentar.')

elif dados['Sexo'] == 'F' or 'f':
        if idade >= 56:
            print(dados['Nome'],'Você já tem idade para se aposentar.')
        else:
            tempo_restante = 56 - idade
            print(dados['Nome'],'faltam',tempo_restante,' anos para se aposentar.')

else:
    print('Fim do programa')

for k,v in dados.items():
    print('-',k,'tem o valor:',v)