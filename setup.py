import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

ROOT_DIR = "CNN_Classifier"
REPO_NAME: str = "End-to-End-ML-project"
AUTHOR_USERNAME: str = "michalgonet"
SRC_REPO: str = "End-to-End-ML-project"
AUTHOR_EMAIL: str = "michal.gonet.mail@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    project_urls={
        "Bug Tracker": f'https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues',
    },
    package_dir={"": ROOT_DIR},
    packages=setuptools.find_packages(where=ROOT_DIR)
)
