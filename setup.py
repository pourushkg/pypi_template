import setuptools 

with open('README.md','r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "MY_IPYNB_PACKAGE"
AUTHOR_NAME = "pourushkg"
SRC_REPO = "MY_IPYNB_PACKAGE"
AUTHOR_EMAIL = "pkg.21p10161@mtech.nitdgp.ac.in"
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
    
)