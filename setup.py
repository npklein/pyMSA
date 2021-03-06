# Copyright (c) 2012 - N.P. de Klein
#
#     This file is part of Python Mass Spec Analyzer (PyMSA).
#
#     Python Mass Spec Analyzer (PyMSA) is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     Python Mass Spec Analyzer (PyMSA) is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with Python Mass Spec Analyzer (PyMSA).  If not, see <http://www.gnu.org/licenses/>.")

from distutils.core import setup

setup(
    name='PyMSA',
    version='0.3.0',
    author='N.P. de Klein, D.M.A. Martin',
    author_email='niekdeklein@gmail.com',
    packages=['pyMSA', 'pyMSA.test'],
    license='LICENSE.txt',
    description='MS/MS analyzing tools',
    scripts = ['bin/featureFinder.sh', 'bin/featureMapper.sh'],
    long_description=open('README.txt').read(),
)
