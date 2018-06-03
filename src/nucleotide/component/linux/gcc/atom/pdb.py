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


def _linux_PDB_CPPFLAGS( P_data ):
    Ir_list = [ '-g' ]
    return Ir_list

    if( True == ( 'file-name-compile' in P_data ) ):
        Ir_list.append( 'TODO"' + P_data['file-name-compile'] + '"' )
    else:
        if( True == ( 'file-name' in P_data ) ):
            Ir_list.append( 'TODO"' + P_data['file-name'] + '"' )

    return Ir_list

atom_linux_PDB = {
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
        'CPPFLAGS'  : _linux_PDB_CPPFLAGS,
    },
    'name' : 'PDB',
    'class': [  'PDB', 'linux:PDB' ]
}

class PDB:
    def __init__(self):
        pass

    @staticmethod
    def extend( P_option ):
         nucleotide.component.function.extend( P_option, 'A:linux:PDB',           atom_linux_PDB )
         atom_linux_PDB['platform']['host'] = 'X'; 
         nucleotide.component.function.extend( P_option, 'x:linux:PDB',           atom_linux_PDB )
         atom_linux_PDB['platform']['guest'] = 'X'; 
         nucleotide.component.function.extend( P_option, 'y:linux:PDB',           atom_linux_PDB )

    @staticmethod
    def check():
        pass
 
