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

atom_boost_blank = {
    'platform' : {
        'host'  : 'X',
        'guest' : 'X'
    },
    'cc' : {
        'vendor' : 'X',
        'name'   : 'X',
        'version': 'X'
    },
    'config' : {
    },
    'name' : 'boost:blank',
    'class':  [ 'boost', 'boost:blank' ]
}

class Boost:


    def init( P_option ) :
        function.extend( P_option, 'boost:blank',           atom_boost_blank            )

    def check():
        pass