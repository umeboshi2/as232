from setuptools import setup, find_packages
import sys, os

install_requires = [
    'hornstone',
    ]


setup_requirements = [
    'pytest-runner',
    # TODO(umeboshi2): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(name='as232',
      version='0.1.0',
      description="python code to help manipulate git-annex",
      long_description="""\
python code to help manipulate git-annex""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Joseph Rawson',
      author_email='joseph.rawson.works@gmail.com',
      url='https://github.com/umeboshi2/as232',
      license='Public Domain',
      packages=find_packages(include=['as232'],
                             exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points={
          'console_scripts': [
              'gadupes = as232.scripts.gadupes:main',
              ]
          },
      )
