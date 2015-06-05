#!/usr/bin/env python
from distutils.core import setup, Extension

setup(
    name='x64dbg',
    version='1.0',
    description='Python x64dbg sdk library',
    author='Tomer Zait (RealGame)',
    author_email='realgam3@gmail.com',
    py_modules=['_x64dbg'],
    ext_modules=[Extension(
            '__x64dbg', ['__x64dbg.cpp'],
            language='c++',
            include_dirs=[r'..\pluginsdk'],
            library_dirs=[r'..\pluginsdk'],
            libraries=['x32_bridge', 'x32_dbg'],
    )]
)
