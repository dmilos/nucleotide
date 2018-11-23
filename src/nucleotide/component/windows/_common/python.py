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



def _python_default_CPPPATH( P_list ):
    return [ os.getenv('PYTHON_INCLUDE') ]

def _python_default_LIBPATH( P_list ):
    return [ os.getenv('PYTHON_LIBPATH') ]

def _python_default_LIBS( P_list ):
    #TODO 'python' + P_list['version']
    return [ 'pythonXYZ' ]

atom_python_default = {
    'platform' : {
        'host'  : 'X',
        'guest' : 'X'
    },
    'cc' : {
        'vendor' : 'X',
        'name'   : 'X',
        'version': 'X'
    },
    'config' : {
            'CPPPATH'  : _python_default_CPPPATH,
            'LIBPATH'  : _python_default_LIBPATH,
            'LIBS'     : _python_default_LIBS
    },
    'name' : 'python:default',
    'class': [ 'python', 'python:default' ]
}


def _python27_default_CPPPATH( P_list ):
    I_result = os.getenv('PYTHON27_INCLUDE')
    if( None == I_result ):
        return _python_default_CPPPATH( P_list )
    return [ I_result ]

def _python27_default_LIBPATH( P_list ):
    I_result = os.getenv('PYTHON27_LIBPATH')
    if( None == I_result ):
        return _python_default_LIBPATH( P_list )
    return [ I_result ]

atom_python27_default = {
    'platform' : {
        'host'  : 'X',
        'guest' : 'X'
    },
    'cc' : {
        'vendor'  : 'X',
        'name'    : 'X',
        'version' : 'X'
    },
    'config' : {
            'CPPPATH'  : _python27_default_CPPPATH,
            'LIBPATH'  : _python27_default_LIBPATH,
            'LIBS'   : [ 'python27' ]
    },
    'name' : 'python27:default',
    'class':  [ 'python', 'python:default', 'python27:default' ]
}


def _python35_default_CPPPATH( P_list ):
    I_result = os.getenv('PYTHON35_INCLUDE')
    if( None == I_result ):
        return _python_default_CPPPATH( P_list )
    return [ I_result ]

def _python35_default_LIBPATH( P_list ):
    I_result = os.getenv('PYTHON35_LIBPATH')
    if( None == I_result ):
        return _python_default_LIBPATH( P_list )
    return [ I_result ]

atom_python35_default = {
    'platform' : {
        'host'  : 'X',
        'guest' : 'X'
    },
    'cc' : {
        'vendor': 'X',
        'name': 'X',
        'version': 'X'
    },
    'config' : {
            'CPPPATH'  : _python35_default_CPPPATH,
            'LIBPATH'  : _python35_default_LIBPATH,
            'LIBS'   : [ 'python35' ]
    },
    'name' : 'python35:default',
    'class': [  'python', 'python:default', 'python35:default' ]
}

class Python:
    def __init__( self ):
        pass

    @staticmethod
    def extend( P_option ) :
        nucleotide.component.function.extend( P_option, 'python:default',    atom_python_default   )
        nucleotide.component.function.extend( P_option, 'python27:default',  atom_python27_default )
        nucleotide.component.function.extend( P_option, 'python35:default',  atom_python35_default )

    @staticmethod
    def check():
        nucleotide.component.function.check__env( 'PYTHONPATH' )
        nucleotide.component.function.check__env( 'PYTHON_INCLUDE' )
        nucleotide.component.function.check__env( 'PYTHON_LIBPATH' )
        nucleotide.component.function.check__env( 'PYTHON_VERSION' )

        nucleotide.component.function.check__env( 'PYTHON27_INCLUDE' )
        nucleotide.component.function.check__env( 'PYTHON27_LIBPATH' )
        nucleotide.component.function.check__env( 'PYTHON27_VERSION' )

        nucleotide.component.function.check__env( 'PYTHON35_INCLUDE' )
        nucleotide.component.function.check__env( 'PYTHON35_LIBPATH' )
        nucleotide.component.function.check__env( 'PYTHON35_VERSION' )
