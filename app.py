from flask import Flask
from presentation.controllers.livro_controller import livro_bp

# Configura o Flask para procurar as Views dentro da pasta Presentation
app = Flask(__name__, template_folder='presentation/views')

app.register_blueprint(livro_bp)

if __name__ == '__main__':
    app.run(debug=True)