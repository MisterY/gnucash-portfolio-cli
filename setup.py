""" The minimal setup """

from setuptools import setup

setup(name='gnucash_portfolio_cli',
      version='1.1.0',
      description='command-line interface to Gnucash Portfolio',
      url='https://github.com/MisterY/gnucash-portfolio-cli',
      author='Alen Siljak',
      author_email='alen.siljak@gmx.com',
      license='GPL version 3',
      packages=['gnucash_portfolio_cli'],
      install_requires=['gnucash_portfolio']
)
