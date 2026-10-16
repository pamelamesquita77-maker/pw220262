from flask import render_template


class AutorController:

    @staticmethod
    def index():
        autor = {
            "nome": "Seu nome completo",
            "formacoes": [
                "Licenciatura em Matemática"
            ],
            "experiencias": [
                "Adicione aqui suas experiências."
            ]
        }

        return render_template(
            "autor.html",
            autor=autor
        )
    