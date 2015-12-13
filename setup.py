#-*- coding: utf-8 -*-
from distutils.core import setup
from guate import division_politica

with open('README.md', 'r') as ld:
    long_description = ld.read()

setup_args = dict(
    name='guate.division-politica',
    version=division_politica.__version__,
    packages=['guate.division_politica'],
    include_package_data=True,
    author='Darwin Monroy',
    author_email='contact@darwinmonroy.com',
    description='División Política de Guatemala',
    long_description=long_description

)


if __name__ == '__main__':
    setup(**setup_args)
