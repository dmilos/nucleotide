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

# type = [ 'console', 'UI' ]


def _windows_RebuildLazy_CPPFLAGS( P_data ):

    if( False == ( 'enable' in P_data ) ):
        return ['/Gm-']

    if( 'true' == P_data[ 'enable' ] ):
        return ['/Gm' ]

    if( 'false' == P_data[ 'enable' ] ):
        return [ '/Gm-' ]
        
    # TODO /Zi or /ZI


atom_windows_msvc_RebuildLazy = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },

    'config' : {
        'CPPFLAGS'    : _windows_RebuildLazy_CPPFLAGS,
    },
    'name' :'windows:compiler:rebuild:lazy',
    'class':  [ 'compiler:rebuild:lazy', 'windows:compiler:rebuild:lazy' ]
}

class RebuildLazy:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
        nucleotide.component.function.extend( P_option, 'windows:compiler:rebuild:lazy',         atom_windows_msvc_RebuildLazy )

    @staticmethod
    def check():
        pass
