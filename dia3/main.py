#FÁCIL:
#1
def questaoUm():
    #print("Olá, mundo!"
    #Correção:
    print("Olá, mundo!")
    #O código não funcionou devido a falta de parênteses fechando a função
#2
def questaoDois():
    #print(nome)
    #Correção
    nome = input("Insira seu nome: ")
    print(nome)
    #É necessário atribuir um valor a variável antes de realizar alguma operação com ela

#MÉDIO:
#3
def questaoTres():
    '''
    def somar(a,b):
        return a+b
    resultado = somar(10,"5")
    print(resultado)
    Resultado: unsupported operand type(s) for +: 'int' and 'str'
    '''
    #O código quebrou ao tentar somar um valor inteiro com uma string
    try:
        def somar(a,b):
            return a+b
        resultado = somar(10,"5")
        print(resultado)
    except TypeError:
        print("Operações entre um valor inteiro e uma string não são suportadas")

#4
def questaoQuatro():
    '''
    numeros = [10,20,30]
    indice = int(input("Digite um índice para acessar a lista: "))

    print(numero[indice])
    '''
    while True:
        try:
            numeros = [10,20,30]
            indice = int(input("\nDigite um índice para acessar a lista: "))
            print(numeros[indice])
            break
        except ValueError:
            print("\nApenas um número inteiro é permitido")

        except IndexError:
            print(f"\nInsira um índice entre 0 e {len(numeros)-1}")
    '''
    Para não permitir que o código quebre mesmo com um valor quebrado
    Foi usado um loop que checa qual o erro e avisa ao usuário
    '''
#5
def questaoCinco():
    def dividir(a,b):
        return a/b
    while True:
        try:
            num1 = input("Digite o primeiro número: ")
            num2 = input("Digite o segundo número: ")
            resultado = dividir(int(num1), int(num2))
            print(f"Resultado: {resultado}")
        except ValueError:
            print("\nDigite apenas valores inteiros!\n")
        except ZeroDivisionError:
            print("\nDigite um valor diferente de 0\n")
    #Para corrigir esse código foi necessário adicionar um loop 
    #que checa se o valor inserido é válido, 
    #se não ele dá printa o erro para o usuário e repete o loop


#Difícil
#6
def questaoSeis():
    '''
    dados = {
        "nome": "Isaac ",
        "idade": 25,
        "cidade": "São Paulo"
    }

    chave = input("Digite a chave que deseja acessar: ")

    print(f"O valor da chave '{chave}' é: {dados[chave]}")
    '''
    while True:    
        try:    
            dados = {
                "nome":"Isaac ",
                "idade": 25,
                "cidade": "São Paulo"
            }
            chave = input("Digite a chave que deseja acessar: ")
            print(f"O valor da chave '{chave}' é: {dados[chave]}")
            break
        except KeyError:
            print(dados.get(chave,"A chave inserida não é válida, tente inserir: nome/idade/cidade"))
    #Para evitar a quebra do código foi utilizado 
    #a função get no dicionário para ter uma resposta padrão de erro
#7
def questaoSete():
    '''
    def validar_idade(idade)
        if idade < 0 or idade > 120:
            raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
        return f"Idade válida: {idade}"

    idade = int(input("Digite sua idade: "))
    print(validar_idade(idade))
    '''
    def validar_idade(idade):
        if idade< 0 or idade > 120:
            raise ValueError("A idade deve estar entre 0 e 120 anos!")
        return f"idade válida: {idade}"
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            print(validar_idade(idade))
            break
        except ValueError:
            print("A idade inserida não é um valor válido\nTente uma idade entre 0 e 120 anos")
    #Para corrigir o código foi necessário um loop
    #e adicionar uma nova mensagem de erro
    #para conseguir informar o usuário sem que o código quebre

#EXTRA
def questaoExtra():
    '''
    def calcular_media(notas):
        soma = sum(notas)
        quantidade = len(notas)
        return soma/quantidade

    notas = [8,9,"10",7]
    media =  calcular_media(notas)
    print(f"Média: {media:.2f}")
'''
    def calcular_media(notas):
        soma = sum(notas)
        quantidade = len(notas)
        return soma/quantidade
    try:
        notas = []
        i = 0
        while i != 'q':
            i = input("Insira uma nota ou insira q para sair: ")
            if i != 'q':
                notas.append(i.lower())
        notasInt = map(int,notas)
        notas = list(notasInt)
        media = calcular_media(notas)
        print(f"Média: {media:.2}")
    except ZeroDivisionError:
        print("Não havia números para dividir")
    except ValueError:
        print("Houve um valor inv")
#TypeError
#ZeroDivisionError
questaoExtra()