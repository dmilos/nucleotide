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

atom_windows_exception = {
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
        'CPPFLAGS'  : ['/EHsc' ],
    },
    'name' : 'exception',
    'class': [  'exception', 'compiler:exception', 'windows:msvc:compiler:exception' ]
}

class Exception:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
         nucleotide.component.function.extend( P_option, 'windows:exception',    atom_windows_exception)

    @staticmethod
    def check():
        pass

