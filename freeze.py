from flask_frozen import Freezer
from app import app  # Asegúrate de que 'app' es el nombre de tu aplicación Flask

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()

