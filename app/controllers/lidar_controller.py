from flask import Blueprint, render_template, request, redirect, flash, url_for, send_from_directory, jsonify
from app.services.file_service import FileService
import os
import json

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

@lidar_bp.route('/visualize/')
def visualize():
    latest_file = None
    upload_folder = 'uploads'

    try:
        files = sorted(
            [f for f in os.listdir(upload_folder) if f.endswith(('.pcd', '.ply'))],
            key=lambda x: os.path.getmtime(os.path.join(upload_folder, x)),
            reverse=True
        )
        if files:
            latest_file = files[0]
    except Exception as e:
        print(f"Erreur lecture fichiers: {e}")

    return render_template("pages/visualize.html", filename=latest_file)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "uploads")

@lidar_bp.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@lidar_bp.route('/api/points/<filename>')
def get_points(filename):
    filepath = f"uploads/{filename}"
    try:
        from app.services.pointcloud_service import PointCloudService
        data_json = PointCloudService.get_point_cloud_json(filepath)
        return jsonify(json.loads(data_json))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@lidar_bp.route('/preprocess')
def preprocess():
    return "<h1>Prétraitement à venir</h1>"

@lidar_bp.route('/segment')
def segment():
    return "<h1>Segmentation à venir</h1>"

@lidar_bp.route('/detect')
def detect():
    return "<h1>Détection à venir</h1>"
