from setuptools import setup, find_packages

setup(
    name="dataset-archiver",
    version="2.0.0",
    description="Package dataset directories into reproducible archives",
    author="Omar Haddad",
    author_email="omar.haddad@example.org",
    packages=find_packages(),
    install_requires=["requests>=2.31.0"],
)
