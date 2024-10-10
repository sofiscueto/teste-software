import random
lista = [random.randint(1, 100) for _ in range(5)]

numeros = [8, 15, 32]

def main():

    def adicionar_numero(lista):
        try:
            numero = int(imput("Digite um número inteiro para ser adicionado á lista: "))
            lista.append(numero)
            print(f"Número {numero} adicionado à lista.")
        except ValueError:
            print("Número inválido! Por favor, insira um número inteiro.")

    def remover_numero(lista):
        try:
            numero = int(imput("Digite um número inteiro para ser retirado da lista: "))
            lista.remove(numero)
            print(f"Número {numero} removido da lista.")
        except ValueError:
            print("Número inválido! Por favor, insira um número existente na lista.")
    
    def exibir_lista(lista):
        print("Lista atual: ", lista)

    def calculo_soma(lista):
        soma = sum(lista)
        print("A soma de todos os números na lista é:", soma)

    def calcular_media(lista):
        if lista:
            media = sum(lista)
