from setuptools import setup, find_packages

setup(
    name="my_library",  
    version="0.1.0",  
    author="maryeme elmaaroufy",
    author_email="elmaaroufymaryeme@gmail.com",
    description="Une bibliothèque Python pour démonstration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="", 
    packages=find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
    
    ],
)
