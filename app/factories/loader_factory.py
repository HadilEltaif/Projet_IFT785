from app.loaders.pcd_loader import PCDLoader
from app.loaders.ply_loader import PLYLoader
from app.loaders.bin_loader import BINLoader

class LoaderFactory:
    @staticmethod
    def get_loader(filepath):
        extension = filepath.split(".")[-1].lower()
        loaders = {
            "pcd": PCDLoader(),
            "ply": PLYLoader(),
            "bin": BINLoader()
        }
        loader = loaders.get(extension)
        if not loader:
            raise ValueError(f"Format non supporté : {extension}")
        return loader

