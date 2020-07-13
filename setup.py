"""Module to set-up the package."""

from setuptools import find_packages, setup
from typing import List

def readme() -> str:
    """Reads and returns the readme."""
    try:
        with open('README.rst') as f:
            return f.read()
    except FileNotFoundError as e:
        print(f'{e}')
        return ''

def requirements() -> List[str]:
    """Read and returns a list of requirements for package."""
    try:
        with open('requirements.txt') as f:
            return f.read().split('\n')
    except FileNotFoundError:
        return ['']

setup(name='flask_company',
      version='1.0.0',
      description='',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=['Development Status :: 3 - Alpha',
                   'License :: License',
                   'Programming Language :: Python :: 3.7.2',
                   'Topic :: Machine Learning'],
      url='https://github.com/alexjrlewis/flask_company',
      author='Alex J. R. Lewis',
      author_email='alexjrlewis@icloud.com',
      packages=find_packages(exclude=['tests', 'test_*']),
      install_requires=requirements(),
      include_package_data=True,
      zip_safe=False)
