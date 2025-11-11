
from ex01_01 import Animal

# 2. Definição da Subclasse (classe filha) que herda de Animal
class Cachorro(Animal):
    """
    Uma subclasse que representa um cachorro e herda de Animal.
    """
    # Como não definimos um __init__ aqui, ele usa automaticamente o da classe pai (Animal).

    def latir(self):
        """
        Um método específico para a classe Cachorro.
        """
        print(f"{self.nome} faz: Au au!")