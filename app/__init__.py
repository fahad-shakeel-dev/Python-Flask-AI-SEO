from flask import Flask
from dotenv import load_dotenv
from app.competitor import competitor_bp
load_dotenv()
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_prefixed_env()

  # Import and register blueprints
from .routes.main_routes import main_bp
from .routes.auth_routes import auth_bp
app.register_blueprint(main_bp)
app.register_blueprint(competitor_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

