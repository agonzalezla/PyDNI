from setuptools import setup, find_packages

setup(
    name="PyDNI",
    version="0.1.0",
    description="Verificador de DNIs y CIFs españoles",
    author="Alberto Gonzalez",
    author_email="agonzalezla@protonmail.com",
    packages=find_packages(),
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules"
        "Natural Language :: Spanish",
    ],
)
