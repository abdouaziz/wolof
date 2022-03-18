import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wolof",
    version="0.0.3",
    author="Abdou Aziz DIOP",
    author_email="abdouaziz@gmail.com",
    description="wolof is a python library for the Wolof language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abdouaziz/wolof",
    project_urls={
        "Bug Tracker": "https://github.com/abdouaziz/wolof/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)