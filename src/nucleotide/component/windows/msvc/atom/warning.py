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
import nucleotide.component._common.warning
import nucleotide.component._common.warning.util


def _windows_compiler_warning_CPPFLAGS( P_list ):
    Ir_list= []
    I_translator = nucleotide.translator.Translator( {'host'  : 'Windows','guest' : 'Windows'}, P_cc = { 'vendor': 'Microsoft', 'name': 'msvc', 'version': 'X'} )

    return nucleotide.component._common.warning.util.list( P_list, I_translator )

atom_windows_compiler_warning = {
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
        'CPPFLAGS' : _windows_compiler_warning_CPPFLAGS
    },
    'name' :'compiler:warning',
    'class':  [ 'compiler:warning', 'windows:compiler:warning' ]
}

class Warning:
    def __init__(self):
        pass

    @staticmethod
    def extend(P_option):
        nucleotide.component.function.extend( P_option, 'windows:compiler:warning',  atom_windows_compiler_warning )

    @staticmethod
    def check(self):
        pass
