peso = float(input('Qual seu Peso: '))
altura = float(input('Qual a sua Altura: '))
imc = peso / (altura * altura)
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce é pedreiro para ficar andando com uma tauba de 30 no peito???')
elif imc >= 18.5 <= 25:
    print('Vai fica GRANDE POHA, ta pequeno ainda.')
elif imc >= 25.1 <= 30:
    print('Cuidado poha quer ficar com  barriga de cerveja?')
elif imc >= 30.01 <= 40:
    print('Ta ficando louco filha da puta, malhar esse banhar seu porco')
elif imc > 40:
    print('Ola moby dyck!!!')

