from setuptools import find_namespace_packages, setup


setup(name="simple_ml",	version="0.1",
    author="Will Spaeth",
    author_email="jwspaeth0@gmail.com",
    packges=find_namespace_packages(include=["simple_ml", "hydra_plugins.*"]),
    scripts=["scripts/simple_train.py", "scripts/simple_test.py"],
    install_requires=[
        "hydra",
        "hydra-submitit-launcher",
        "pandas",
        "pytorch-lightning",
    ],
    python_requires=">=3.8.5"
    )