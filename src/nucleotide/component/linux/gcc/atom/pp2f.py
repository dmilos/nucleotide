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

atom_linux_pp2f = {
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
            'CPPFLAGS'  : ['-E' ],
    },
    'name' : 'pp2f',
    'class':  [ 'pp2f', 'linux:pp2f' ]
}

class PP2F:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
         nucleotide.component.function.extend( P_option, 'A:linux:pp2f',                atom_linux_pp2f    )
         atom_linux_pp2f['platform']['host'] = 'X';
         nucleotide.component.function.extend( P_option, 'x:linux:pp2f',               atom_linux_pp2f    )
         atom_linux_pp2f['platform']['guest'] = 'X';
         nucleotide.component.function.extend( P_option, 'y:linux:pp2f',               atom_linux_pp2f    )


    @staticmethod
    def check():
        pass

