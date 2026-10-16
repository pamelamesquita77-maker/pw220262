from flask import render_template, request
from app.models.Problema import Problema


class ProblemaController:

    @staticmethod
    def index():
        return render_template(
            "index.html",
            enunciado="Digite um número para calcular seu quadrado."
        )

    @staticmethod
    def resolver():
        valor = request.form.get("valor", "")

        problema = Problema(
            enunciado="Calcule o quadrado do número informado."
        )

        resposta = problema.calcular(valor)

        return render_template(
            "problema.html",
            enunciado=problema.enunciado,
            resposta=resposta
        )
    