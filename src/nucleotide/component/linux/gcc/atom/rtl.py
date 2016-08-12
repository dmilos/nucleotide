
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

def _linux_RTL_LINKFLAGS( P_data ):
    I_flag = ''
 
    #if( 'dynamic' == P_data['type'] ):
    #   I_flag += 'D'
    if( 'static' == P_data['type'] ):
       I_flag += '-static'
    return [ I_flag ]

atom_linux_RTL = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor': 'FSF',
        'name'  : 'gcc',
        'version': 'X'
    },
    'config' : {
        'LINKFLAGS'  : _linux_RTL_LINKFLAGS
    },
    'name' :'RTL',
    'class':  [ 'RTL', 'linux:RTL' ]
}

class RTL:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
         nucleotide.component.function.extend( P_option, 'A:linux:RTL',                 atom_linux_RTL )
         atom_linux_RTL['platform']['host'] = 'X';
         nucleotide.component.function.extend( P_option, 'x:linux:RTL',                 atom_linux_RTL )
         atom_linux_RTL['platform']['guest'] = 'X';
         nucleotide.component.function.extend( P_option, 'y:linux:RTL',                 atom_linux_RTL )

    @staticmethod
    def check():
        pass
