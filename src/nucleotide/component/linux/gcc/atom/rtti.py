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

def _linux_RTTI_CPPFLAGS( P_data ):
    if( False == ( 'enable' in P_data ) ):
        return [ '' ]

    if( 'true' == P_data[ 'enable' ] ):
        return [ '' ]

    if( 'false' == P_data[ 'enable' ] ):
        return [ '-fno-rtti' ]

    return [ '' ]

atom_linux_RTTI = {
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
        'CPPFLAGS'   : _linux_RTTI_CPPFLAGS
    },
    'name' :'RTTI',
    'class':  [ 'RTTI', 'linux:RTTI' ]
}

class RTTI:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
         nucleotide.component.function.extend( P_option, 'A:linux:RTTI',                atom_linux_RTTI)
         atom_linux_RTTI['platform']['host'] = 'X';
         nucleotide.component.function.extend( P_option, 'x:linux:RTTI',                atom_linux_RTTI)
         atom_linux_RTTI['platform']['guest'] = 'X';
         nucleotide.component.function.extend( P_option, 'y:linux:RTTI',                atom_linux_RTTI)

    @staticmethod
    def check():
        pass
