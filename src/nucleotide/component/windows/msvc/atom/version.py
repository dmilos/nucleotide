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

def _windows_version_MSVC_VERSION( P_data ):
    if( False == ( 'msvc' in P_data ) ):
        return None
    print( "        ||" + str( P_data ) + "||" )
    return P_data[ 'msvc' ][0]

atom_windows_CCVERSION = {
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
        'MSVC_VERSION'   : _windows_version_MSVC_VERSION
    },
    'name' :'compiler:version',
    'class':  [ 'compiler:version', 'windows:compiler:version' ]
}

class Version:
    def __init__(self):
        pass

    @staticmethod
    def extend(P_option):
        nucleotide.component.function.extend( P_option, 'windows:compiler:version', atom_windows_CCVERSION )

    @staticmethod
    def check(self):
        pass
