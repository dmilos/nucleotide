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

def _windows_dialect_CPPFLAGS( P_data ):
    Ir_list = []

    if( True == ( 'dialect' in P_data ) ):
        if( 'plain_c' == P_data['dialect'] ):
            Ir_list += ['/TC' ]
        if( 'plain_cpp' == P_data['dialect'] ):
            Ir_list += ['/TP' ]

    if( True == ( 'standard' in P_data ) ):
        Ir_list += ['/std:' + P_data['standard'] ]

    return Ir_list

atom_windows_dialect= {
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
        'CPPFLAGS'   : _windows_dialect_CPPFLAGS,
    },
    'name' :'windows:source:c++',
    'class':  [ 'source:c++', 'source:c',  'source:c++11' ]
}

class Dialect:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
         nucleotide.component.function.extend( P_option, 'windows:c++:dialect',             atom_windows_dialect)

    @staticmethod
    def check():
        pass

