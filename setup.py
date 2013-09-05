"""Cubic Spline Approximation (CSA) library wrapper

Python wrapper for csa-c by Pavel Sakov (pavel.sakov@nersc.no):

    https://code.google.com/p/csa-c/

Based on an algorithm by:

    Haber, J., Zeilfelder, F., Davydov, O., and Seidel, H. P. (2001). 
    Smooth approximation and rendering of large scattered data sets. 
    In Proceedings of the conference on Visualization '01, 
    pages 341-348. IEEE Computer Society.

Python wrapper by Robert Hetland (hetland@tamu.edu)


Python code Copyright (c) 2013 Robert Hetland

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

classifiers = """\
Development Status :: beta
Environment :: Console
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: MIT
Operating System :: OS Independent
Programming Language :: Python
Topic :: Scientific/Engineering
Topic :: Software Development :: Libraries :: Python Modules
"""

from numpy.distutils.core import Extension

csa = Extension(name = '_csa',
                sources=["src/csa.c",
                         "src/svd.c"])

doclines = __doc__.split("\n")

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(name = "octant",
          version = '0.1.0',
          description = doclines[0],
          long_description = "\n".join(doclines[2:]),
          author = "Robert Hetland",
          author_email = "hetland@tamu.edu",
          url = "http://octant.googlecode.com/",
          packages = ['csa'],
          license = 'MIT',
          platforms = ["any"],
          ext_package='csa',
          ext_modules = [csa],
          classifiers = filter(None, classifiers.split("\n")),
          )
    
