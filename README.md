# 🚀 Lidar Clustering Web App

Ce projet est une application web développée en Python avec Flask, orientée objet, qui permet de :
- charger des fichiers LiDAR au format `.pcd`,
- effectuer un **prétraitement** (filtrage, nettoyage, downsampling),
- appliquer un **clustering adaptatif** (DBSCAN),
- afficher les résultats via une interface web simple.

## 📁 Structure du projet

```
lidar_clustering_web/
├── app/                    # Code principal de l'application
│   ├── controllers/        # Logique de routing (Flask)
│   ├── models/             # Algorithmes et structures de données
│   ├── services/           # Prétraitement et logique métier
│   ├── templates/          # Fichiers HTML (Jinja2)
│   ├── static/             # Fichiers CSS / JS
│   └── config.py           # Configuration globale
│
├── tests/                  # Tests unitaires et d'intégration
│   ├── unit/
│   └── integration/
│
├── run.py                 # Point d’entrée Flask
├── requirements.txt       # Dépendances
├── README.md              # Ce fichier
└── .gitignore
```

## 🧱 Tech Stack

- Python 3.10+
- Flask (framework web)
- Open3D (visualisation et traitement de nuages de points)
- NumPy, Scikit-learn (DBSCAN)
- HTML, Jinja2 (templates)
- Pytest (tests)

## ✅ Fonctionnalités à venir

- [ ] Upload de fichiers `.pcd` via l'interface
- [ ] Visualisation des clusters
- [ ] Export des résultats
- [ ] Historique des fichiers traités
- [ ] Affichage statistique par cluster

## 🧪 Lancer les tests

```bash
pytest tests/
```

## ▶️ Exécuter le projet

```bash
python run.py
```

Ou via Flask :

```bash
export FLASK_APP=run.py
flask run
```

## 👨‍💻 Auteurs

Projet développé par **Hadil Eltaif** dans le cadre du cours **IFT785 - Développement Orienté Objet Avancé**.
