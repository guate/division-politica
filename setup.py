from setuptools import setup

with open('README.md', 'r') as ld:
    long_description = ld.read()

setup_args = dict(
    name='guate.division-politica',
    use_scm_version=True,
    packages=['guate.division_politica'],
    include_package_data=True,
    author='Darwin Monroy',
    author_email='contact@darwinmonroy.com',
    description='División Política de Guatemala',
    long_description=long_description,
    setup_requires=[
        'setuptools_scm',
    ],
    install_requires=[
        'attrdict',
        'chilero>=0.3.8'
    ]
)


if __name__ == '__main__':
    setup(**setup_args)
