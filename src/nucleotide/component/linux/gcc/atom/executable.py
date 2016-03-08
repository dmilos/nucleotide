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

def _linux_executable_CPPFLAGS( P_data ):
    Ir_list= [] # TODO
    return Ir_list

def _linux_executable_CPPDEFINES( P_data ):
    Ir_list= []# TODO
    return Ir_list

def _linux_executable_LIBS( P_data ):
    Ir_list= []# TODO
    return Ir_list

def _linux_executable_LINKFLAGS( P_data ):
    Ir_list= []# TODO
    return Ir_list

atom_linux_gcc_executable = {
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
        'CPPFLAGS'    : _linux_executable_CPPFLAGS,
        'CPPDEFINES'  : _linux_executable_CPPDEFINES,
        'LIBS'        : _linux_executable_LIBS,
        'LINKFLAGS'   : _linux_executable_LINKFLAGS
    },
    'name' :'linux:executable',
    'class':  [ 'executable', 'linux:executable' ]
}

class Executable:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
        nucleotide.component.function.extend( P_option, 'linux:executable',         atom_linux_gcc_executable)

    @staticmethod
    def check():
        pass
