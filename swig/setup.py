#!/usr/bin/env python
import sys
from distutils.core import setup, Extension

def is_64bit():
    return sys.maxsize > 2**32

setup(
    name='x64dbg_python',
    version='1.0',
    description='Python x64dbg SDK Library',
    author='Tomer Zait (RealGame)',
    author_email='realgam3@gmail.com',
    packages=['x64dbg_python'],
    ext_modules=[Extension(
            r'x64dbg_python.__x64dbg', [r'x64dbg_python\__x64dbg.cpp'],
            language='c++',
            include_dirs=[r'..\pluginsdk'],
            library_dirs=[r'..\pluginsdk'],
            libraries=['x64bridge', 'x64dbg'] if is_64bit() else ['x32bridge', 'x32dbg'],
    )]
)
