aluno = {'nome': str(input('Nome: ')), 'Media': int(input('Media: '))}
if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situacao'] = 'Recuperacao'
else:
    aluno['Situacao'] = 'Reprovaod'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} = {v}')
