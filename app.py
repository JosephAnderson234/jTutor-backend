from flask import Flask
from config import Config
from extensions import jwt, cors

from routes.auth import auth_bp
from routes.upload import upload_bp
from routes.chat import chat_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt.init_app(app)
    cors.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(upload_bp, url_prefix="/upload")
    app.register_blueprint(chat_bp, url_prefix="/chat")

    @app.route("/")
    def health():
        return {"status": "ok"}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
