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

def _component_linux_gcc_atom_module_opencv_CPPDEFINES( P_data ):
    Ir_list = ["OPENCV"]

    return Ir_list

def _component_linux_gcc_atom_module_opencv_CPPPATH( P_data ):
    Ir_list = ['/usr/local/include/opencv', '/usr/local/include/opencv2']
    return Ir_list

def _component_linux_gcc_atom_module_opencv_LINKFLAGS( P_data ):
    Ir_list = []

    return Ir_list

def _component_linux_gcc_atom_module_opencv_LIBPATH( P_data ):
    Ir_list = [ "/usr/local/lib/", "/usr/lib" ]

    return Ir_list

def _component_linux_gcc_atom_module_opencv_LIBS( P_data ):
    Ir_list = [ "libopencv_core.dll", "opencv_highgui.dll", "opencv_imgproc.dll", "opencv_videoio.dll", "opencv_imgproc.dll" ]

    return Ir_list

atom_linux_configuration = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
        'CPPDEFINES' : _component_linux_gcc_atom_module_opencv_CPPDEFINES,
        'CPPPATH'    : _component_linux_gcc_atom_module_opencv_CPPPATH,
        'LINKFLAGS'  : _component_linux_gcc_atom_module_opencv_LINKFLAGS,
        'LIBPATH'    : _component_linux_gcc_atom_module_opencv_LIBPATH,
        'LIBS'       : _component_linux_gcc_atom_module_opencv_LIBS,
    },
    'name' :'package',
    'class':  [ 'package::opencv', 'linux:package:opencv' ]
}

class Configuration:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
         nucleotide.component.function.extend( P_option, 'A:linux:compiler:configuration',               atom_linux_configuration )
         atom_linux_configuration['platform']['host']='X'
         nucleotide.component.function.extend( P_option, 'x:linux:compiler:configuration',               atom_linux_configuration )
         atom_linux_configuration['platform']['guest']='X'
         nucleotide.component.function.extend( P_option, 'y:linux:compiler:configuration',               atom_linux_configuration )

    @staticmethod
    def check():
        pass
