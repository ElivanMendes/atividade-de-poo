from random import randint


class Pix:
    def __init__(self, chave_pix):
        self.__chave_pix = chave_pix

    def get_chave_pix(self):
        return self.__chave_pix


class Conta:
    def __init__(self):
        self.__agencia = randint(1, 10)
        self.__numero = randint(1000, 9999)

    __chaves_pix = []

    def get_agencia(self):
        return self.__agencia

    def get_numero(self):
        return self.__numero

    def cadastrar_chave_pix(self, chave_pix):
        self.__chaves_pix.append(chave_pix)

    def print(self):
        print(f'\n\tAgençia: {self.__agencia}\n\tNumero da Conta: {self.__numero}')

    def print_chaves_pix(self):
        print('\n\tCHAVES PIX:')
        for chave in self.__chaves_pix:
            print(f'\t{chave}')


class Contatos:
    def __init__(self, contato):
        self.__contato = contato

    def get_contato(self):
        return self.__contato


class Cliente:
    def __init__(self, nome, cpf, idade, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__endereco = endereco

    __conta = None
    __contatos = []

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_idade(self):
        return self.__idade

    def get_endereco(self):
        return self.__endereco

    def get_conta(self):
        return self.__conta

    def cadastrar_conta(self):
        self.__conta = Conta()

    def adicionar_contato(self, contato):
        self.__contatos.append(contato)

    def print(self):
        print(f'\n\tNome: {self.__nome}\n\tCPF: {self.__cpf}\n\tIdade: {self.__idade}\n\tEndereço: {self.__endereco}')

    def print_contatos(self):
        print('\n\tCONTATOS:')
        for contato in self.__contatos:
            print(f'\t{contato}')


c1 = Cliente('Elivan', '610550', 20, 'Travessa 1')

c1.print()

c1.cadastrar_conta()

c1.get_conta().print()

c1.get_conta().cadastrar_chave_pix('Elivan@gmail.com')
c1.get_conta().cadastrar_chave_pix('(99) 98877-5544')

c1.get_conta().print_chaves_pix()

c1.adicionar_contato('(99) 9887766-1122')
c1.adicionar_contato('(99) 9811133-6689')

c1.print_contatos()
