# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Cristian Kamia',
    author_email='cnk_2806@me.com',
    url='https://github.com/xcnkx/cli_sample_mod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
    install_requires=['hoge', 'unko'],
    dependency_links=['git+ssh://git@github.com/USERNAME/unko.git#egg=unko'],
)

