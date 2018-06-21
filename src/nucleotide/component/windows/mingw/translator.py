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
import nucleotide.translator
import nucleotide.component
import nucleotide.component.windows
import nucleotide.component.windows.mingw
import nucleotide.component.windows.mingw.atom
import nucleotide.component.windows.mingw.atom.python

## Detect MinGW on Windows
class Translator:
    m_list = []
    def __init__(self):
        self.m_list = []

        try:
            process = subprocess.Popen( [ 'gcc', '-dumpversion' ], stdout = subprocess.PIPE )
        except( EnvironmentError ):
            return

        version = str.split( process.communicate()[0], os.linesep )[0]
        self.m_list.append( nucleotide.Translator(
                {
                    'host'  : 'Windows',
                    'guest' : 'Windows'
                },
                {
                    'vendor' : 'FSF',
                    'name'   : 'gcc',
                    'version': version
                }
              ) )

    def get(self):
        return self.m_list

    @staticmethod
    def check(self):
        pass

    @staticmethod
    def extend(P_options):
        nucleotide.component.windows.mingw.atom.python.Python.extend(P_options)


