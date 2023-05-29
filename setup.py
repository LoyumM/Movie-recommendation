from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Movie-Recommendation"
AUTHOR_USER_NAME = "LoyumM"
SRC_REPO = "src"
# LIST_OF_REQUIREMENTS = ['streamlit']
LIST_OF_REQUIREMENTS = [
    'streamlit==1.22.0',
    'pandas==1.0.1',
    'pickle==4.0',
    'requests==2.31.0',
]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="imbmoirangthem033@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS
)
