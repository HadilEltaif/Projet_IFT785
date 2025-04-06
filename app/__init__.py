from flask import Flask

def create_app():
    app = Flask(__name__)

    # Enregistrement des blueprints
    from app.controllers.lidar_controller import lidar_bp
    app.register_blueprint(lidar_bp)

    return app
