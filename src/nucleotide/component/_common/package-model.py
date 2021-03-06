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

def _common_package_CPPDEFINES( P_list ):
    Ir_list = []
    return Ir_list

def _common_package_CPPPATH( P_list ):
    Ir_list = []
    return Ir_list

def _common_package_LINKFLAGS( P_list ):
    Ir_list = []
    return Ir_list

def _common_package_LIBPATH( P_list ):
    Ir_list = []
    return Ir_list

def _common_package_LIBS( P_list ):
    Ir_list = []
    return Ir_list


atom__common_package = {
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
        'CPPDEFINES' : _common_package_CPPDEFINES,
        'CPPPATH'    : _common_package_CPPPATH,
        'LINKFLAGS'  : _common_package_LINKFLAGS,
        'LIBPATH'    : _common_package_LIBPATH,
        'LIBS'       : _common_package_LIBS,
    },

    'name' :'package',
    'class':  [ 'package' ]
}

class Package:

    def __init( self ) :
        pass

    @staticmethod
    def extend( P_option ) :
        nucleotide.component.function.extend( P_option, 'package',    atom__common_package )

    @staticmethod
    def check():
        pass