#Abrir o Cardapio da lanchonete. Baseado em um arquivo TXT Externo.
contped = soma1 = soma2 = total = 0
card = open('cardapio.txt', 'r') #Declarar uma váriavel para o arquivo, abrir o arquivo e escolher o modo de leitura
print(card.read(),'\n') #Ler o arquivo
while True:
    pedido = int(input('Escolha o seu pedido: '))
    if pedido == 1:
        print('X-Burguer - (Tempo de Espera - 420 Segundo)')
        soma1 = 14.00
    elif pedido == 2:
        print('2 - X-Salada - (Tempo de Espera - 420 Segundos)')
        soma1 = 16.50
    elif pedido == 3:
        print('3 - X-Bacon - (Tempo de Espera - 420 Segundos)')
        soma1 = 18.50
    elif pedido == 4:
        print('4 - Cachorro Quente - Simples - (Tempo de Espera - 300 Segundos)')
        soma1 = 7.00
    elif pedido == 5:
        print('5 - Cachorro Quente - Completo - (Tempo de Espera - 300 Segundos)')
        soma1 = 9.00
    elif pedido == 6:
        print('6 - Coxinha - (Tempo de Espera - 25 Segundos)')
        soma1 = 2.50
    elif pedido == 7 :
        print('7 - Risoles - (Tempo de Espera - 25 Segundos)')
        soma1 = 2.00
    else:
        print('Pedido invalido, Tente novamente')
    continuar = str(input('Deseja realizar um segundo pedido? [S/N]'))
    if continuar in 'Nn':
        break
    else:
        while continuar in 'Ss':
         pedido2 = int(input('Escolha o seu segundo pedido: '))
         if pedido2 == 1:
             print('X-Burguer - (Tempo de Espera - 420 Segundo)')
             soma2 = 14.00
         elif pedido2 == 2:
             print('2 - X-Salada - (Tempo de Espera - 420 Segundos)')
             soma2 = 16.50
         elif pedido2 == 3:
             print('3 - X-Bacon - (Tempo de Espera - 420 Segundos)')
             soma2 = 18.50
         elif pedido2 == 4:
             print('4 - Cachorro Quente - Simples - (Tempo de Espera - 300 Segundos)')
             soma2 = 7.00
         elif pedido2 == 5:
             print('5 - Cachorro Quente - Completo - (Tempo de Espera - 300 Segundos)')
             soma2 = 9.00
         elif pedido2 == 6:
             print('6 - Coxinha - (Tempo de Espera - 25 Segundos)')
             soma2 = 2.50
         elif pedido2 == 7:
             print('7 - Risoles - (Tempo de Espera - 25 Segundos)')
             soma2 = 2.00
         else:
             print('Pedido invalido, Tente novamente')
         contped = 2
         if contped == 2:
            print('Você realizou dois pedidos.','\n')
            break
    if pedido == 1 and pedido2 == 1:
        print('Você pediu dois Hamburguer e ganhou um Suco Gratis.')
    if continuar in'Nn':
        break
    elif contped == 2:
        break

print(f'Seus pedidos estão sendo finalizados, por favor aguarde.\n')
total = soma1 + soma2
print(f'Total a Pagar R${total:.2f}\n')
print('Obrigado pela preferencia, volte sempre!')
card.close()