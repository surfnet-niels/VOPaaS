from setuptools import setup, find_packages

setup(
    name='VOPaaS',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/its-dirg/VOPaaS',
    license='Apache License 2.0',
    author='DIRG',
    author_email='dirg@its.umu.se',
    description='Protocol proxy for the Virtual Organization Platform as a Service (VOPaaS).',
    install_requires=[
        'satosa==0.4.1'
    ]
)
