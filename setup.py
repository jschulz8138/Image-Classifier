from setuptools import setup, find_packages

setup(
    name="image_classifier",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tensorflow", "matplotlib", "numpy", "keras"  # Add any required dependencies
    ],
    description="An image classifier model",
)
