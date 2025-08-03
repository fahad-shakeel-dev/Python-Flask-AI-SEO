# from flask import Flask
# from dotenv import load_dotenv
# from app.competitor import competitor_bp
# load_dotenv()
# app = Flask(__name__, static_folder="static", template_folder="templates")
# app.config.from_prefixed_env()
#
#   # Import and register blueprints
# from .routes.main_routes import main_bp
# from .routes.auth_routes import auth_bp
# app.register_blueprint(main_bp)
# app.register_blueprint(competitor_bp)
# app.register_blueprint(auth_bp, url_prefix='/auth')
#
# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
#











# from flask import Flask
# from dotenv import load_dotenv
# from app.competitor import competitor_bp
#
# load_dotenv()
# app = Flask(__name__, static_folder="static", template_folder="templates")
# app.config.from_prefixed_env()
#
# # Import and register blueprints
# from .routes.main_routes import main_bp
# from .routes.auth_routes import auth_bp
# app.register_blueprint(main_bp)
# app.register_blueprint(competitor_bp)
# app.register_blueprint(auth_bp, url_prefix='/auth')
#
# if __name__ == "__main__":
#     app.run(debug=True, port=5000)  # Running on port 5000 as specified









from flask import Flask
from dotenv import load_dotenv
from app.competitor import competitor_bp
from app.analyzer import kw_model, sum_pipe, emo_pipe  # Preload model loaders

load_dotenv()
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_prefixed_env()

# Preload models at startup to reduce first-request latency
with app.app_context():
    kw_model()  # Load KeyBERT model
    sum_pipe()  # Load summarization pipeline
    emo_pipe()  # Load emotion pipeline

# Import and register blueprints
from .routes.main_routes import main_bp
from .routes.auth_routes import auth_bp
app.register_blueprint(main_bp)
app.register_blueprint(competitor_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True, port=5000)