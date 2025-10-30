"""
FritzBox Tray - A system tray application for interacting with FRITZ!Box devices.
Copyright (C) 2023 Andreas Violaris

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
import os
from setuptools import setup, find_namespace_packages

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(project_urls={
    'Homepage': 'https://github.com/lineaje-labs-gos/fritzbox-tray',
    'Repository': 'https://github.com/lineaje-labs-gos/fritzbox-tray',
    'Tracker': 'https://github.com/lineaje-labs-gos/fritzbox-tray/issues',
  }, 
  maintainer_email="221268890+Lineaje-DepFixer@users.noreply.github.com", 
  maintainer="Lineaje DepFixer", 
    name='fritzbox-tray',
    version="1.0.60+lineaje.1",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "fritzbox_tray": ["*.py"],
        "fritzbox_tray.resources": ["*.ico"],
    },
    description='A system tray application for interacting with FRITZ!Box devices.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['fritz', 'fritzbox', 'fritz-box', 'fritzbox-tray', 'fritzbox_tray',
              'avm-fritz', 'tray', 'python', 'pypi', 'python3', 'tray',
              'tray-application', 'pypi-package', 'tray-app'],
    author='Andreas Violaris',
    url="https://github.com/lineaje-labs-gos/fritzbox-tray",
    install_requires=['pillow==10.3.0'] + [req for req in requirements if not req.startswith('pillow')],
    entry_points={
        'gui_scripts': [
            'fritzbox-tray=fritzbox_tray.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)