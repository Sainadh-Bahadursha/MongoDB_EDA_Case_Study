import importlib.metadata
packages = [
    "pymongo",
    "pandas",
    "python-dotenv",
    "numpy",
    "matplotlib",
    "seaborn",
    "notebook",
    "jupyter",
    "tqdm",
    "python-dotenv"
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")