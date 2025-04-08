from flask import Blueprint, render_template, request, jsonify, send_file, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
import tempfile
import json

from app.services.pointcloud_service import PointCloudService
from app.services.preprocessing_service import PreprocessingService
from app.services.file_service import FileService

lidar_bp = Blueprint('lidar', __name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "uploads")
PROCESSED_FOLDER = os.path.join(UPLOAD_FOLDER, "processed")


@lidar_bp.route('/')
def index():
    return render_template("pages/index.html")


@lidar_bp.route('/about')
def about():
    return render_template("pages/about.html")


@lidar_bp.route('/contact', methods=["GET", "POST"])
def contact():
    return render_template("pages/contact.html")


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


@lidar_bp.route('/visualize/')
def visualize():
    upload_folder = os.path.join("uploads")
    filename = request.args.get('filename')

    try:
        files = sorted([f for f in os.listdir(upload_folder) if f.endswith(('.pcd', '.ply', '.bin'))])
    except Exception as e:
        print(f"Erreur lecture fichiers: {e}")
        files = []

    return render_template("pages/visualize.html", files=files, filename=filename)


@lidar_bp.route('/api/points/<filename>')
def get_points(filename):
    filepath = os.path.join("uploads", filename)
    if not os.path.exists(filepath):
        filepath = os.path.join("uploads", "processed", filename)
    try:
        data_json = PointCloudService.get_point_cloud_json(filepath)
        return jsonify(json.loads(data_json))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@lidar_bp.route('/uploads/<path:filename>')
def uploaded_file(filename):
    if os.path.exists(os.path.join(UPLOAD_FOLDER, "processed", filename)):
        return send_from_directory(os.path.join(UPLOAD_FOLDER, "processed"), filename)
    return send_from_directory(UPLOAD_FOLDER, filename)


@lidar_bp.route("/preprocess/")
def preprocess_page():
    files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith(('.pcd', '.ply', '.bin'))]
    return render_template("pages/preprocess.html", files=files)


@lidar_bp.route("/preprocess_step_and_return_json/<step>/<filename>")
def preprocess_and_return_json(step, filename):
    file_path = os.path.join("uploads", filename)
    if not os.path.exists(file_path):
        return jsonify({"error": "Fichier non trouvé."}), 404

    try:
        _, new_path = PreprocessingService.apply_step_and_save(file_path, step)
        processed_name = os.path.basename(new_path)
        return jsonify({
            "filename": processed_name
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@lidar_bp.route("/download/<filename>")
def download_file(filename):
    path = os.path.join(PROCESSED_FOLDER, filename)
    if not os.path.exists(path):
        return "Fichier introuvable", 404
    return send_file(path, as_attachment=True)
