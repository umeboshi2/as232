from setuptools import setup, find_packages
import sys, os

version = '0.0'

install_requires = [
    'unipath',
    ]


setup(name='as232',
      version=version,
      description="python code to help manipulate git-annex",
      long_description="""\
python code to help manipulate git-annex""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Joseph Rawson',
      author_email='joseph.rawson.works@gmail.com',
      url='https://github.com/umeboshi2/as232',
      license='License name',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
