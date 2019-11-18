from setuptools import setup

setup(
    name='uchicago',
    version='0.01',
    description='tools for living life at uchicago',
    author='Anand Jain',
    author_email='anandj@uchicago.edu',
    packages=['uchicago'],  # same as name
    install_requires=['selenium',
                      'bs4',
                      'requests',
                      'xml'
                      ]  # external packages as dependencies
)
