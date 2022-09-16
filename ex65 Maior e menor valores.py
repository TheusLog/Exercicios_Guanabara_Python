#num = int(input('Digite um Numero '))
#resp = str(input('Quer continuar[S/N]: ')).strip().upper()
cont = soma = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    if resp in 'Ss':
        num = int(input('Digite um Numero '))
        resp = str(input('Quer continuar[S/N]: ')).strip().upper()
        cont += 1
        soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('Voce digitou {} numeros e a soma foi {} e a media {:.2f} '. format(cont, soma, media))
print('O maior numero foi {} e o menor foi o {}'.format(maior, menor))


