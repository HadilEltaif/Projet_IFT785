from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'ma_clé_secrète_lidar_2025'
    from app.controllers.lidar_controller import lidar_bp
    app.register_blueprint(lidar_bp)

    return app

