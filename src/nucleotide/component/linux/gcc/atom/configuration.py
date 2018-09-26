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

def atom_linux_configuration_CPPFLAGS( P_data ):
    Ir_list = []

    if( False == ( 'name' in P_data ) ):
        return Ir_list

    if( 'debug' == P_data[ 'name' ].lower() ):
        Ir_list += [ '-g'  ]

    if( 'release'== P_data[ 'name' ].lower() ):
        pass

    return Ir_list

def atom_linux_configuration_CPPDEFINES( P_data ):
    Ir_list = []

    if( False == ( 'name' in P_data ) ):
        return Ir_list

    if( 'debug' == P_data[ 'name' ].lower() ):
        Ir_list += [ '_DEBUG'  ]

    if( 'release' == P_data[ 'name' ].lower() ):
        Ir_list += [ 'NDEBUG'  ]

    return Ir_list

def atom_linux_configuration_LINKFLAGS( P_data ):
    Ir_list = []

    if( False == ( 'name' in P_data ) ):
        return Ir_list

    if( 'debug' == P_data[ 'name' ].lower() ):
        pass #Ir_list += [ 'TODO'  ]

    if( 'release'== P_data[ 'name' ].lower() ):
        pass

    return Ir_list


atom_linux_configuration = {
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
        'CPPFLAGS'   : atom_linux_configuration_CPPFLAGS,
        'CPPDEFINES' : atom_linux_configuration_CPPDEFINES,
        'LINKFLAGS'  : atom_linux_configuration_LINKFLAGS
    },
    'name' :'compiler:configuration',
    'class': [ 'compiler:configuration', 'linux:compiler:configuration' ]
}

class Configuration:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
         nucleotide.component.function.extend( P_option, 'A:linux:compiler:configuration',               atom_linux_configuration )
         atom_linux_configuration['platform']['host']='X'
         nucleotide.component.function.extend( P_option, 'x:linux:compiler:configuration',               atom_linux_configuration )
         atom_linux_configuration['platform']['guest']='X'
         nucleotide.component.function.extend( P_option, 'y:linux:compiler:configuration',               atom_linux_configuration )

    @staticmethod
    def check():
        pass
