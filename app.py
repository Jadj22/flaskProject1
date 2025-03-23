from flask_swagger_ui import get_swaggerui_blueprint
from app import create_app
import platform

app = create_app()

if __name__ == "__main__":
    if platform.system() == "Windows":
        from waitress import serve
        print("Démarrage avec Waitress pour Windows...")
        serve(app, host="0.0.0.0", port=5000)
    else:
        print("Démarrage avec Flask pour développement...")
        app.run(debug=True, host="0.0.0.0", port=5000)