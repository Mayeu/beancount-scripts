# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['bean-extract-price']
install_requires = \
['beancount>=2.2,<3.0']

setup_kwargs = {
    'name': 'beancount-scripts',
    'version': '1.0.3',
    'description': 'Scripts I use for my accounting using beancount',
    'long_description': None,
    'author': 'Mayeu',
    'author_email': 'm@mayeu.me',
    'url': 'https://github.com/Mayeu/beancount-scripts',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
    'scripts': ['bin/bean-extract-price']
}


setup(**setup_kwargs)
