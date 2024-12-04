"""
Setup script for the Image Classifier package.
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="groupX",
    version="1.0.0",
    author="groupX",
    description="CSCN73010: image classifier ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jschulz8138/Image-Classifier",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "flask",
        "numpy",
        "opencv-python",
        "matplotlib",
        "tensorflow",
    ],
    extras_require={
        "test": [
            "pytest",
        ],
    },
    python_requires=">=3.11",
)
