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
import traceback

import nucleotide
import nucleotide.component
import nucleotide.component.function
import nucleotide.component.windows.msvc.atom.module.generator


def _windows_msvc_atom_module_python_CPPDEFINES( P_list ):
    #print( "_windows_msvc_atom_module_python_CPPDEFINES" )
    Ir_result = [];
    return Ir_result

def _windows_msvc_atom_module_python_CPPPATH( P_list ):
    #print( "_windows_msvc_atom_module_python_CPPPATH" )

    prefix  = { "PYTHONROOT", "PYTHON_ROOT", "PYTHON" }
    Ir_result = nucleotide.component.windows.msvc.atom.module.generator.find_ENVIRONMENT_CPPPATH( prefix, P_list )

    return Ir_result

def _windows_msvc_atom_module_python_LINKFLAGS( P_list ):
    Ir_result = [];
    #print( '_windows_msvc_atom_module_python_LINKFLAGS' )
    return Ir_result

def _windows_msvc_atom_module_python_LIBPATH( P_list ):
    #print( "_windows_msvc_atom_module_python_LIBPATH" )

    prefix  = { "PYTHONROOT", "PYTHON_ROOT", "PYTHON" }
    Ir_result = nucleotide.component.windows.msvc.atom.module.generator.find_ENVIRONMENT_LIBPATH( prefix, P_list )

    return Ir_result

def _windows_msvc_atom_module_python_LIBS( P_list ):
    #print( "_windows_msvc_atom_module_python_LIBS" )
    Ir_result = [];
    return Ir_result


atom__common_package = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor' : 'Microsoft',
        'name'   : 'msvc',
        'version': 'X'
    },
    'config' : {
        'CPPDEFINES' : _windows_msvc_atom_module_python_CPPDEFINES,
        'CPPPATH'    : _windows_msvc_atom_module_python_CPPPATH,
        'LINKFLAGS'  : _windows_msvc_atom_module_python_LINKFLAGS,
        'LIBPATH'    : _windows_msvc_atom_module_python_LIBPATH,
        'LIBS'       : _windows_msvc_atom_module_python_LIBS,
    },

    'name' :'package',
    'class':  [ 'package::python', 'windows:package:python' ]
}

 