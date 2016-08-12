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
import nucleotide.component._common
import nucleotide.component._common.warning
import nucleotide.component._common.warning.util


def _linux_compiler_warning_CPPFLAGS( P_list ):
    Ir_list= []
    I_translator = nucleotide.translator.Translator( {'host'  : 'Linux','guest' : 'Linux'}, P_cc = { 'vendor': 'FSF', 'name': 'gcc', 'version': 'X'} )

    return nucleotide.component._common.warning.util.list( P_list, I_translator )

atom_linux_compiler_warning = {
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
        'CPPFLAGS' : _linux_compiler_warning_CPPFLAGS
    },
    'name' :'compiler:warning',
    'class':  [ 'compiler:warning', 'linux:compiler:warning' ]
}

class Warning:
    def __init__(self):
        pass

    @staticmethod
    def extend(P_option):
        nucleotide.component.function.extend( P_option, 'A:linux:compiler:warning',  atom_linux_compiler_warning )
        atom_linux_compiler_warning['platform']['host'] = 'X';
        nucleotide.component.function.extend( P_option, 'x:linux:compiler:warning',  atom_linux_compiler_warning )
        atom_linux_compiler_warning['platform']['guest'] = 'X';
        nucleotide.component.function.extend( P_option, 'y:linux:compiler:warning',  atom_linux_compiler_warning )

    @staticmethod
    def check(self):
        pass
