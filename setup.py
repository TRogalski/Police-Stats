try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python web scraping and data processing project',
    'author': 'TRogalski',
    'author_email': 'tomracc@yahoo.com',
    'version': '0.1',
    'install_requires': ['nose', 'bs4', 'requests'], # external dependencies (packages)
    'packages': ['policeStats'],
    'scripts': [],
    'name': 'policeStats'
}

setup(**config)
