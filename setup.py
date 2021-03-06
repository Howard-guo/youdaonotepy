#!/usr/bin/env python

from distutils.core import setup
import ynote

if ynote.__version__.endswith('b'):
    dev_status = 'Development Status :: 4 - Beta'
else:
    dev_status = 'Development Status :: 5 - Production/Stable'

kw=dict(name = 'ynote',
    version = ynote.__version__,
    description = 'Youdao Note Python SDK',
    long_description = open('README', 'r').read(),
    author = 'Li Chuan',
    author_email = 'daniellee0219@gmail.com',
    url = 'https://github.com/daniellee219/youdaonotepy',
    download_url = 'https://github.com/daniellee219/youdaonotepy',
    packages = ['ynote'],
    license = 'Apache License, Version 2.0',
    classifiers = [
        dev_status,
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])

setup(**kw)
