from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="HIDUU",
    version="1.0.5",
    author="Patrick Gagnon",
    author_email="plgagnon00@gmail.com",
    description="A package to upload information to Cerner HealtheIntent",
    long_description=readme,
    url="https://github.com/patrickgagnon/HIDUU",
    packages=['hiduu'],
)