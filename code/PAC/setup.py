from setuptools import setup

setup(
    name='PAC',
    version='0.0.0',
    description='A python implementation of the PAC learning framework',
    author='Mohammed D. Belgoumri',
    author_email='mohammedbelgoumri@gmail.com',
    license='MIT',
    packages=['PAC'],
    install_requires=[
        'numpy',
        'scipy',
        'sympy',
    ]
)