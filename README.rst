=====
as232
=====


.. image:: https://img.shields.io/pypi/v/as232.svg
        :target: https://pypi.python.org/pypi/as232

.. image:: https://img.shields.io/travis/umeboshi2/as232.svg
        :target: https://travis-ci.org/umeboshi2/as232

.. image:: https://readthedocs.org/projects/as232/badge/?version=latest
        :target: https://as232.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/umeboshi2/as232/shield.svg
     :target: https://pyup.io/repos/github/umeboshi2/as232/
     :alt: Updates


python code to help manipulate git-annex


* Free software: UNLICENSED
* Documentation: https://as232.readthedocs.io.



Getting Started
---------------

- Change directory into your newly created project.

    cd as232

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Configure the database.

    env/bin/initialize_as232_db development.ini

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

