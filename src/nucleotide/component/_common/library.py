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

def _common_library_LIBPATH( P_list ):

    Ir_list = []

    for item in P_list:
        if( False == ( 'path' in P_list[item] ) ):
            continue
        Ir_list += [ P_list[item]['path'] ]

    #print( 'Library::_common_library_LIBPATH::Ir_list =  ' + str( Ir_list ) )

    return Ir_list

def _common_library_LIBS( P_list ):

    Ir_list = []

    for item in P_list:
        if( False == ( 'list' in P_list[item] ) ):
            continue
        Ir_list += P_list[item]['list']

    #print( 'Library::_common_library_LIBS::Ir_list =  ' + str( Ir_list ) )

    return Ir_list


atom__common_library = {
    'platform' : {
        'host'  : 'X',
        'guest' : 'X'
    },
    'cc' : {
        'vendor' : 'X',
        'name'   : 'X',
        'version': 'X'
    },
    'config' : {
        'LIBPATH' : _common_library_LIBPATH,
        'LIBS'    : _common_library_LIBS,
    },
    'name' :'library',
    'class':  [ 'library' ]
}

class Library:

    def __init( self ) :
        pass

    @staticmethod
    def extend( P_option ) :
        nucleotide.component.function.extend( P_option, 'library',    atom__common_library )

    @staticmethod
    def check():
        pass