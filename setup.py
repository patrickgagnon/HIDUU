from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

#requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="HIDUU",
    version="1.0.3",
    author="Patrick Gagnon",
    author_email="plgagnon00@gmail.com",
    py_modules=["HIDUU"],
    description="A package to upload information to Cerner HealtheIntent",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/patrickgagnon/HIDUU",
    packages=find_packages(),
#    install_requires=requirements.txt,
    classifiers=[ ],
)