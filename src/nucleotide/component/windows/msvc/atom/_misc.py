﻿#!/usr/bin/env python2

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

def _windows_configuration_CPPDEFINES( P_data ):
    Ir_list = []

    if( False == P_data.has_key( 'name') ):
        return Ir_list

    if( 'debug '== P_data[ 'name' ] ):
        Ir_list += [ '_DEBUG' ]

    if( 'release'== P_data[ 'name' ] ):
        Ir_list += [ 'NDEBUG' ]
    return Ir_list

def _windows_configuration_CPPFLAGS( P_data ):
    Ir_list = []

    if( False == P_data.has_key( 'name') ):
        return Ir_list

    if( 'debug '== P_data[ 'name' ] ):
        Ir_list += [ '/RTC1'  ]

    if( 'release'== P_data[ 'name' ] ):
        pass
    return Ir_list

def _windows_configuration_LINKFLAGS( P_data ):
    Ir_data = []

    if( False == P_data.has_key( 'name') ):
        return Ir_data

    if( 'debug '== P_data[ 'name' ] ):
        Ir_list += [ '/DEBUG' ]

    if( 'release'== P_data[ 'name' ] ):
        pass

    return Ir_data

# debug   'CPPDEFINES' : [ '_DEBUG' ],
# debug   'CPPFLAGS'   : [ '/RTC1'  ],
# debug   'LINKFLAGS'  : [ '/DEBUG' ]

# release:  'CPPDEFINES'   : [ 'NDEBUG' ],

atom_windows_configuration = {
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
        'CPPDEFINES' : _windows_configuration_CPPDEFINES,
        'CPPFLAGS'   : _windows_configuration_CPPFLAGS,
        'LINKFLAGS'  : _windows_configuration_LINKFLAGS
    },
    'name' :'compiler:configuration',
    'class': [ 'compiler:configuration', 'windows:compiler:configuration' ]
}

atom_windows_shared_library = {
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
        'CPPDEFINES'  : ['_USRDLL', '_WINDLL' ],
        'LINKFLAGS'   : [ '/DLL', '/SUBSYSTEM:WINDOWS' ]
    },
    'name' :'dll',
    'class':  [ 'shared:library' ]
}

atom_windows_shared_object = {
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
        'CPPDEFINES'  : ['_LIB' ],
    },
    'name' :'lib',
    'class': [  'shared:object' ]
}


def _windows_optimisation_CPPFLAGS( P_data ):
    Ir_list = []
    if( True == P_data.has_key( 'configuration' ) ):
        if( 'debug' == P_data['configuration'] ):
           Ir_list.append( '/Od' )
        if( 'release' == P_data['configuration'] ):
           Ir_list.append( '/O2' )

    return Ir_list

atom_windows_optimisation = {
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
        'CPPFLAGS'  : _windows_optimisation_CPPFLAGS,
    },
    'name' : 'release-optimisation',
    'class': [ 'compiler:optimisation', 'windows:compiler:configuration' ]
}


def init( P_option ) :

    nucleotide.component.function.extend( P_option, 'windows:compiler:configuration',    atom_windows_configuration )
    nucleotide.component.function.extend( P_option, 'windows:compiler:optimisation',     atom_windows_optimisation )

    nucleotide.component.function.extend( P_option, 'windows:shared:library', atom_windows_shared_library)
    nucleotide.component.function.extend( P_option, 'windows:shared:object',  atom_windows_shared_object)

   #nucleotide.component.function.extend( P_option, 'windows:linker:warning',      atom_windows_linker_warning )
   #nucleotide.component.function.extend( P_option, 'windows:linker:optimisation', atom_windows_linker_warning )

