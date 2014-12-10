#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='pyscss_pkg_resources',
    version='0.1',
    author='Gary van der Merwe',
    author_email="garyvdm@gmail.com",
    description="pyScss extension to allow for loading of import for pkg_resource.",
    license="GPL",
    packages=['pyscss_pkg_resources', ],
    include_package_data=True,
    package_data={'': ['*.scss']},
    install_requires=['pyScss', ],
    test_suite='pyscss_pkg_resources.tests',
)
