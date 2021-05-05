from setuptools import setup, find_packages

setup(
    name='toil_demo',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'marshmallow==3.10.0',
        'toil[all]==5.2.0',
        'pytest==6.2.2',
        'numpy==1.20.1',
        'ipython',
        'ipdb',
    ]
)
