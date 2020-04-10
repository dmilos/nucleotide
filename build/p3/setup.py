from setuptools import find_packages
from distutils.core import setup
import time

import os
import glob

rootdir = os.path.abspath( os.path.dirname(__file__) )
print ( rootdir )

#my_version = "0.1.0" +  str(time.time()),
my_version = "0.1.4.8"

my_packages = find_packages( rootdir )

with open( os.path.join( rootdir, "readme.txt" ), "r") as fh:
    my_long_description = fh.read()

print ( my_long_description )
print ( my_packages )

setup(
    name="nucleotide",
    version          = my_version,
    keywords         = 'scons, module, universal, unified, compiler, c++',
    author           = "Dejan Milosavljevic",
    author_email     = "dmilos@gmail.com",
    url              = "https://github.com/dmilos/nucleotide",
    license          = "https://raw.githubusercontent.com/dmilos/nucleotide/master/license.txt",
    packages         = my_packages,
    description      = "An Scons library which wraps interface of various compilers in to one universal.",
    long_description = my_long_description,
    platforms        = ["All"],
    #install_requires = [ "scons"  ],
    # NO scripts = [ "nucleotide"  ]
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Build Tools'
    ],
)
