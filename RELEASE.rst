=========================
pymongo-stubs Releases
=========================

Versioning
----------

pymongo-stubs's version numbers follow `semantic versioning`_: each version
number is structured "major.minor.patch". Patch releases fix bugs, minor
releases add features (and may fix bugs), and major releases include API
changes that break backwards compatibility (and may add features and fix
bugs).

In between releases we add .devN to the version number to denote the version
under development. So if we just released 1.0.0, then the current dev
version might be 1.0.1.dev0 or 1.1.0.dev0.

.. _semantic versioning: http://semver.org/

Release Process
---------------

#. Add a changlog entry for this release in CHANGELOG.rst.
#. Bump "version" in setup.py. Commit the change and tag
   the release. Immediately bump the "version" to "dev0" in a new commit::

     $ # Bump to release version number
     $ git commit -a -m "pymongo-stubs <release version number>"
     $ git tag -a "pymongo-stubs <release version number>"
     $ # Bump to dev version number
     $ git commit -a -m "BUMP pymongo-stubs <release version number>"
     $ git push
     $ git push --tags

#. Build the release packages::

     $ git clone git@github.com:mongodb-labs/pymongo-stubs.git
     $ cd pymongo-stubs/
     $ git checkout "pymongo-stubs <release version number>"
     $ python3 setup.py sdist
     $ python3 setup.py bdist_wheel

   This will create the following distributions::

     $ ls dist
     pymongo-stubs-<version>.tar.gz
     pymongo-stubs-<version>-py3-none-any.whl

#. Upload all the release packages to PyPI with twine::

     $ python3 -m twine upload dist/*

