# 1. Definição da Superclasse (classe pai)
class Animal:
    """
    Uma classe base que representa um animal.
    """
    def __init__(self, nome, idade):
        """
        Construtor da classe Animal.
        Inicializa os atributos nome e idade.
        """
        self.nome = nome
        self.idade = idade
        print(f"{self.nome}, um animal de {self.idade} anos, foi criado.")

    def fazer_som(self):
        """
        Método que representa o som genérico de um animal.
        """
        print(f"{self.nome} faz: Som genérico de animal.")
