# autor: Michel
# data: 11/11/2025

# 1. Crie uma Hierarquia de Animais
# Defina uma superclasse `Animal` com um construtor que 
# aceita `nome` e `idade`, e um método `fazer_som()` que 
# imprime "Som genérico de animal".

# Crie uma subclasse `Cachorro` que herde de `Animal`. 
# Adicione um método `latir()` específico do cachorro. 
# Crie um objeto `Cachorro` e chame `fazer_som()` (herdado) e `latir()`.


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

# --- Demonstração do uso das classes ---

# 3. Criando um objeto (instância) da subclasse Cachorro
# Ao criar o objeto, o construtor __init__ da superclasse Animal é chamado.
meu_cachorro = Cachorro("Rex", 5)

print("\n--- Chamando os métodos do objeto 'meu_cachorro' ---")

# 4. Chamando o método herdado da superclasse
# O método fazer_som() não foi definido em Cachorro, mas foi herdado de Animal.
meu_cachorro.fazer_som()

# 5. Chamando o método específico da subclasse
# O método latir() pertence apenas à classe Cachorro.
meu_cachorro.latir()