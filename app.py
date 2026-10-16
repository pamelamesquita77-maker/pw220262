from flask import Flask
from app.controllers.ProblemaController import ProblemaController
from app.controllers.AutorController import AutorController
from app.controllers.StaticController import StaticController

app = Flask(
    __name__,
    template_folder="app/views"
)


# FrontController: centralização das rotas

@app.route("/")
@app.route("/index")
def index():
    return ProblemaController.index()


@app.route("/problema", methods=["GET", "POST"])
def problema():
    if __import__("flask").request.method == "POST":
        return ProblemaController.resolver()

    return ProblemaController.index()


@app.route("/autor")
def autor():
    return AutorController.index()


@app.route("/style.css")
def css():
    return StaticController.css()


if __name__ == "__main__":
    app.run(debug=True)
    