from setuptools import setup, find_packages

setup(
    name="my_library",  # Nom de la bibliothèque
    version="0.1.0",  # Version initiale
    author="meryam elmaaroufy",
    author_email="elmaaroufymaryeme@gmail.com",
    description="Une bibliothèque Python pour démonstration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/votre-repo/my_library",  # URL du projet
    packages=find_packages(),  # Trouve automatiquement les packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # Dépendances du projet (à inclure si nécessaire)
    ],
)
