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

# type = [ 'console', 'UI' ]


def _windows_executable_CPPFLAGS( P_data ):
    Ir_list= [] # TODO
    return Ir_list

def _windows_executable_CPPDEFINES( P_data ):
    Ir_list= []

    if( False == ( 'type' in P_data ) ):
        return Ir_list

    if( 'console' == P_data['type'] ):
        Ir_list += ['_CONSOLE' ]

    if( 'UI' == P_data['type'] ):
        Ir_list += [ ]# TODO

    return Ir_list

def _windows_executable_LIBS( P_data ):
    Ir_list= []# TODO
    return Ir_list

def _windows_executable_LINKFLAGS( P_data ):
    Ir_list= []

    if( False == ( 'type' in P_data ) ):
        return Ir_list

    if( 'console' == P_data['type'] ):
        Ir_list += ['/SUBSYSTEM:CONSOLE' ]

    if( 'UI' == P_data['type'] ):
        Ir_list += [ '/SUBSYSTEM:WINDOWS' ]

    return Ir_list

atom_windows_msvc_executable = {
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
        'CPPFLAGS'    : _windows_executable_CPPFLAGS,
        'CPPDEFINES'  : _windows_executable_CPPDEFINES,
        'LIBS'        : _windows_executable_LIBS,
        'LINKFLAGS'   : _windows_executable_LINKFLAGS
    },
    'name' :'windows:executable',
    'class':  [ 'executable', 'windows:executable' ]
}

class Executable:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
        nucleotide.component.function.extend( P_option, 'windows:executable',         atom_windows_msvc_executable )

    @staticmethod
    def check():
        pass
