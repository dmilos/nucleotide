#!/usr/bin/env python2

#   Copyright 2015 Dejan D. M. Milosavljevic
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License. 


import os
import subprocess

import nucleotide
import nucleotide.component
import nucleotide.component.function



def _python_linux_default_CPPFLAGS( P_list ):
    try:
        p = subprocess.Popen( [ '/usr/bin/python-config', ' --cflags' ],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    except :
        return []
        
    output, error = p.communicate()
    if( None != error ):
        return []

    return output.split()

def _python_linux_default_LINKFLAGS( P_list ):
    try:
        p = subprocess.Popen( [ '/usr/bin/python-config', ' --ldflags' ],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    except :
        return []

        output, error = p.communicate()
    if( None != error ):
        return []

    return output.split()

atom_python_linux_default = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
            'CPPFLAGS' : _python_linux_default_CPPFLAGS,
            'LINKFLAGS': _python_linux_default_LINKFLAGS,
    },
    'name' : 'python:linux:default',
    'class': [ 'python', 'python:default', 'python:linux:default' ]
}

def _python27_linux_CPPFLAGS( P_list ):
    try:
        p = subprocess.Popen( [ '/usr/bin/python2-config', ' --cflags' ],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    except :
        return _python_linux_default_CPPFLAGS(P_list)

    output, error = p.communicate()
    if( None != error ):
        return []

    return output.split()

def _python27_linux_LINKFLAGS( P_list ):
    try:
        p = subprocess.Popen( [ '/usr/bin/python2-config', ' --ldflags'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    except :
        return _python_linux_default_LINKFLAGS( P_list )

    output, error = p.communicate()
    if( None != error ):
        return []

    return output.split()


atom_python27_linux= {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor': 'FSF',
        'name': 'gcc',
        'version': 'X'
    },
    'config' : {
        'CPPFLAGS' : _python27_linux_CPPFLAGS,
        'LINKFLAGS': _python27_linux_LINKFLAGS,
    },
    'name' : 'python27:linux',
    'class':  [ 'python', 'python:default', 'python:linux:default', 'python27:default' , 'python27:linux' ]
}

def _python35_linux_CPPFLAGS( P_list ):
    try:
        p = subprocess.Popen( [ '/usr/bin/python3-config', ' --cflags' ],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    except :
        return _python_linux_default_CPPFLAGS(P_list)

    output, error = p.communicate()
    if( None != error ):
        return []

    return output.split()

def _python35_linux_LINKFLAGS( P_list ):
    try:
        p = subprocess.Popen( [ '/usr/bin/python3-config', ' --ldflags' ],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    except :
        return _python_linux_default_LINKFLAGS(P_list)

    output, error = p.communicate()
    if( None != error ):
        return []

    return output.split()


atom_python35_linux= {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor': 'FSF',
        'name': 'gcc',
        'version': 'X'
    },
    'config' : {
        'CPPFLAGS' : _python35_linux_CPPFLAGS,
        'LINKFLAGS': _python35_linux_LINKFLAGS,
    },
    'name' : 'python35:linux',
    'class':  [ 'python', 'python:default', 'python:linux:default', 'python35:default', 'python35:linux' ]
}

class Python:
    def __init__(self):
        pass

    @staticmethod
    def extend(P_option):
        nucleotide.component.function.extend( P_option, 'python:linux:default',  atom_python_linux_default )
        nucleotide.component.function.extend( P_option, 'python27:linux',        atom_python27_linux )
        nucleotide.component.function.extend( P_option, 'python35:linux',        atom_python35_linux )

    def check(self):
        nucleotide.component.function.check__env( 'PYTHONPATH' )
