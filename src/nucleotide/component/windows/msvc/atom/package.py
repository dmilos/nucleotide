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

import nucleotide.component.windows.msvc.atom.module.boost
import nucleotide.component.windows.msvc.atom.module.opencv
import nucleotide.component.windows.msvc.atom.module.zlib
import nucleotide.component.windows.msvc.atom.module.tbb
import nucleotide.component.windows.msvc.atom.module.protobuf
import nucleotide.component.windows.msvc.atom.module.python
import nucleotide.component.windows.msvc.atom.module.bzip2


Is_list={
    'boost': {
        'CPPDEFINES':nucleotide.component.windows.msvc.atom.module.boost._windows_msvc_atom_module_boost_CPPDEFINES,
        'CPPPATH'   :nucleotide.component.windows.msvc.atom.module.boost._windows_msvc_atom_module_boost_CPPPATH,
        'LINKFLAGS' :nucleotide.component.windows.msvc.atom.module.boost._windows_msvc_atom_module_boost_LINKFLAGS,
        'LIBPATH'   :nucleotide.component.windows.msvc.atom.module.boost._windows_msvc_atom_module_boost_LIBPATH,
        'LIBS'      :nucleotide.component.windows.msvc.atom.module.boost._windows_msvc_atom_module_boost_LIBS,
    },
    'opencv': {
        'CPPDEFINES':nucleotide.component.windows.msvc.atom.module.opencv._windows_msvc_atom_module_opencv_CPPDEFINES,
        'CPPPATH'   :nucleotide.component.windows.msvc.atom.module.opencv._windows_msvc_atom_module_opencv_CPPPATH,
        'LINKFLAGS' :nucleotide.component.windows.msvc.atom.module.opencv._windows_msvc_atom_module_opencv_LINKFLAGS,
        'LIBPATH'   :nucleotide.component.windows.msvc.atom.module.opencv._windows_msvc_atom_module_opencv_LIBPATH,
        'LIBS'      :nucleotide.component.windows.msvc.atom.module.opencv._windows_msvc_atom_module_opencv_LIBS,
    },
    'zlib': {
        'CPPDEFINES':nucleotide.component.windows.msvc.atom.module.zlib._windows_msvc_atom_module_zlib_CPPDEFINES,
        'CPPPATH'   :nucleotide.component.windows.msvc.atom.module.zlib._windows_msvc_atom_module_zlib_CPPPATH,
        'LINKFLAGS' :nucleotide.component.windows.msvc.atom.module.zlib._windows_msvc_atom_module_zlib_LINKFLAGS,
        'LIBPATH'   :nucleotide.component.windows.msvc.atom.module.zlib._windows_msvc_atom_module_zlib_LIBPATH,
        'LIBS'      :nucleotide.component.windows.msvc.atom.module.zlib._windows_msvc_atom_module_zlib_LIBS,
    },

    'tbb': {
        'CPPDEFINES':nucleotide.component.windows.msvc.atom.module.tbb._windows_msvc_atom_module_tbb_CPPDEFINES,
        'CPPPATH'   :nucleotide.component.windows.msvc.atom.module.tbb._windows_msvc_atom_module_tbb_CPPPATH,
        'LINKFLAGS' :nucleotide.component.windows.msvc.atom.module.tbb._windows_msvc_atom_module_tbb_LINKFLAGS,
        'LIBPATH'   :nucleotide.component.windows.msvc.atom.module.tbb._windows_msvc_atom_module_tbb_LIBPATH,
        'LIBS'      :nucleotide.component.windows.msvc.atom.module.tbb._windows_msvc_atom_module_tbb_LIBS,
    },

    'protobuf': {
        'CPPDEFINES':nucleotide.component.windows.msvc.atom.module.protobuf._windows_msvc_atom_module_protobuf_CPPDEFINES,
        'CPPPATH'   :nucleotide.component.windows.msvc.atom.module.protobuf._windows_msvc_atom_module_protobuf_CPPPATH,
        'LINKFLAGS' :nucleotide.component.windows.msvc.atom.module.protobuf._windows_msvc_atom_module_protobuf_LINKFLAGS,
        'LIBPATH'   :nucleotide.component.windows.msvc.atom.module.protobuf._windows_msvc_atom_module_protobuf_LIBPATH,
        'LIBS'      :nucleotide.component.windows.msvc.atom.module.protobuf._windows_msvc_atom_module_protobuf_LIBS,
    },

    'python': {
        'CPPDEFINES':nucleotide.component.windows.msvc.atom.module.python._windows_msvc_atom_module_python_CPPDEFINES,
        'CPPPATH'   :nucleotide.component.windows.msvc.atom.module.python._windows_msvc_atom_module_python_CPPPATH,
        'LINKFLAGS' :nucleotide.component.windows.msvc.atom.module.python._windows_msvc_atom_module_python_LINKFLAGS,
        'LIBPATH'   :nucleotide.component.windows.msvc.atom.module.python._windows_msvc_atom_module_python_LIBPATH,
        'LIBS'      :nucleotide.component.windows.msvc.atom.module.python._windows_msvc_atom_module_python_LIBS,
    },

    'bzip2': {
        'CPPDEFINES':nucleotide.component.windows.msvc.atom.module.bzip2._windows_msvc_atom_module_bzip2_CPPDEFINES,
        'CPPPATH'   :nucleotide.component.windows.msvc.atom.module.bzip2._windows_msvc_atom_module_bzip2_CPPPATH,
        'LINKFLAGS' :nucleotide.component.windows.msvc.atom.module.bzip2._windows_msvc_atom_module_bzip2_LINKFLAGS,
        'LIBPATH'   :nucleotide.component.windows.msvc.atom.module.bzip2._windows_msvc_atom_module_bzip2_LIBPATH,
        'LIBS'      :nucleotide.component.windows.msvc.atom.module.bzip2._windows_msvc_atom_module_bzip2_LIBS,
    }
}

def _windows_msvc_atom_package_CPPDEFINES( P_list ):

    #print P_list
    for key in P_list:
        if( key in Is_list ):
            return Is_list[key]['CPPDEFINES'](  P_list[key] )
        else:
            print( 'Pakage: \'' + key + '\' Not found.' )

    return []


def _windows_msvc_atom_package_CPPPATH( P_list ):

    #print P_list
    for key in P_list:
        if( key in Is_list ):
            return Is_list[key]['CPPPATH'](  P_list[key] )
        else:
            print( 'Pakage: \'' + key + '\' Not found.' )

    return []

def _windows_msvc_atom_package_LINKFLAGS( P_list ):

    #print P_list
    for key in P_list:
        if( key in Is_list ):
            return Is_list[key]['LINKFLAGS'](  P_list[key] )
        else:
            print( 'Pakage: \'' + key + '\' Not found.' )

    return []

def _windows_msvc_atom_package_LIBPATH( P_list ):

    #print P_list
    for key in P_list:
        if( key in Is_list ):
            return Is_list[key]['LIBPATH'](  P_list[key] )
        else:
            print( 'Pakage: \'' + key + '\' Not found.' )

    return []

def _windows_msvc_atom_package_LIBS( P_list ):

    #print P_list
    for key in P_list:
        if( key in Is_list ):
            return Is_list[key]['LIBS'](  P_list[key] )
        else:
            print( 'Pakage: \'' + key + '\' Not found.' )

    return []


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
        'CPPDEFINES' : _windows_msvc_atom_package_CPPDEFINES,
        'CPPPATH'    : _windows_msvc_atom_package_CPPPATH,
        'LINKFLAGS'  : _windows_msvc_atom_package_LINKFLAGS,
        'LIBPATH'    : _windows_msvc_atom_package_LIBPATH,
        'LIBS'       : _windows_msvc_atom_package_LIBS,
    },

    'name' :'package',
    'class':  [ 'package', 'windows:package' ]
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