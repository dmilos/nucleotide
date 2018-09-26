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
import subprocess

import nucleotide
import nucleotide.component
import nucleotide.component.function

def _windows_PDB_CPPFLAGS( P_data ):
    Ir_list = []

    if( True == ( 'configuration' in P_data ) ):
        if( 'debug' == P_data[ 'configuration' ].lower() ):
           Ir_list.append( '/ZI' )
        if( 'release' == P_data[ 'configuration' ].lower() ):
           Ir_list.append( '/Zi' )

    if( True == ( 'format' in P_data ) ):
        if( 'none' == P_data[ 'format' ] ):
           pass
        if( 'C7' == P_data[ 'format' ] ):
           Ir_list.append( '/Z7' )
        if( 'classic' == P_data[ 'format' ] ):
           Ir_list.append( '/Zi' )
        if( 'extended' == P_data[ 'format' ] ):
           Ir_list.append( '/ZI' )

    if( True == ( 'synchronous' in P_data ) ):
        if( 'true' == P_data[ 'synchronous' ] ):
           Ir_list.append( '/FS' )

    if( True == ( 'file-name-compile' in P_data ) ):
        Ir_list.append( '/Fd"' + P_data['file-name-compile'] + '"' )
    else:
        if( True == ( 'file-name' in P_data ) ):
            Ir_list.append( '/Fd"' + P_data['file-name'] + '"' )

    return Ir_list

def _windows_PDB_LINKFLAGS( P_data ):
    Ir_list = []
    if( True == ( 'configuration' in P_data ) ):
        if( 'debug' == P_data['configuration'].lower() ):
           Ir_list.append( '/DEBUG' )
        if( 'release' == P_data['configuration'].lower() ):
           Ir_list.append( '/DEBUG' )

    if( True == ( 'file-name-executable' in P_data )  ):
        Ir_list.append( '/PDB:"' + P_data['file-name-executable'] + '"' )
    else:
        if( True == ( 'file-name' in P_data ) ):
            Ir_list.append( '/PDB:"' + P_data['file-name'] + '"' )

    return Ir_list

atom_windows_PDB = {
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
        'CPPFLAGS'  : _windows_PDB_CPPFLAGS,
        'LINKFLAGS' : _windows_PDB_LINKFLAGS,
    },
    'name' : 'PDB',
    'class': [  'PDB', 'windows:PDB' ]
}


class PDB:
    def __init__(self):
        pass

    @staticmethod
    def extend(P_option):
        nucleotide.component.function.extend( P_option, 'windows:PDB',  atom_windows_PDB )

    @staticmethod
    def check(self):
        pass

