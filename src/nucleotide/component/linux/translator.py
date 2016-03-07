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


import subprocess
import platform
import os

import nucleotide
import nucleotide.component
import nucleotide.component.linux
import nucleotide.component.linux._common
import nucleotide.component.linux._common.translator
import nucleotide.component.linux.gcc
import nucleotide.component.linux.gcc.translator

## Detect Translators on Linux
class Translator:
    m_list = []
    def __init__(self):
        self.m_list = []
        if( 'Linux' != platform.system() ):
            return

        I__common  = nucleotide.component.linux._common.translator.Translator()
        self.m_list += I__common.get()

        I_gcc      = nucleotide.component.linux.gcc.translator.Translator()
        self.m_list += I_gcc.get()

    def get(self):
        return self.m_list

    def check(self):
        pass

    @staticmethod
    def extend(P_options):
        if( 'Linux' != platform.system() ):
            return

        nucleotide.component.linux._common.translator.Translator.extend(P_options)
        nucleotide.component.linux.gcc.translator.Translator.extend(P_options)

