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


def _windows_msvc_atom_package_CPPDEFINES( P_list ):

    if( True == ( 'boost' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.boost._windows_msvc_atom_module_boost_CPPDEFINES( P_list['boost'] )

    if( True == ( 'opencv' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.opencv._windows_msvc_atom_module_opencv_CPPDEFINES( P_list['opencv'] )

    if( True == ( 'zlib' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.zlib._windows_msvc_atom_module_zlib_CPPDEFINES( P_list['zlib'] )

    if( True == ( 'tbb' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.tbb._windows_msvc_atom_module_tbb_CPPDEFINES( P_list['tbb'] )

    if( True == ( 'protobuf' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.protobuf._windows_msvc_atom_module_protobuf_CPPDEFINES( P_list['protobuf'] )

    return []

def _windows_msvc_atom_package_CPPPATH( P_list ):

    if( True == ( 'boost' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.boost._windows_msvc_atom_module_boost_CPPPATH( P_list['boost'] )

    if( True == ( 'opencv' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.opencv._windows_msvc_atom_module_opencv_CPPPATH( P_list['opencv'] )

    if( True == ( 'zlib' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.zlib._windows_msvc_atom_module_zlib_CPPPATH( P_list['zlib'] )

    if( True == ( 'tbb' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.tbb._windows_msvc_atom_module_tbb_CPPPATH( P_list['tbb'] )

    if( True == ( 'protobuf' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.protobuf._windows_msvc_atom_module_protobuf_CPPPATH( P_list['protobuf'] )

    return []

def _windows_msvc_atom_package_LINKFLAGS( P_list ):

    if( True == ( 'boost' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.boost._windows_msvc_atom_module_boost_LINKFLAGS( P_list['boost'] )

    if( True == ( 'opencv' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.opencv._windows_msvc_atom_module_opencv_LINKFLAGS( P_list['opencv'] )

    if( True == ( 'zlib' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.zlib._windows_msvc_atom_module_zlib_LINKFLAGS( P_list['zlib'] )

    if( True == ( 'tbb' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.tbb._windows_msvc_atom_module_tbb_LINKFLAGS( P_list['tbb'] )

    if( True == ( 'protobuf' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.protobuf._windows_msvc_atom_module_protobuf_LINKFLAGS( P_list['protobuf'] )

    return []

def _windows_msvc_atom_package_LIBPATH( P_list ):

    if( True == ( 'boost' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.boost._windows_msvc_atom_module_boost_LIBPATH( P_list['boost'] )

    if( True == ( 'opencv' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.opencv._windows_msvc_atom_module_opencv_LIBPATH( P_list['opencv'] )

    if( True == ( 'zlib' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.zlib._windows_msvc_atom_module_zlib_LIBPATH( P_list['zlib'] )

    if( True == ( 'tbb' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.tbb._windows_msvc_atom_module_tbb_LIBPATH( P_list['tbb'] )

    if( True == ( 'protobuf' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.protobuf._windows_msvc_atom_module_protobuf_LIBPATH( P_list['protobuf'] )

    return []

def _windows_msvc_atom_package_LIBS( P_list ):

    if( True == ( 'boost' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.boost._windows_msvc_atom_module_boost_LIBS( P_list['boost'] )

    if( True == ( 'opencv' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.opencv._windows_msvc_atom_module_opencv_LIBS( P_list['opencv'] )

    if( True == ( 'zlib' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.zlib._windows_msvc_atom_module_zlib_LIBS( P_list['zlib'] )

    if( True == ( 'tbb' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.tbb._windows_msvc_atom_module_tbb_LIBS( P_list['tbb'] )

    if( True == ( 'protobuf' in  P_list ) ):
        return nucleotide.component.windows.msvc.atom.module.protobuf._windows_msvc_atom_module_protobuf_LIBS( P_list['protobuf'] )
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