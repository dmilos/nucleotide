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

def _linux_Dialect_CPPFLAGS( P_data ):
    Ir_list = []

    if( True == ( 'dialect' in P_data ) ):
        if( 'plain_c' == P_data['dialect'] ):
            pass
        if( 'plain_cpp' == P_data['dialect'] ):
            pass

    if( True == ( 'standard' in P_data ) ):
        Ir_list += [ '-std=' + P_data['standard'] ]

    return Ir_list

atom_linux_gcc_dialect = {
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
        'CPPFLAGS'   : _linux_Dialect_CPPFLAGS
    },
    'name' :'source:c++:dialect',
    'class':  [ 'source:c++', 'source:c++:dialect' ,'linux:source:c++:dialect'  ]
}

class Dialect:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
        nucleotide.component.function.extend( P_option, 'A:linux:source:c++:dialect',   atom_linux_gcc_dialect )
        atom_linux_gcc_dialect['platform']['host'] = 'X'; 
        nucleotide.component.function.extend( P_option, 'x:linux:source:c++:dialect',   atom_linux_gcc_dialect )
        atom_linux_gcc_dialect['platform']['guest'] = 'X'; 
        nucleotide.component.function.extend( P_option, 'y:linux:source:c++:dialect',   atom_linux_gcc_dialect )

    @staticmethod
    def check():
        pass

