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
import nucleotide.component.windows
import nucleotide.component.windows._common
import nucleotide.component.windows._common.translator
import nucleotide.component.windows.mingw
import nucleotide.component.windows.mingw.translator
import nucleotide.component.windows.msvc
import nucleotide.component.windows.msvc.translator
import nucleotide.component.windows.cygwingcc
import nucleotide.component.windows.cygwingcc.translator

## Detect MinGW on Windows
class Translator:
    m_list = []
    def __init__(self):
        self.m_list = []

        if( False == Translator._detect() ):
            return

        I__common = nucleotide.component.windows._common.translator.Translator()
        self.m_list += I__common.get()

        I_mingw    = nucleotide.component.windows.mingw.translator.Translator()
        self.m_list += I_mingw.get()

        if( 'Windows' == platform.system() ):
            I_msvc   = nucleotide.component.windows.msvc.translator.Translator()
            self.m_list += I_msvc.get()

        if( 'CYGWIN_NT' in platform.system() ):
            I_cygwin    = nucleotide.component.windows.mingw.translator.Translator()
            self.m_list += I_cygwin.get()

    def get(self):
        return self.m_list

    def check(self):
        pass

    @staticmethod
    def extend(P_options):

        if( False == Translator._detect() ):
            return

        nucleotide.component.windows._common.translator.Translator.extend(P_options)
        nucleotide.component.windows.mingw.translator.Translator.extend(P_options)

        if( 'Windows' == platform.system() ):
            nucleotide.component.windows.msvc.translator.Translator.extend(P_options)

        if( 'CYGWIN_NT' in platform.system() ):
            nucleotide.component.windows.cygwingcc.translator.Translator.extend(P_options)

    @staticmethod
    def _detect():
        if( 'Windows' == platform.system() ):
            #print ( "Platform: " + platform.system() )
            return True

        if( 'CYGWIN_NT' in platform.system() ):
            #print ( "Platform: " + platform.system() )
            return True

        print ( "Unknown Platform: " + platform.system() )
        return False
