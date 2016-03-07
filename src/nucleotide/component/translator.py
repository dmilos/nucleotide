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
import sys
import platform

import nucleotide
import nucleotide.component._common
import nucleotide.component._common.translator
import nucleotide.component.linux
import nucleotide.component.linux.translator
import nucleotide.component.windows
import nucleotide.component.windows.translator

## Detect existing translators
class Translator:
    m_list = None
    def __init__(self):
        self.m_list = []

        I__common  = nucleotide.component._common.translator.Translator()
        self.m_list += I__common.get()

        I_windows  = nucleotide.component.windows.translator.Translator()
        self.m_list += I_windows.get()

        I_linux  = nucleotide.component.linux.translator.Translator()
        self.m_list += I_linux.get()

    @staticmethod
    def extend(P_options):
        nucleotide.component._common.translator.Translator.extend( P_options )
        nucleotide.component.linux.translator.Translator.extend( P_options )
        nucleotide.component.windows.translator.Translator.extend( P_options )

    @staticmethod
    def platform():
        return platform.system()

    def get(self):
        return self.m_list
