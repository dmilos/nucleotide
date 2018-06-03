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


import nucleotide
import nucleotide.component
import nucleotide.component.function


def _linux_Macro_CPPFLAGS( P_data ):
    Ir_list = []

    if( False== ( 'name' in P_data ) ):
        return Ir_list

    s = '-D' + P_data[ 'name' ]

    if( True == ( 'parameter' in P_data ) ):
        s += '('
        for p in P_data['parameter']:
            s += p
            s += ','
        s = s = s[:-1]
        s += ')'

    if( True == ( 'body' in P_data ) ):
        s += '=' + P_data[ 'body' ]

    Ir_list += [ s ]
    return Ir_list

atom_linux_Macro = {
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
        'CPPFLAGS'  : _linux_Macro_CPPFLAGS,
    },
    'name' : 'macro',
    'class': [  'macro', 'linux:macro' ]
}

# { 'name' : 'MY_MAX', 'parameter':['a', 'b'], 'body': '( (a)<(b) ? (b) : (a) )' }
class Macro:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
        nucleotide.component.function.extend( P_option, 'A:linux:compiler:macro',  atom_linux_Macro )
        atom_linux_Macro['platform']['host'] = 'X';
        nucleotide.component.function.extend( P_option, 'x:linux:compiler:macro',  atom_linux_Macro )
        atom_linux_Macro['platform']['guest'] = 'X';
        nucleotide.component.function.extend( P_option, 'y:linux:compiler:macro',  atom_linux_Macro )

    @staticmethod
    def check():
        pass

