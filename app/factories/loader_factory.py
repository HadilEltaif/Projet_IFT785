from app.loaders.pcd_loader import PCDLoader
from app.loaders.ply_loader import PLYLoader
from app.loaders.bin_loader import BINLoader
from app.utils.config import GlobalConfig  # 🔁 Ajout

class LoaderFactory:
    @staticmethod
    def get_loader(filepath):
        config = GlobalConfig()  # 🔁 Singleton

        extension = filepath.split(".")[-1].lower()

        if config.debug:
            print(f"[DEBUG] Tentative de chargement du fichier : {filepath}")
            print(f"[DEBUG] Extension détectée : {extension}")

        loaders = {
            "pcd": PCDLoader(),
            "ply": PLYLoader(),
            "bin": BINLoader()
        }

        loader = loaders.get(extension)
        if not loader:
            raise ValueError(f"Format non supporté : {extension}")

        if config.debug:
            print(f"[DEBUG] Utilisation du loader : {loader.__class__.__name__}")

        return loader
