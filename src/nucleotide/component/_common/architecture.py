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

def __common_architecture_TARGET_ARCH( P_data ):
    if( False == ( 'name' in P_data ) ):
        return ''
    return P_data[ 'name' ]

atom_common_architecture = {
    'platform' : {
        'host'  : 'X',
        'guest' : 'X'
    },
    'cc' : {
        'vendor': 'X',
        'name': 'X',
        'version': 'X'
    },
    'config' : {
        'TARGET_ARCH' : __common_architecture_TARGET_ARCH
    },
    'name' :'architecture',
    'class':  [ 'architecture', 'compiler:architecture' ]
}

class Architecture:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ) :
        nucleotide.component.function.extend( P_option, 'compiler:architecture',        atom_common_architecture )

    @staticmethod
    def check():
        pass

