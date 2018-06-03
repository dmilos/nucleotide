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

def _linux_gcc_version_GCC_CC_VERSION( P_data ):
    if( False == ( 'gcc' in P_data ) ):
        return None
    return 'gcc-' + P_data[ 'gcc' ][0]

def _linux_gcc_version_GCC_CXX_VERSION( P_data ):
    if( False == ( 'gcc' in P_data ) ):
        return None
    return 'g++-' + P_data[ 'gcc' ][0]

def _linux_gcc_version_GCC_LINK_VERSION( P_data ):
    if( False == ( 'gcc' in P_data ) ):
        return None
    return 'g++-' + P_data[ 'gcc' ][0]


atom_linux_CCVERSION = {
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
        'CC'    : _linux_gcc_version_GCC_CC_VERSION,
        'CXX'   : _linux_gcc_version_GCC_CXX_VERSION,
        'LINK'  : _linux_gcc_version_GCC_LINK_VERSION
    },
    'name' :'compiler:version',
    'class':  [ 'compiler:version', 'linux:compiler:version' ]
}

class Version:
    def __init__(self):
        pass

    @staticmethod
    def extend(P_option):
        nucleotide.component.function.extend( P_option, 'linux:compiler:version', atom_linux_CCVERSION )

    @staticmethod
    def check(self):
        pass
