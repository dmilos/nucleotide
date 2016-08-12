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

import nucleotide
import nucleotide.component
import nucleotide.component.function

import nucleotide.translator
import nucleotide.config
import nucleotide.klass

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


class Boost:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ) :
            nucleotide.component.function.extend( P_option, 'boost:mingw',           atom_boost_mingw            )

    @staticmethod
    def check():

        function.check__env( 'BOOST_MINGW_INCLUDE' )
        function.check__env( 'BOOST_MINGW_LIBPATH' )
        function.check__env( 'BOOST_MINGW_VERSION' )
