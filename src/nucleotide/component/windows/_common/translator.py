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


import platform

import nucleotide
import nucleotide.component
import nucleotide.component.windows
import nucleotide.component.windows._common
import nucleotide.component.windows._common.python
import nucleotide.component.windows._common.boost

## Detect _Common on Linux
class Translator:
    m_list = []
    def __init__(self):
        self.m_list = []
        if( 'Linux' != platform.system() ):
            return

    def get(self):
        return self.m_list

    def check(self):
        pass

    @staticmethod
    def extend(P_options):
        if( 'Windows' != platform.system() ):
            return

        nucleotide.component.windows._common.python.Python.extend(P_options)
        nucleotide.component.windows._common.boost.Boost.extend(P_options)

