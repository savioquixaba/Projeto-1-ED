class imovel:
    def __init__(self,tipo,valor,codigo):
      self._tipo = tipo
      self._valor = valor  
      self._codigo = codigo
    
    @property
    def tipo(self):
      return self._tipo
    @property
    def valor(self):
      return self._valor
    @property
    def codigo(self):
      return self._codigo
  
    @tipo.setter
    def tipo(self,new_tipo):
      self._tipo = new_tipo      
    @valor.setter
    def valor(self,new_valor):
      self._valor = new_valor
    @codigo.setter
    def codigo(self,new_codigo):
      self._codigo = new_codigo

    def __str__(self):
      return f'Código: {self._codigo} Tipo: {self._tipo}  Valor:       {self._valor}R$'
class Banco:
    def __init__(self, nome_do_banco, contas = [], financiamentos = []):
        self._nome_do_banco = nome_do_banco
        self._contas = contas
        self._financiamentos = financiamentos
    
#Gets
    @property
    def nome_do_banco(self):
        return self._nome_do_banco
    
    @property
    def contas(self):
        return self._contas
    
    @property
    def financiamentos(self):
        return self._financiamentos
    
#Setts
    @nome_do_banco.setter
    def nome_do_banco(self, novo_banco):
        self._nome_do_banco = novo_banco
    @contas.setter
    def contas(self,nova_conta):
      self._contas = nova_conta
    @financiamentos.setter
    def financiamentos(self,novo_finan):
      self._financiamentos = novo_finan
    def total_valor_contas(self):
      sm = 0
      for x in self._contas:
        sm += x.saldo
      return f'{sm}'
    def  financiamentos_cliente(self, cpfe):
        cnt = 1 
        for x in self._contas: 
          if x.cliente.cpf == cpfe:
            for y in x.cliente.financiamentos:
              print(f'{cnt}.\n Imovel: {y.imovel}  \n Banco:{y.banco.nome_do_banco}\n Financiamento: {y.valor_financiamento}\nAporte: {y.num_aportes}')
              cnt +=1
              print(y)
          else:
            print('mijo')
            continue
    def __str__(self):
        return f'{self._nome_do_banco}'
              
            



class conta:
    def __init__(self, cliente, ide, saldo):
      self._cliente = cliente
      self._ide = ide 
      self._saldo = saldo


    @property
    def ide(self):
        return self._ide
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def saldo(self):
        return self._saldo


    @ide.setter
    def ide(self, nova_ide):
        self._ide = nova_ide
    
    @cliente.setter
    def cliente(self, novo_cliente):
        self._cliente = novo_cliente
    @saldo.setter
    def saldo(self,new_saldo):
        self._saldo = new_saldo
        
    def creditar(self, valor):
        self._saldo += valor
    
    def debitar(self, valor):

        if self._saldo >= valor:
            self._saldo -= valor
        else:
            return "não ha saldo suficiente"
    
    def transferencia(self, valor, outra_conta):
        if self._saldo >= valor:
          self.debitar(valor)
          outra_conta.creditar(valor)
        else:
          print('Não foi possivel realizar a transferência!')
    
    def sacar_depositar(self,valor,opt):
      while True:
        if opt == '1':
          self.debitar(valor)
          break
        elif opt =='2':
          self.creditar(valor)
          break
        else:
          print('Opção Não existe! DIgite novamente.')

    #def __str__(self):
     # return "ide: {}, cliente: {}, saldo: {}, transferencia: {}".format(self._ide, self._cliente, self._saldo, self.transferencia)
    

class financiamento:
  def __init__(self,cliente,imovel,banco,valor_financiamento,num_aportes):
    self.__cliente = cliente
    self.__imovel = imovel
    self.__banco = banco
    self.__valor_financiamento = valor_financiamento
    self.__num_aportes = num_aportes
  
  @property
  def valor_financiamento(self):
    return self.__valor_financiamento
  @property
  def imovel(self):
    return self.__imovel
  @property
  def banco(self):
    return self.__banco
  @property
  def cliente(self):
    return self.__cliente
  @property
  def num_aportes(self):
    return self.__num_aportes 
  @valor_financiamento.setter
  def valor_financiamento(self,new_value):
    self.__valor_financiamento = new_value
  @imovel.setter
  def imovel(self,new_imovel):
    self.__imovel = new_imovel
  @banco.setter
  def banco(self,new_banco):
    self.__banco = new_banco
  @num_aportes.setter
  def num_aportes(self,new_aporte):
    self.__num_aportes = new_aporte
  @cliente.setter
  def cliente(self,new_client):
    self.__cliente = new_client
  def receber_aporte(self,value):
    self.__valor_financiamento -= _ 
    self.__num_aportes += 1

  


  def __str__(self):
    return f'Imovel: {self.__imovel}\nBanco:{self.__banco}\nValor: {self.__valor_financiamento}\nCPF:{self.__cliente.cpf}'


class cliente:
    def __init__(self, nome, cpf, salario, financiamentos = []):
      self._nome = nome 
      self._cpf = cpf
      self._salario = salario
      self._financiamentos = financiamentos

    #Gets
    @property
    def nome(self):
      return self._nome

    @property
    def cpf(self):
      return self._cpf

    @property
    def salario(self):
      return self._salario

    @property
    def financiamentos(self):
      return self._financiamentos
    

    #Setts
    @nome.setter
    def nome(self, novo_nome):
      self._nome = novo_nome

    @cpf.setter
    def cpf(self, novo_cpf):
      self._cpf = novo_cpf

    @salario.setter
    def salario(self, novo_salario):
      self._salario = novo_salario

    @financiamentos.setter
    def financiamentos(self, novo_financiamento):
      self._financiamentos = novo_financiamento


    #new_financiamento
    def new_financiamento(self,fin,conta):
          #value_finan = int(input('Digite o valor do financiamento -> '))
          #financiamento(id_account,imov,bank,value_finan,1)
         
            if 1 > (fin.valor_financiamento/fin.imovel.valor) > 0.7 and (conta.saldo)>= (fin.valor_financiamento):
              opt = input(f'Não foi Possíviel Realizar o financiamento! Receber aporte de {fin.imovel.valor - fin.valor_financiamento}R$ ?(Y/N)')
              if opt.lower() == 'y':
                fin.receber_aporte(fin.imovel.valor - conta.saldo)
                conta.debitar(fin.valor_financiamento)
                self.financiamentos.append(fin)
                fin.banco.financiamentos.append(fin)
                
            elif conta.saldo >= fin.valor_financiamento and (fin.valor_financiamento/fin.imovel.valor) >= 1 :
              if (fin.valor_financiamento/fin.imovel.valor) == 1:
                conta.debitar(fin.valor_financiamento)
                self.financiamentos.append(fin)
                fin.banco.financiamentos.append(fin)
              else:
                fin.valor_financiamento = fin.valor_financiamento - (fin.valor_financiamento - fin.imovel.valor)
              
                conta.debitar(fin.valor_financiamento)
              
                self.financiamentos.append(fin)
                fin.banco.financiamentos.append(fin)
              
            else:
              print('Não foi Possivel realizar o financiamento!')
              
          #bank.financiamentos.append(fin)
    
        

    def total_financiado(self):
      soma = 0
      for x in self._financiamentos:
        soma += x.valor_financiamento 

      return f' Total financiado -> {soma}'

    def __str__(self):
        return "nome: {}, cpf: {}, salario: {}".format(self._nome, self._cpf, self._salario)

