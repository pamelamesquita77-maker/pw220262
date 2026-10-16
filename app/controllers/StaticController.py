from flask import send_from_directory
from pathlib import Path


class StaticController:

    @staticmethod
    def css():
        caminho = Path(__file__).resolve().parents[1] / "views"

        return send_from_directory(
            str(caminho),
            "style.css"
        )
    