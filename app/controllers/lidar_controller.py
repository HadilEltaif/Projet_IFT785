from flask import Blueprint, render_template, request, jsonify, send_file, flash, redirect, url_for, send_from_directory
import os
import json

from app.services.pointcloud_service import PointCloudService
from app.services.clustering_service import ClusteringService
from app.utils.geometry_utils import compute_bounding_box

from app.commands.commands import UploadCommand, PreprocessCommand, VisualizeCommand
from app.services.pointcloud_service import PointCloudService

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

        from app.services.file_service import FileService
        if not FileService.allowed_file(file.filename):
            flash("Format de fichier non supporté. Utilisez .pcd, .ply ou .bin", "error")
            return redirect(request.url)

        try:
            cmd = UploadCommand(file)
            cmd.execute()
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
        if not os.path.exists(filepath):
            return jsonify({"error": "Fichier non trouvé."}), 404

    try:
        cmd = VisualizeCommand(filepath)
        return jsonify(cmd.execute())
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
        original_points = PointCloudService.get_numpy_array(file_path)
        num_points_before = original_points.shape[0]

        cmd = PreprocessCommand(file_path, step)
        _, new_path = cmd.execute()
        processed_name = os.path.basename(new_path)

        processed_points = PointCloudService.get_numpy_array(new_path)
        num_points_after = processed_points.shape[0]

        return jsonify({
            "filename": processed_name,
            "points": processed_points.tolist(),
            "points_before": num_points_before,
            "points_after": num_points_after
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@lidar_bp.route("/download/<filename>")
def download_file(filename):
    path = os.path.join(PROCESSED_FOLDER, filename)
    if not os.path.exists(path):
        return "Fichier introuvable", 404
    return send_file(path, as_attachment=True)





@lidar_bp.route("/cluster_page")
def cluster_page():
    try:
        all_files = []

        for folder in [UPLOAD_FOLDER, PROCESSED_FOLDER]:
            if os.path.exists(folder):
                files = [
                    f for f in os.listdir(folder)
                    if f.endswith(('.pcd', '.ply', '.bin'))
                ]
                all_files.extend(files)

        # Supprimer les doublons (ex. même nom dans les deux dossiers)
        unique_files = sorted(list(set(all_files)))

    except Exception as e:
        print(f"[Erreur lecture fichiers cluster_page] {e}")
        unique_files = []

    return render_template("pages/cluster.html", files=unique_files)

@lidar_bp.route("/cluster/<filename>")
def cluster(filename):
    print(f"📦 Clustering reçu : {filename}")
    possible_paths = [
        os.path.join("uploads", "processed", filename),
        os.path.join("uploads", filename)
    ]

    for path in possible_paths:
        if os.path.exists(path):
            try:
                points = PointCloudService.get_numpy_array(path)
                clusters = ClusteringService.cluster_points(points)
                result = []
                for cluster in clusters:
                    box = compute_bounding_box(cluster)
                    result.append({
                        "points": cluster.tolist(),
                        "bbox": box
                    })
                return jsonify({"clusters": result, "count": len(result)})
            except Exception as e:
                return jsonify({"error": str(e)}), 500

    print("❌ Fichier non trouvé.")
    return jsonify({"error": "Fichier non trouvé"}), 404
