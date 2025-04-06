from app.factories.loader_factory import LoaderFactory

def load_file(filepath):
    ext = filepath.split('.')[-1]
    loader = LoaderFactory.get_loader(ext)
    return loader.load(filepath)
