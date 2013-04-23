from os import path
import site
from setuptools import setup

# fix encoding
sitecustomize_py = path.join(path.dirname(site.__file__), 'sitecustomize.py')
with open(sitecustomize_py, 'w') as f:
    f.write("import sys; sys.setdefaultencoding('utf-8')")

setup(
    name='Rigveda Wiki Mirror', version='0.0.1',
    packages=['rwm'],
    install_requires=[
        'FlaskEx', 'uwsgi', 'cython', 'gevent==1.0dev',
    ],
    dependency_links=[
        'https://github.com/surfly/gevent/tarball/1.0rc2'
        '#egg=gevent-1.0dev'
    ]
)
