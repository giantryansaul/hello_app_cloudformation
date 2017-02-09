from setuptools import setup, find_packages

setup(
    name='hello_app_cloudformation',
    packages=find_packages(),
    version='1.0.0',
    url='https://github.com/giantryansaul/hello_app_cloudformation',
    author='Ryan Saul',
    author_email='giantryansaul@gmail.com',

    install_requires=[
        'boto3',
        'jinja2'
    ],
)
