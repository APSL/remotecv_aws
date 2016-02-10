# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='remotecv_aws',
    version='0.1',
    description='Remotecv AWS loader',
    author='Edu Heraiz @ APSL',
    author_email='gshark@gmail.com',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'botocore>=1.2.0',
    ],
    extras_require={
    },
)