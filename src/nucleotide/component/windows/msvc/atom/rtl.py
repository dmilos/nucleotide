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

def _windows_RTL_CPPFLAGS( P_data ):
    I_flag = 'M'

    if( 'dynamic' == P_data['type'].lower() ):
       I_flag += 'D'
    if( 'static' == P_data['type'].lower() ):
       I_flag += 'T'

    if( True == ( 'configuration' in P_data ) ):
        if( 'debug' == P_data['configuration'].lower() ):
           I_flag += 'd'
        if( 'release' == P_data['configuration'].lower() ):
           pass

    return [ '/' + I_flag ]

atom_windows_RTL= {
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
        'CPPFLAGS'  : _windows_RTL_CPPFLAGS
    },
    'name' :'RTL',
    'class':  [ 'RTL', 'windows:RTL' ]
}

class RTL:
    def __init__(self):
        pass

    @staticmethod
    def extend(P_option):
        nucleotide.component.function.extend( P_option, 'windows:RTL',  atom_windows_RTL )

    @staticmethod
    def check(self):
        pass
