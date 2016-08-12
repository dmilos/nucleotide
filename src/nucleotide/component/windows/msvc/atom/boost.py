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
import nucleotide.component.windows._common.boost


def _boost_msvc12_CPPPATH( P_list ):
    I_arc = '32';
    #TODO

    I_result = os.getenv('BOOST_MSVC12_INCLUDE')
    if( None == I_result ):
        return nucleotide.component.windows._common.boost._boost_blank_CPPPATH( P_list )
    return [ I_result ]

def _boost_msvc12_LIBPATH( P_list ):
    I_arc = '32';
    I_result = os.getenv('BOOST_MSVC12_LIBPATH')
    if( None == I_result ):
        return nucleotide.component.windows._common.boost._boost_blank_LIBPATH( P_list )
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



class Boost:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ) :
        nucleotide.component.function.extend( P_option, 'boost:msvc12',          atom_boost_msvc_12          )

    def check():

        nucleotide.component.function.check__env( 'BOOST_MSVC12_INCLUDE' )
        nucleotide.component.function.check__env( 'BOOST_MSVC12_LIBPATH' )
        nucleotide.component.function.check__env( 'BOOST_MSVC12_VERSION' )
        nucleotide.component.function.check__env( 'BOOST_MSVC12_64_INCLUDE' )
        nucleotide.component.function.check__env( 'BOOST_MSVC12_64_LIBPATH' )
        nucleotide.component.function.check__env( 'BOOST_MSVC12_64_VERSION' )
