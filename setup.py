#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "django-keyvalue",
    version = "1.0",
    url = 'http://ondrejsika.com/docs/django-keyvalue',
    download_url = 'https://github.com/sikaondrej/django-keyvalue',
    license = 'GNU LGPL v.3',
    description = "",
    author = 'Ondrej Sika',
    author_email = 'dev@ondrejsika.com',
    packages = find_packages(),
    requires = ["django", ],
    include_package_data = True,
    zip_safe = False,
)
