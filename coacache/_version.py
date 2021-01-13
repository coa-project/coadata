# -*- coding: utf-8 -*-

"""
Project : PyCoA-CoaCache
Date :    january 2021
Authors : Olivier Dadoun, Julien Browaeys, Tristan Beau
Copyright ©pycoa.fr

Module : coacache._version

About : Provides cached version of some data used by the pycoa project, if those data became unavailable.

"""

# Store the version here so:
# 1) we don't load dependencies by storing it in __init__.py
# 2) we can import it in setup.py for the same reason
# 3) we can import it into your module module
# see : https://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package

__version__ = '202101'
__author__= 'Tristan Beau, Julien Browaeys, Olivier Dadoun'
__email__= 'support@pycoa.fr'
