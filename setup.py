import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "coccidiosisDiseaseClassification"
AUTHOR_USER_NAME = "lakshitcodes"
SRC_REPO = "coccidiosisDiseaseClassification"
AUTHOR_EMAIL = "jainlakshit849@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lakshitcodes/Coccidiosis-Disease-Classification",
    project_urls={
        "Bug_Tracker": "https://github.com/lakshitcodes/Coccidiosis-Disease-Classification/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
