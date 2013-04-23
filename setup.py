#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "django-keyval",
    version = "1.0",
    url = 'http://ondrejsika.com/docs/django-keyval',
    download_url = 'https://github.com/sikaondrej/django-keyval',
    license = 'GNU LGPL v.3',
    description = "",
    author = 'Ondrej Sika',
    author_email = 'dev@ondrejsika.com',
    packages = find_packages(),
    requires = ["django", ],
    include_package_data = True,
    zip_safe = False,
)
