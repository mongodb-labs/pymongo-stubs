==================================================
pymongo-stubs: Experimental stub files for PyMongo
==================================================

Experimental stub files for `PyMongo`_ 3.

**pymongo-stubs is NOT an officially supported MongoDB product.**

Example
=======

.. image:: https://raw.githubusercontent.com/mongodb-labs/pymongo-stubs/main/images/screencast.gif

Installation
============

pymongo-stubs can be installed with `pip`_::

  $ python3 -m pip install pymongo-stubs

Installing from source
----------------------

pymongo-stubs' source code is hosted on Github: `mongodb-labs/pymongo-stubs`_.
To install pymongo-stubs from source::

  $ git clone git@github.com:mongodb/pymongo-stubs.git
  $ python3 -m pip install ./pymongo-stubs

Dependencies
============

pymongo-stubs is compatible with Python >=3.6 and `PyMongo`_ >=3.11,<4.0.

Roadmap
=======

pymongo-stubs adds support for type checking `PyMongo`_ 3.X code. This project
will not support PyMongo 4. Instead, PyMongo 4 will add inline type
annotations (in `PYTHON-2432`_) which removes the need to maintain stub files.
This project will reach end-of-life when `PYTHON-2432`_ is completed or when
MongoDB drops support for `PyMongo`_ 3.X.

Support / Feedback
==================

pymongo-stubs is experimental and is not an officially supported MongoDB product.
For questions, discussions, or general technical support, visit the
`MongoDB Community Forums`_.

Bugs / Feature Requests
=======================

Think you’ve found a bug? Please open a case in our issue management tool, JIRA:

- `Create an account and login <https://jira.mongodb.org>`_.
- Navigate to `the PYTHON project <https://jira.mongodb.org/browse/PYTHON>`_.
- Click **Create Issue** - Please provide as much information as possible about the issue type and how to reproduce it.

Bug reports in JIRA for all driver projects (i.e. PYTHON, CSHARP, JAVA) and the
Core Server (i.e. SERVER) project are **public**.

.. _PyMongo: https://pypi.org/project/pymongo/
.. _PYTHON-2432: https://jira.mongodb.org/browse/PYTHON-2432
.. _pip: https://pypi.python.org/pypi/pip
.. _mongodb-labs/pymongo-stubs: https://github.com/mongodb-labs/pymongo-stubs
.. _MongoDB Community Forums: https://developer.mongodb.com/community/forums/tag/python
