import os

from setuptools import setup


def find_stubs(package):
    stubs = []
    for root, _, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return stubs


with open("README.rst", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="pymongo-stubs",
    version="0.1.0",
    description="Experimental stub files for PyMongo",
    long_description=LONG_DESCRIPTION,
    packages=["pymongo-stubs", "bson-stubs", "gridfs-stubs"],
    package_data={
        "pymongo-stubs": find_stubs("pymongo-stubs"),
        "bson-stubs": find_stubs("bson-stubs"),
        "gridfs-stubs": find_stubs("gridfs-stubs"),
    },
    author="Shane Harvey",
    author_email="drivers-python-noreply@mongodb.com",
    url="https://github.com/mongodb/pymongo-stubs",
    keywords=["mongo", "mongodb", "pymongo", "bson", "gridfs"],
    license="Apache License, Version 2.0",
    # PEP 561 says to use install_requires to list compatible versions
    # https://www.python.org/dev/peps/pep-0561/#stub-only-packages
    install_requires=["pymongo>=3.11,<4.0"],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Database",
        "Typing :: Typed",
    ],
)
