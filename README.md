# 🚀 LiDAR Clustering Web

**LiDAR Clustering Web** est une application web interactive qui permet de téléverser, visualiser, prétraiter, segmenter et analyser des fichiers de données 3D (PCD, PLY, BIN). Ce projet applique les principes SOLID et les design patterns (Factory, Strategy, etc.) pour une architecture propre, maintenable et extensible.

---

## 📁 Structure du projet

```
app/
│
├── controllers/         # Contrôleurs Flask
├── services/            # Logique métier (traitement, clustering, etc.)
├── factories/           # Pattern Factory (chargement fichiers)
├── strategies/          # Pattern Strategy (prétraitement, clustering)
├── loaders/             # Loaders spécifiques (pcd, ply, bin)
├── interfaces/          # Interfaces abstraites (SOLID)
├── models/              # Structures de données (PointCloud, etc.)
├── templates/           # Templates HTML (Flask + Jinja2)
├── static/              # CSS, images, logos
├── utils/               # Utilitaires (log, config, helpers)
└── config.py            # Configuration globale
```

---

## 🌐 Fonctionnalités

- ✅ Téléversement de fichiers `.pcd`, `.ply`, `.bin`
- ✅ Visualisation interactive de nuages de points
- ✅ Prétraitement (filtres, transformation)
- ✅ Segmentation et clustering
- ✅ Interface web en Flask
- ✅ Intégration de design patterns
- ✅ Respect des principes SOLID

---

## 🔌 Installation

1. **Cloner le projet**  
```bash
git clone https://github.com/<your-username>/lidar_clustering_web.git
cd lidar_clustering_web
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate.bat       # Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

---

## ▶️ Lancer l'application

```bash
python run.py
```

> Accédez à l'application sur : http://127.0.0.1:5000/

---

## 🧱 Design Patterns utilisés

- **Factory** → pour le chargement flexible de fichiers (PCD, PLY, BIN)
- **Strategy** → pour l'application dynamique de différents algorithmes de clustering
- **Interface / Abstraction** → via `ILoader`, `IPreprocessing`, `IClustering`
- **Single Responsibility** → chaque classe a une responsabilité claire
- **Open/Closed Principle** → facile d’ajouter de nouveaux formats sans modifier l’existant

---

## 🧪 Tests

Les tests unitaires seront ajoutés dans le dossier `tests/` pour valider le comportement de chaque composant (services, loaders, stratégies).

---

## 👩‍💻 Développé par

Hadil Eltaif  
Université de Sherbrooke  
Laboratoire DOMUS 💚