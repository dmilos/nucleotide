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
import platform

import function
import nucleotide.direction
import nucleotide.config
import nucleotide.klass

def _boost_blank_CPPPATH( P_list ):
    return [ os.getenv('BOOST_INCLUDE') ]

def _boost_blank_LIBPATH( P_list ):
    return [ os.getenv('BOOST_LIBPATH') ]

atom_boost_blank = {
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
            'CPPPATH' : _boost_blank_CPPPATH,
            'LIBPATH' : _boost_blank_LIBPATH
    },
    'name' : 'boost:blank',
    'class':  [ 'boost', 'boost:blank' ]
}

def _boost_msvc12_CPPPATH( P_list ):
    I_arc = '32';
    #TODO

    I_result = os.getenv('BOOST_MSVC12_INCLUDE')
    if( None == I_result ):
        return _boost_blank_CPPPATH( P_list )
    return [ I_result ]

def _boost_msvc12_LIBPATH( P_list ):
    I_arc = '32';
    I_result = os.getenv('BOOST_MSVC12_LIBPATH')
    if( None == I_result ):
        return _boost_blank_LIBPATH( P_list )
    return [ I_result ]

atom_boost_msvc_12 = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor' : 'Microsoft',
        'name'   : 'msvc',
        'version': '12'
    },
    'config' : {
            'CPPPATH' : _boost_msvc12_CPPPATH,
            'LIBPATH' : _boost_msvc12_LIBPATH
    },
    'name' :'boost:msvc12',
    'class': [ 'boost', 'boost:blank', 'boost:msvc12'  ]
}

def _boost_mingw_CPPPATH( P_list ):
    I_result = os.getenv('BOOST_MINGW_INCLUDE')
    if( None == I_result ):
        return _boost_blank_CPPPATH( P_list )
    return [ I_result ]

def _boost_mingw_LIBPATH( P_list ):
    I_result = os.getenv('BOOST_MINGW_LIBPATH')
    if( None == I_result ):
        return _boost_blank_LIBPATH( P_list )
    return [ I_result ]

atom_boost_mingw = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor' : 'mingw',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
            'CPPPATH' : _boost_mingw_CPPPATH,
            'LIBPATH' : _boost_mingw_LIBPATH
    },
    'name' :'boost:mingw',
    'class': [ 'boost', 'boost:blank', 'boost:mingw'  ]
}

atom_boost_python_static = {
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
            'CPPDEFINES' : [ 'BOOST_PYTHON_STATIC_LIB' ],
    },
    'name' :'boost:python:static',
    'class':  [ 'boost:python:static' ]
}

atom_boost_linux_gcc_blank= {
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
        'LINKFLAGS' : [ '-lboost_system', '-static-libstdc++', '-lpthread', '-lboost_system' ],
        'CPPDEFINES' : [ 'BOOST_SYSTEM_NO_DEPRECATED' ],
    },
    'name' :'boost:linux:blank',
    'class':  [ 'boost', 'boost:blank', 'boost:linux:', 'boost:linux:blank' ]
}


def init( P_option ) :
    function.extend( P_option, 'boost:blank',           atom_boost_blank            )
    function.extend( P_option, 'boost:msvc12',          atom_boost_msvc_12          )
    function.extend( P_option, 'boost:mingw',           atom_boost_mingw            )
    function.extend( P_option, 'boost:python:static',   atom_boost_python_static    )
    function.extend( P_option, 'boost:linux:gcc',       atom_boost_linux_gcc_blank  )


def check():
    function.check__env( 'BOOST_INCLUDE' )
    function.check__env( 'BOOST_LIBPATH' )
    function.check__env( 'BOOST_VERSION' )

    if( 'Windows' == platform.system() ):
        function.check__env( 'BOOST_MSVC12_INCLUDE' )
        function.check__env( 'BOOST_MSVC12_LIBPATH' )
        function.check__env( 'BOOST_MSVC12_VERSION' )
        function.check__env( 'BOOST_MSVC12_64_INCLUDE' )
        function.check__env( 'BOOST_MSVC12_64_LIBPATH' )
        function.check__env( 'BOOST_MSVC12_64_VERSION' )

    if( 'Windows' == platform.system() ):
        function.check__env( 'BOOST_MINGW_INCLUDE' )
        function.check__env( 'BOOST_MINGW_LIBPATH' )
        function.check__env( 'BOOST_MINGW_VERSION' )
        function.check__env( 'BOOST158_MINGW_INCLUDE' )
        function.check__env( 'BOOST158_MINGW_LIBPATH' )
        function.check__env( 'BOOST158_MINGW_VERSION' )
