from flask import Flask

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_prefixed_env()

  # Import and register blueprints
from .routes.main_routes import main_bp
from .routes.auth_routes import auth_bp
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

#
# from flask import Flask
#
# app = Flask(__name__, static_folder="static", template_folder="templates")
# app.config.from_prefixed_env()
#
# # Import and register blueprints
# from .routes.main_routes import main_bp
# from .routes.auth_routes import auth_bp
# from .routes.dashboard import dashboard
# app.register_blueprint(main_bp)
# app.register_blueprint(auth_bp, url_prefix='/auth')
# app.register_blueprint(dashboard, url_prefix='/dashboard')
#
# if __name__ == "__main__":
#     app.run(debug=True, port=5000)