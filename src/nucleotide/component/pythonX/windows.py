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

import nucleotide.component.function
import nucleotide.component.pythonX.common


def _python_python27_msvc12_CPPPATH( P_list ):
    I_result = os.getenv('PYTHON27_MSVC12_INCLUDE')
    if( None == I_result ):
        return nucleotide.component.pythonX.common._python27_default_CPPPATH( P_list )
    return [ I_result ]

def _python_python27_msvc12_LIBPATH( P_list ):
    I_result = os.getenv('PYTHON27_MSVC12_LIBPATH')
    if( None == I_result ):
        return nucleotide.component.pythonX.common._python27_default_LIBPATH( P_list )
    return [ I_result ]

atom_python27_msvc_12 = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': '12'
    },
    'config' : {
            'CPPPATH': _python_python27_msvc12_CPPPATH,
            'LIBPATH': _python_python27_msvc12_LIBPATH,
            'LIBS'   : [ 'python27.lib' ]
    },
    'name' : 'python27:msvc12',
    'class':  [ 'python', 'python:default', 'python27:default', 'python27:msvc12' ]
}

def _python_python35_msvc12_CPPPATH( P_list ):
    I_result = os.getenv('PYTHON35_MSVC12_INCLUDE')
    if( None == I_result ):
        return _python35_default_CPPPATH( P_list )
    return [ I_result ]

def _python_python35_msvc12_LIBPATH( P_list ):
    I_result = os.getenv('PYTHON35_MSVC12_LIBPATH')
    if( None == I_result ):
        return _python35_default_LIBPATH( P_list )
    return [ I_result ]

atom_python35_msvc_12 = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': '12'
    },
    'config' : {
            'CPPPATH': _python_python35_msvc12_CPPPATH,
            'LIBPATH': _python_python35_msvc12_LIBPATH,
            'LIBS'   : [ 'python35.lib' ]
    },
    'name' : 'python35:msvc12',
    'class':  [ 'python', 'python:default', 'python35:default', 'python35:msvc12' ]
}


def _python_python27_mingw_CPPPATH( P_list ):
    I_result = os.getenv('PYTHON35_MINGW_INCLUDE')
    if( None == I_result ):
        return nucleotide.component.pythonX.common._python27_default_CPPPATH( P_list )
    return [ I_result ]

def _python_python27_mingw_LIBPATH( P_list ):
    I_result = os.getenv('PYTHON35_MINGW_LIBPATH')
    if( None == I_result ):
        return nucleotide.component.pythonX.common._python27_default_LIBPATH( P_list )
    return [ I_result ]

atom_python27_mingw = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor'  : 'mingw',
        'name'    : 'gcc',
        'version' : 'X'
    },
    'config' : {
            'CPPPATH': [ os.getenv('PYTHON27_MINGW_INCLUDE') ],
            'LIBPATH': [ os.getenv('PYTHON27_MINGW_LIBPATH') ],
            'LIBS'   : [ 'python27.a' ]
    },
    'name' : 'python27:mingw',
    'class':  [ 'python', 'python:default', 'python27:default', 'python27:mingw' ]
}


def _python_python35_mingw_CPPPATH( P_list ):
    I_result = os.getenv( 'PYTHON35_MINGW_INCLUDE' )
    if( None == I_result ):
        return _python35_default_CPPPATH( P_list )
    return [ I_result ]

def _python_python35_mingw_LIBPATH( P_list ):
    I_result = os.getenv( 'PYTHON35_MINGW_LIBPATH' )
    if( None == I_result ):
        return _python35_default_LIBPATH( P_list )
    return [ I_result ]

atom_python35_mingw = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor'  : 'mingw',
        'name'    : 'gcc',
        'version' : 'X'
    },
    'config' : {
            'CPPPATH': _python_python35_mingw_CPPPATH,
            'LIBPATH': _python_python35_mingw_LIBPATH,
            'LIBS'   : [ 'python35.a' ]
    },
    'name' : 'python35:mingw',
    'class':  [ 'python', 'python:default', 'python35:default', 'python35:mingw' ]
}


def init( P_option ) :

    nucleotide.component.function.extend( P_option, 'python27:msvc',    atom_python27_msvc_12 )
    nucleotide.component.function.extend( P_option, 'python35:msvc',    atom_python35_msvc_12 )
    nucleotide.component.function.extend( P_option, 'python27:mingw ',  atom_python27_mingw   )
    nucleotide.component.function.extend( P_option, 'python35:mingw',   atom_python35_mingw   )

def check():

    nucleotide.component.function.check__env( 'PYTHONPATH' )

    nucleotide.component.function.check__env( 'PYTHON27_MSVC12_INCLUDE' )
    nucleotide.component.function.check__env( 'PYTHON27_MSVC12_LIBPATH' )
    nucleotide.component.function.check__env( 'PYTHON27_MSVC12_VERSION' )

    nucleotide.component.function.check__env( 'PYTHON35_MSVC12_INCLUDE' )
    nucleotide.component.function.check__env( 'PYTHON35_MSVC12_LIBPATH' )
    nucleotide.component.function.check__env( 'PYTHON35_MSVC12_VERSION' )

    nucleotide.component.function.check__env( 'PYTHON27_MINGW_INCLUDE' )
    nucleotide.component.function.check__env( 'PYTHON27_MINGW_LIBPATH' )
    nucleotide.component.function.check__env( 'PYTHON27_MINGW_VERSION' )

    nucleotide.component.function.check__env( 'PYTHON35_MINGW_INCLUDE' )
    nucleotide.component.function.check__env( 'PYTHON35_MINGW_LIBPATH' )
    nucleotide.component.function.check__env( 'PYTHON35_MINGW_VERSION' )

#print 'End importing Module: -|' + __name__