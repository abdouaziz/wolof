from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="wolof",
        version="0.1.0",
        description="wolof is a python library for the Wolof language",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Abdou Aziz DIOP",
        author_email="abdouaziz@gmail.com",
        url="https://github.com/abdouaziz/wolof",
        license="Apache License",
        packages=find_packages(),
        include_package_data=True,
        install_requires=["torch", "transformers", "numpy", "tqdm"],
        platforms=["linux", "unix"],
        python_requires=">3.5.2",
    )