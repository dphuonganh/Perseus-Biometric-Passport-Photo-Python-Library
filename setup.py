# Copyright (C) 2019 Majormode.  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os

import pipfile
import setuptools


__author__ = "Daniel CAUNE"
__copyright__ = "Copyright (C) 2019, Majormode"
__credits__ = ["Daniel CAUNE"]
__email__ = "daniel.caune@gmail.com"
__license__ = "MIT"
__maintainer__ = "Daniel CAUNE"
__status__ = "Production"
__version__ = '1.0.0'


# Base directory where this file is located.
BASE_DIR = os.path.dirname(__file__)


def get_requirements():
    pip_file = pipfile.load()
    return os.linesep.join([
        package_name
        for package_name, package_version in pip_file.data['default'].items()])


def read_file(file_path_name):
    with open(file_path_name, mode='rt', encoding='utf-8') as fd:
        return fd.read()


setuptools.setup(
    author=__author__,
    author_email=__email__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
    description='Biometric Passport Photo Python Library',
    install_requires=get_requirements(),
    license=__license__,
    long_description=read_file(os.path.join(BASE_DIR, 'README.md')),
    long_description_content_type='text/markdown',
    name='perseus-biometric-passport-photo-library',
    packages=setuptools.find_packages(),
    platforms=['any'],
    project_urls={
        'Bug Tracker': 'https://github.com/dcaune/perseus-biometric-passport-photo-python-library/issues',
        'Documentation': 'https://github.com/dcaune/perseus-biometric-passport-photo-python-library',
        'Source Code': 'https://github.com/dcaune/perseus-biometric-passport-photo-python-library',
    },
    python_requires='>=3.6',
    version=__version__
)
