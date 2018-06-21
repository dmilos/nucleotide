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


component_windows_cygwingcc_atom_blank = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'cygwin'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'cygwingcc',
        'version': 'X' 
    },
    'name' :'blank',
    'config' : {
        'CPPDEFINES'   : [ ],
        'CPPFLAGS'     : [],
        'LIBS'   : [ ]
    },
    'class': [ 'blank', 'cygwingcc:blank' ]
}

class Blank:
    def __init__(self):
        pass

    @staticmethod
    def extend(P_option):
        nucleotide.component.function.extend( P_option, 'cygwingcc:blank', component_windows_cygwingcc_atom_blank )

    @staticmethod
    def check(self):
        pass
 