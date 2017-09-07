# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="OpenFisca-Loiret",
    version="0.1.0",
    description="Extension OpenFisca pour les aides sociales du conseil départemental du Loiret",
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    author="",
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'OpenFisca-Core >= 17, < 18',
        'OpenFisca-France >= 18.9, < 19'
        ],
    extras_require = {
        'test': [
            'nose',
            ]
        },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
