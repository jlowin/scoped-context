from setuptools import setup, find_packages

setup(
    name="scoped_context",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
    description=(
        "A simple context manager package for handling scoped application context."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jeremiah Lowin",
    url="https://github.com/jlowin/scoped-context",
)
