# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='firstclass',
    version='0.1.0',
    description='A simple python course',
    long_description=readme,
    author='Liu Dongqing',
    author_email='liudongqing@gmail.com',
    url='https://github.com/liudongqing/firstclass',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
