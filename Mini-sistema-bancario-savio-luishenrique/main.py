import time
import os
from banco_brasil import conta,Banco,financiamento,imovel,cliente



#***************main**************

#tabela_contas = []
#financiaments = []
tabela_clientes = []
senha_admin = 'bomdia'

ademiros = [['Henrique',101010,5000,10000,157],['Savio',202020,10000,20000,147],['Governo',000000,1000000000000,10000000000000,177]]

e = []
for x in ademiros:
  client = cliente(x[0],x[1],x[2])
  e.append(conta(client,x[4],x[3]))
  
  
bank_caixa = Banco('Caixa',e[:],[])
e = []
people = [['Alfredo',303030,5000,10000,137],['Josefa',404040,10000,20000,127]]

for x in people:
  client = cliente(x[0],x[1],x[2])
  e.append(conta(client,x[4],x[3]))
  
bank_itau = Banco('Itau',e[:],[])


e = 0
h = 0
banks = []
banks.append(bank_caixa)
banks.append(bank_itau)
while h == 0:
  print('#'*36)
  print('#'*36)
  print(('#'*10) + '  BANCO 24H  '.upper() + ('#'*13) )
  print('#'*36)
  print('#'*36)
  print('#'*36 + '\n'*2)

  conta1 = int(input('Digite o número da conta -> '))
  os.system('clear')
  banco_name = int(input('\nDigite o número correspondente do Banco\n\n 1 Para CAIXA\n 2 Para o ITAU \n\n ->'))
  bank_atual = banks[banco_name - 1 ] 
  for finder in bank_atual.contas:
    if finder.ide == conta1 :
      cliente1 = finder.cliente.cpf
      h = 1
      time.sleep(2)
      break
    else:
      continue
      time.sleep(2)
power = 1
while power == 1:
  os.system('clear')
  print('#'*36)
  print('#'*36)
  print(('#'*10) + '  BANCO 24H  '.upper() + ('#'*13) )
  print('#'*36)
  print('#'*36)
  print('#'*36 + '\n'*3)
  opcao = input('#1- Fazer Transferência  \n#2- Mostrar Financiamentos \n#3- Mostrar dinhero total do Banco \n#4 Mostrar o total financiado \n#5 Fazer um novo financiamento  \n#6 Sacar ou depositar\n\n-> ')
  if opcao == '1':
    
    for k in bank_atual.contas:
        if k.ide == conta1:
          bank_sec = int(input('\nDigite o número correspondente do Banco da conta que irá receber\n\n 1 Para CAIXA\n 2 Para o ITAU \n\n ->'))
          conta2 = int(input('Digite o número da conta que você quer transferir -> '))
          bank_send = banks[bank_sec - 1]
          for verify in bank_send.contas:
            if verify.ide == conta2 and verify.ide != conta1:
              qnt = float(input('Digite a quantia que quer transferir -> '))
              k.transferencia(qnt,verify)
              break
          print(f'Seu saldo -> {k.saldo} R$')
          print(f'Saldo de {verify.cliente.nome} -> {verify.saldo} R$')
          input()
          break
  
  elif opcao == '2':
    
    for k in bank_atual.contas:
      if k.cliente.cpf == cliente1:
        for x in  k.cliente.financiamentos:
       	 	print(f'Tipo:{x.imovel.tipo}\nBanco:{x.banco.nome_do_banco}\nCódigo -> {x.imovel.codigo}\nValor:{x.imovel.valor}R$\nCPF:{x.cliente.cpf}\n\n')
         	
      input()
    
        
  elif opcao == '3':
    for x in banks:
      password = input('Digite a senha de admin -> ')
      banco_to_see = int(input('\nDigite o número correspondente do Banco\n\n 1 Para CAIXA\n 2 Para o ITAU \n\n ->'))
      banko = banks[banco_to_see - 1]
      if password == senha_admin:
        print(f'Total de valor no banco do(a) {banko.nome_do_banco} -> {banko.total_valor_contas()}R$')
        input()
        break
  elif opcao == '4':
  
    for k in bank_atual.contas:
      if k.cliente.cpf == cliente1:
        print(f'{k.cliente.total_financiado()}R$')
        print(f'Seu salario -> {k.cliente.salario}R$')
    input()
  elif opcao == '5':

      for k in bank_atual.contas:
        if k.cliente.cpf == cliente1:
          tipo = input('Digite o tipo de imovel -> ')
          valor = float(input('Digite o valor do Imovel -> '))
          cod = int(input('Digite o numero identificador/código -> '))
          imov = imovel(tipo,valor,cod)
          value_finan = int(input('Digite o valor do financiamento -> '))
          fin = financiamento(k.cliente,imov,bank_atual,value_finan,0)
    
          k.cliente.new_financiamento(fin,k)
          break
      time.sleep(2)
  elif opcao == '6':
    for k in bank_atual.contas:
      if k.ide == conta1:
        opcao = input('Você quer sacar(1) ou depositar(2) ? -> ')
        value = float(input(f'\n\nVocê optou em {opcao}. Digite o valor -> '))
        k.sacar_depositar(value,opcao)
    
    
            
  elif opcao == '7':
    quit()
  else:
    print('Erro! Digite a opção novamente!')   
    time.sleep(2)
          
        

  
