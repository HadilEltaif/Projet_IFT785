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

Le projet applique plusieurs **design patterns classiques** afin d’assurer une architecture souple, modulaire et extensible :

- **✅ Factory Pattern** : utilisé dans `factories/loader_factory.py` pour instancier dynamiquement des chargeurs selon l’extension du fichier (.pcd, .ply, .bin).
- **✅ Strategy Pattern** : dans `strategies/`, chaque traitement (suppression du sol, outliers, downsampling...) est interchangeable via une interface `IPreprocessing`.
- **✅ Singleton Pattern** : le fichier `utils/config.py` implémente un singleton `GlobalConfig` pour centraliser la configuration globale de l’application.
- **✅ Command Pattern** : toutes les actions métier comme téléverser, prétraiter ou visualiser sont encapsulées sous forme de commandes dans `commands.py`, ce qui permet un contrôle clair et réutilisable.
- **✅ Decorator Pattern** : les stratégies de prétraitement peuvent être enveloppées dans des décorateurs comme `StrategyLoggerDecorator` pour ajouter dynamiquement des logs ou métriques sans modifier les classes d'origine.
---

## 🧭 Principes SOLID appliqués

Le projet respecte plusieurs principes SOLID pour garantir une base de code propre, testable et évolutive :

- **S — Single Responsibility Principle (SRP)** : chaque module (loader, service, strategy) a une responsabilité unique.
- **O — Open/Closed Principle (OCP)** : il est possible d’ajouter de nouvelles stratégies ou extensions sans modifier le code existant.
- **L — Liskov Substitution Principle (LSP)** : les interfaces `ILoader`, `IPreprocessing` permettent d’échanger librement les implémentations.
- **I — Interface Segregation Principle (ISP)** : chaque interface est spécialisée (ex: séparation IClustering / IPreprocessing).
- **D — Dependency Inversion Principle (DIP)** : les composants dépendent d’abstractions (interfaces) plutôt que d’implémentations concrètes, ce qui facilite le test unitaire et le remplacement dynamique.

## 🧪 Tests

Les tests unitaires seront ajoutés dans le dossier `tests/` pour valider le comportement de chaque composant (services, loaders, stratégies).

---

## 👩‍💻 Développé par

Hadil Eltaif  
Université de Sherbrooke  
Laboratoire DOMUS 💚