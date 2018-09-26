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

def _atom_linux_optimization_CPPFLAGS( P_data ):
    Ir_list = []

    if( False == ( 'configuration' in P_data ) ):
        return Ir_list

    if( 'debug' == P_data[ 'configuration' ].lower() ):
        Ir_list += [ '-Og'  ]

    if( 'release' == P_data[ 'configuration' ].lower() ):
        Ir_list += [ '-O2'  ]

    return Ir_list


def _atom_linux_optimization_CPPDEFINES( P_data ):
    Ir_list = []
    return Ir_list

def _atom_linux_optimization_LINKFLAGS( P_data ):
    Ir_list = []
    return Ir_list

def _atom_linux_optimization_LIBS( P_data ):
    Ir_list = []
    return Ir_list


atom_linux_optimization = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'name' :'optimization',
    'config' : {
        'CPPFLAGS'    : _atom_linux_optimization_CPPFLAGS,
        'CPPDEFINES'  : _atom_linux_optimization_CPPDEFINES,
        'LINKFLAGS'   : _atom_linux_optimization_LINKFLAGS,
        'LIBS'        : _atom_linux_optimization_LIBS
    },
    'class': [ 'optimization', 'compiler:optimization', 'linux:compiler:optimization',
               'optimisation', 'compiler:optimisation', 'linux:compiler:optimisation'
    ]
}

class Optimization:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
         nucleotide.component.function.extend( P_option, 'A:linux:optimization',               atom_linux_optimization)
         atom_linux_optimization['platform']['host']='X'
         nucleotide.component.function.extend( P_option, 'x:linux:optimization',               atom_linux_optimization)
         atom_linux_optimization['platform']['guest']='X'
         nucleotide.component.function.extend( P_option, 'y:linux:optimization',               atom_linux_optimization)

         nucleotide.component.function.extend( P_option, 'A:linux:optimisation',               atom_linux_optimization)
         atom_linux_optimization['platform']['host']='X'
         nucleotide.component.function.extend( P_option, 'x:linux:optimisation',               atom_linux_optimization)
         atom_linux_optimization['platform']['guest']='X'
         nucleotide.component.function.extend( P_option, 'y:linux:optimisation',               atom_linux_optimization)

    @staticmethod
    def check():
        pass
