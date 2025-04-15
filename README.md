# LiDAR Clustering Web

**LiDAR Clustering Web** est une application web interactive développée en Flask, permettant de téléverser, visualiser, prétraiter, segmenter et analyser des fichiers de données LiDAR 3D (`.pcd`, `.ply`, `.bin`). Le projet est structuré autour des principes **SOLID** et implémente plusieurs **design patterns** pour assurer modularité, extensibilité et maintenabilité.

---

## 🌐 Fonctionnalités principales

- 📤 Téléversement de fichiers 3D (.pcd, .ply, .bin)
- 👁️ Visualisation interactive des nuages de points avec Three.js
- 🧹 Prétraitement des données (sol, outliers, découpe latérale/verticale)
- 🔗 Pipeline de prétraitement dynamique (Chain of Responsibility)
- 📦 Clustering DBSCAN mais on peut utiliser d'autres algos.
- 📊 Calcul des bounding boxes pour chaque cluster
- 🧠 Architecture modulaire (Factory, Strategy, Command, etc.)
- 🌍 Interface web ergonomique avec Flask + Bootstrap

---

## 🧱 Structure du projet

```
app/
├── commands/                 # Command Pattern (Upload, Preprocess, Visualize)
├── controllers/             # Contrôleurs Flask
├── preprocessing_pipeline/  # Chaîne de prétraitement (Chain of Responsibility)
├── strategies/              # Stratégies de prétraitement et clustering
├── factories/               # Factory Pattern pour loaders de fichiers
├── loaders/                 # Loaders PCD, BIN, PLY
├── interfaces/              # Interfaces abstraites
├── models/                  # Structures de données (PointCloud, etc.)
├── services/                # Services métiers
├── utils/                   # Utils & configuration
├── templates/, static/      # HTML (Jinja2) & CSS/JS
└── config.py                # Configuration globale
```

---

## ⚙️ Installation

1. **Cloner le dépôt :**
```bash
git clone https://github.com/HadilEltaif/Projet_IFT785.git
cd Projet_IFT785
```

2. **Créer un environnement virtuel :**
```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. **Installer les dépendances :**
```bash
pip install -r requirements.txt
```

---

## ▶️ Lancer l'application

```bash
python run.py
```

➡️ Ouvrir [http://127.0.0.1:5000/](http://127.0.0.1:5000/) dans votre navigateur.

---
## 🧪 Exécuter les tests
 
1. **Exécuter tous les tests**
   ```sh
   python -m pytest --cov=app
   ```
   ```sh
   python -m pytest --cov=app --cov-report=term-missing
   ```
2. **Générer un rapport de couverture en HTML**
   ```sh
   python -m pytest --cov=app --cov-report=html
   ```
   Ouvrir le fichier `htmlcov/index.html` dans un navigateur.

## 💡 Design Patterns utilisés

| Pattern                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| ✅ Factory Pattern      | `LoaderFactory` choisit dynamiquement un loader selon le type de fichier    |
| ✅ Strategy Pattern     | Applique des traitements comme `RemoveFloorStrategy`, `DownsampleStrategy`  |
| ✅ Command Pattern      | Actions (Upload, Visualize, Preprocess) encapsulées dans `Command` classes |
| ✅ Singleton Pattern    | `GlobalConfig` stocke la config globale de manière centralisée              |
| ✅ Decorator Pattern    | `StrategyLoggerDecorator` ajoute des logs sans modifier les stratégies      |
| ✅ Observer Pattern     | Notification automatique de changements dans le nuage de points             |
| ✅ Adapter Pattern      | Permet d’adapter différents loaders vers un modèle unique (`PointCloud`)    |
| ✅ Chain of Responsibility | Pipeline de prétraitement avec des handlers chaînables (`RemoveFloorHandler` → `RemoveOutliersHandler` → ...) |

---

## 🧠 Principes SOLID appliqués

- **S - Single Responsibility** : Chaque classe a une seule responsabilité
- **O - Open/Closed** : Ajout de nouvelles stratégies sans modifier les classes existantes
- **L - Liskov Substitution** : Interfaces respectées par toutes les implémentations
- **I - Interface Segregation** : Interfaces spécifiques et claires (chargement, clustering…)
- **D - Dependency Inversion** : Les contrôleurs dépendent d’abstractions (interfaces)

---

## 📄 Auteurs

Projet réalisé par **Hadil Eltaif** dans le cadre du cours *Approches orientées objet avancées* à l'Université de Sherbrooke.

---

## 📜 Licence

Ce projet est distribué sous licence MIT.
