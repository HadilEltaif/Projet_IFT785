from flask import Blueprint, render_template

lidar_bp = Blueprint('lidar', __name__)

@lidar_bp.route('/')
def index():
    return render_template("pages/index.html")

@lidar_bp.route('/about')
def about():
    return render_template("pages/about.html")

@lidar_bp.route('/contact', methods=["GET", "POST"])
def contact():
    return render_template("pages/contact.html")

@lidar_bp.route('/upload')
def upload():
    return render_template("pages/upload.html")

@lidar_bp.route('/visualize')
def visualize():
    return render_template("pages/visualize.html")

@lidar_bp.route('/preprocess')
def preprocess():
    return "<h1>Prétraitement à venir</h1>"

@lidar_bp.route('/segment')
def segment():
    return "<h1>Segmentation à venir</h1>"

@lidar_bp.route('/detect')
def detect():
    return "<h1>Détection à venir</h1>"
