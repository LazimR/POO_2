import datetime
from random import randint
class Conta:
    __slots__ = ['_numero','_titular','saldo','_limite','_historico','_senha','_login']
    
    _total_contas = 0
    
    
    def __init__(self,numero,titular,senha,login,saldo = 0 ,limite = 1000):
        self._numero = numero
        self._titular = titular
        self.saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self._senha = senha
        self._login = login
        Conta._total_contas += 1

    @staticmethod
    def get_total_contas():
        return Conta._total_contas
    
    @property
    def get_numero(self):
        return self._numero

    @get_numero.setter
    def set_numero(self,n):
        self._numero = n

    @property
    def get_titular(self):
        return self._titular

    @get_titular.setter
    def set_titular(self,t):
        self._titular = t

    @property
    def get_limite(self):
        return self._limite
    
    @get_limite.setter
    def set_limite(self,l):
        self._limite = l

    @property
    def get_historico(self):
        return self._historico

    @get_historico.setter
    def set_historico(self,h):
        self._historico = h

    @property
    def get_senha(self):
        return self._senha
    
    @get_senha.setter
    def set_senha(self,s):
        self._senha = s

    @property
    def get_login(self):
        return self._login
    
    @get_login.setter
    def set_login(self,l):
        self._login = l

    def deposita(self,quantidade):
        if quantidade > 0:
            self.saldo += quantidade
            self._historico.transacao.append(f'Deposito:{quantidade} - Data:{datetime.datetime.now()}') 
            return True
        else:
            return False

    def saque(self,quantidade,senha,t = 0):
        if senha == self._senha and quantidade > 0 and quantidade <= self.saldo:
            self.saldo -= quantidade
            if t == 0:
                self._historico.transacao.append(f'Saque:{quantidade} - Data:{datetime.datetime.now()}')
            else:
                self._historico.transacao.append(f'Transferência:{quantidade} - Data:{datetime.datetime.now()}')
            return True
        
        else:
            return False

    def extrato(self):
        print(f'Conta:{self._numero}  Saldo:{self.saldo}')
        self._historico.transacao.append(f'Pedido de extrato as {datetime.datetime.now()}')
        

    def transfere(self,destino,quantidade,senha):
        if self.saque(quantidade,senha,1):
            return destino.deposita(quantidade)
        else:
            return False
        
class Cliente:
    def __init__(self,nome,sobre,cpf):
        self._nome = nome
        self._sobre = sobre
        self._cpf = cpf

    @property
    def get_nome(self):
        return self._nome
    
    @get_nome.setter
    def set_nome(self,n):
        self._nome = n

    @property
    def get_sobre(self):
        return self._sobre
    
    @get_sobre.setter
    def set_sobre(self,s):
        self._sobre = s

    @property
    def get_cpf(self):
        return self._cpf
    
    @get_cpf.setter
    def set_cpf(self,cpf):
        self._cpf = cpf

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.now()
        self.transacao = []

    def imprime(self):
        print(f'Data abertura: {self.data_abertura}')
        print('Transações:')
        for i in self.transacao:
            print(i)

def gera_numero():
    n = randint(100,999)
    for i in b.contas:
        if b.contas[i].get_numero == n:
            return gera_numero()
    return n

class Banco:

    def __init__(self):
        self.contas = {}
        self.clientes = {}

    def adiciona_conta(self,c,l):
        self.contas[l] = c

    def adiciona_cliente(self,c,cpf):
        self.clientes[cpf] = c
        

def sys_banco(conta):
    while True:
        opc = int(input('1 - Saque\n2 - Deposito\n3 - Transferência\n4 - Extrato\n5 - Sair\n'))
        if opc == 1:
            try:
                senha = input('Senha:')
                quantia = float(input('Quantia:'))
                if conta.saque(quantia,senha):
                    print('Saque feito com sucesso!\n')
                else:
                    print('Erro na operação!\n')
            except ValueError:
                print('Dado incorreto!\n')
        elif opc == 2:
            try:
                quantia = float(input('Quantia:'))
                if conta.deposita(quantia):
                    print('Deposito feito com sucesso!\n')
                else:
                    print('Erro na operação!\n')
            except ValueError:
                print('Valor invalido!\n')

        elif opc == 3:
            try:
                senha = input('Senha:')
                if senha == conta.get_senha:
                    n = int(input('Informe o número da conta destinatária: '))
                    for i in b.contas:
                        if b.contas[i].get_numero == n:
                            quantia = float(input('Quantia:'))
                            if conta.transfere(b.contas[i],quantia,senha):
                                print('Transferência feita com sucesso!\n')
                            else:
                                print('Saldo insuficiente\n')        
            except ValueError:
                print('Dado invalido!\n')
                
                
        elif opc == 4:
            conta.extrato()
    
        elif opc == 5:
            break
        
        else:
            print('Opção invalida')



b = Banco()

if __name__ == '__main__':
    while True:
        opc = input('1 - Login\n2 - Cadastrar\n3 - Sair\n')
        if opc == '1':
        
            login = input('Login:')
            senha = input('Senha:')
            for i in b.contas:
                if i == login:
                    if b.contas[login].get_senha == senha:
                        sys_banco(b.contas[login])        

        elif opc == '2':
            while True:
                nome = input('Não use caracteres especiais\nPrimeiro Nome:')
                if nome.isalpha():
                    nome = nome.upper()
                    break
                else:
                    print('Não é permitido caracteres especiais ou números!\n')

            while True:
                sobre = input('Não use caracteres especiais\nSobrenome:')
                if sobre.isalpha():
                    sobre = sobre.upper()
                    break
                else:
                    print('Não é permitido caracteres especiais ou números!\n')
                    
            while True:
                cpf = str(input('\nApenas números\nInforme o CPF:'))
                
                if cpf.isdecimal() and len(cpf) == 11:
                    break
                else:
                    print('CPF invalido!\n')
            login = input('Informe o login:')
            senha =  input('Informe a senha:')
            numero = gera_numero()

            if login in b.contas:
                print('Login já cadastrado!')   
            else:
                cliente = Cliente(nome,sobre,cpf)
                c = Conta(int(numero),cliente,senha,login)
                b.adiciona_cliente(cliente, cpf)             
                b.adiciona_conta(c, login) 
                print(f'O número da sua conta é {numero}')
        
        elif opc == '3':
            break
        else:
            print('Opção invalida')


    
