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


atom_windows_blank = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor' : 'Microsoft',
        'name'   : 'msvc',
        'version': 'X'
    },
    'name' :'blank',
    'config' : {
        'CPPDEFINES'   : ['WIN32', '_WINDOWS' ],
        'CPPFLAGS'     : ['/Zc:forScope'],
        #'LIBS'   : [ 'kernel32.lib', 'user32.lib', 'gdi32.lib', 'winspool.lib', 'comdlg32.lib', 'advapi32.lib', 'shell32.lib', 'ole32.lib', 'oleaut32.lib', 'uuid.lib', 'odbc32.lib', 'odbccp32.lib' ]
    },
    'class': [ 'blank', 'windows:blank' ]
}

class Blank:
    def __init__(self):
        pass

    @staticmethod
    def extend(P_option):
        nucleotide.component.function.extend( P_option, 'windows:blank', atom_windows_blank )

    @staticmethod
    def check(self):
        pass
 