# pylint: disable=invalid-name, exec-used
"""Setup georideapilib package."""
from __future__ import absolute_import

import os
import sys

from setuptools import setup

sys.path.insert(0, '.')

CURRENT_DIR = os.path.dirname(__file__)

# to deploy to pip, please use
# make pythonpack
# python setup.py register sdist upload
# and be sure to test it firstly using
# "python setup.py register sdist upload -r pypitest"
setup(
    name='georideapilib',
    packages=['georideapilib', 'georideapilib.objects'],  # this must be the same as the name above
    version='0.9.6',
    description='Lib to control GeoRide tracker devices with theire rest api',
    author='Matthieu DUVAL',
    author_email='georideapilib@duval-dev.fr',
    # use the URL to the github repo
    url='https://github.com/hacf/georide-api',
    download_url='https://codeload.github.com/hacf/georide-api/tar.gz/0.9.3',
    keywords=['rest', 'georide', 'api', 'grutier', 'GeoRide'],  # arbitrary keywords
    classifiers=[],
    install_requires=["python-socketio[client]==4.6.1"],
    tests_require=[
        'pytest>=3.7',
        'pytest-pep8',  
        'pytest-cov',
        'python-coveralls',
        'pylint',
        'coverage>=4.4'
    ]
)