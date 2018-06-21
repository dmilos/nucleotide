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


def _windows_alignment_CPPFLAGS( P_data ):

    if( False == ( 'size' in P_data ) ):
        return []
    return  ['/Zp' + P_data['size'] ]

atom_windows_msvc_alignment = {
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
        'CPPFLAGS'    : _windows_alignment_CPPFLAGS,
    },
    'name' :'compiler:memory:alignment',
    'class':  [ 'compiler:alignment', 'compiler:memory:alignment', 'windows:memory:alignment', 'windows:compiler:memory:alignment' ]
}

class Alignment:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
        nucleotide.component.function.extend( P_option, 'windows:memory:alignment',         atom_windows_msvc_alignment )

    @staticmethod
    def check():
        pass
