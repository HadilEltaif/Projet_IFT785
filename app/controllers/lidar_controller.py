from flask import Blueprint, render_template, request, redirect, flash, url_for
from app.services.file_service import FileService

lidar_bp = Blueprint('lidar', __name__)

@lidar_bp.route('/upload/', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("file")

        if not file:
            flash("Aucun fichier sélectionné.", "error")
            return redirect(request.url)

        if not FileService.allowed_file(file.filename):
            flash("Format de fichier non supporté. Utilisez .pcd, .ply ou .bin", "error")
            return redirect(request.url)

        try:
            FileService.process_uploaded_file(file)
            flash("Fichier téléversé avec succès !", "success")
        except Exception as e:
            flash(f"Erreur lors du traitement du fichier : {str(e)}", "error")

        return redirect(url_for("lidar.upload"))

    return render_template("pages/upload.html")
@lidar_bp.route('/')
def index():
    return render_template("pages/index.html")

@lidar_bp.route('/about')
def about():
    return render_template("pages/about.html")

@lidar_bp.route('/contact', methods=["GET", "POST"])
def contact():
    return render_template("pages/contact.html")

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
