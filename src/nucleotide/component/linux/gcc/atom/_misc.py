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

import nucleotide.translator
import nucleotide.config
import nucleotide.klass

atom_linux_shared_library = {
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
        # Nothing. It is empty
    },
    'name' :'dll',
    'class':  [ 'executable:shared_object', 'linux:executable:shared_object' ]
}

atom_linux_shared_object = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor': 'FSF',
        'name': 'gcc',
        'version': 'X'
    },
     'config' : {
           'CPPDEFINES'  : ['_LIB' ],
    },
    'name' :'lib',
    'class': [  'shared:library' ]
}

def init( P_option ) :

   #nucleotide.component.function.extend( P_option, 'architecture',        atom_linux_architecture )

    nucleotide.component.function.extend( P_option, 'linux:shared_library',        atom_linux_shared_library)
    nucleotide.component.function.extend( P_option, 'linux:shared_object',         atom_linux_shared_object)
    #nucleotide.component.function.extend( P_option, 'linux:static_release',        atom_linux_static_release)

   #nucleotide.component.function.extend( P_option, 'linux:linker:warning',    atom_linux_linker_warning )
   #nucleotide.component.function.extend( P_option, 'linux:compiler:feature:for-scope',  atom_linux_compiler_warning )   -ffor-scope




