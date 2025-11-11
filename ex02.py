# 1. Definição da Superclasse (classe pai)
class FormaGeometrica:
    """
    Classe base genérica para formas geométricas.
    """
    def calcular_area(self):
        """
        Método base. Como uma forma genérica não tem fórmula de área,
        levantamos um erro indicando que as subclasses DEVEM implementar isso.
        """
        raise NotImplementedError("A subclasse deve implementar o método calcular_area()")

# 2. Definição da Subclasse (classe filha)
class Circulo(FormaGeometrica):
    """
    Subclasse que representa um Círculo e herda de FormaGeometrica.
    """
    def __init__(self, raio):
        """
        Construtor específico do Círculo.
        Recebe o raio e o armazena como atributo da instância.
        """
        self.raio = raio

    def calcular_area(self):
        """
        Sobrescrita do método calcular_area().
        Aqui definimos a lógica específica para calcular a área de um círculo.
        Fórmula: pi * raio²
        """
        pi = 3.14159
        area = pi * (self.raio ** 2)
        return area

# --- Demonstração do uso das classes ---

# 3. Criando um objeto (instância) da subclasse Circulo
# Vamos criar um círculo com raio 5
meu_circulo = Circulo(5)

print(f"Círculo criado com raio: {meu_circulo.raio}")

# 4. Chamando o método sobrescrito
# O Python vai usar a versão do método definida em Circulo, e não em FormaGeometrica.
area_calculada = meu_circulo.calcular_area()

print(f"A área do círculo é: {area_calculada}")