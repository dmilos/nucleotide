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


def _linux_gcc_alignment_CPPFLAGS( P_data ):

    if( False == ( 'size' in P_data ) ):
        return []
    return  ['-fpack-struct=' + P_data['size'] ]

atom_linux_gcc_alignment = {
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
        'CPPFLAGS'    : _linux_gcc_alignment_CPPFLAGS,
    },
    'name' :'compiler:memory:alignment',
    'class':  [ 'compiler:memory:alignment', 'linux:memory:alignment', 'linux:compiler:memory:alignment' ]
}

class Alignment:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
        nucleotide.component.function.extend( P_option, 'A:linux:memory:alignment',             atom_linux_gcc_alignment)
        atom_linux_gcc_alignment['platform']['host']  = 'X';
        nucleotide.component.function.extend( P_option, 'x:linux:memory:alignment',             atom_linux_gcc_alignment)
        atom_linux_gcc_alignment['platform']['guest'] = 'X';
        nucleotide.component.function.extend( P_option, 'y:linux:memory:alignment',             atom_linux_gcc_alignment)

    @staticmethod
    def check():
        pass
