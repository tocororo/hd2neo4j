from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hd2neo4j",
    version="0.1.0",
    author="<Jorge Luis Arencibia>",
    author_email="<jorge9815rdz@gmail.com>",
    description="yet another tool for transforming heterogeneous data in to knowledge graph",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
