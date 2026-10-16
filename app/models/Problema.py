class Problema:
    def __init__(self, enunciado, resposta=""):
        self.enunciado = enunciado
        self.resposta = resposta

    def calcular(self, valor):
        try:
            numero = float(valor)
            resultado = numero ** 2
            return f"O quadrado de {numero:g} é {resultado:g}."
        except (ValueError, TypeError):
            return "Digite um número válido."
        