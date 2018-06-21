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
import glob
import re

import nucleotide
import nucleotide.component
import nucleotide.component.linux
import nucleotide.component.linux.gcc
import nucleotide.component.linux.gcc.atom
import nucleotide.component.linux.gcc.atom._misc
import nucleotide.component.linux.gcc.atom.python
import nucleotide.component.linux.gcc.atom.warning
import nucleotide.component.linux.gcc.atom.pdb
import nucleotide.component.linux.gcc.atom.blank
import nucleotide.component.linux.gcc.atom.rtl
import nucleotide.component.linux.gcc.atom.rtti
import nucleotide.component.linux.gcc.atom.pp2f
import nucleotide.component.linux.gcc.atom.exception
import nucleotide.component.linux.gcc.atom.dialect
import nucleotide.component.linux.gcc.atom.encode
import nucleotide.component.linux.gcc.atom.executable
import nucleotide.component.linux.gcc.atom.macro
import nucleotide.component.linux.gcc.atom.version
import nucleotide.component.linux.gcc.atom.configuration
import nucleotide.component.linux.gcc.atom.optimization
import nucleotide.component.linux.gcc.atom.package
import nucleotide.component.linux.gcc.atom.alignment

## Detect GCC on linux
class Translator:
    m_list = []

    def __init__(self):
        self.m_list = []

        I_data = {
                'platform' : {
                    'host'  : 'Linux',
                    'guest' : 'Linux'
                },
                'cc' : {
                    'vendor' : 'FSF',
                    'name'   : 'gcc',
                    'version': 'X'
                }
            }
        self.m_list += [ nucleotide.Translator( I_data['platform'], I_data['cc'] ) ]

        r = re.compile('/usr/bin/gcc-(([0-9]+)(\\.[0-9]+)*)')

        list = glob.glob("/usr/bin/gcc-*")

        for item in list:
            m = r.search( item )
            if( None == m ):
                continue
            I_data = {
                    'platform' : {
                        'host'  : 'Linux',
                        'guest' : 'Linux'
                    },
                    'cc' : {
                        'vendor' : 'FSF',
                        'name'   : 'gcc',
                        'version': m.group(1)
                    }
                }
            self.m_list += [ nucleotide.Translator( I_data['platform'], I_data['cc'] ) ]

    def get(self):
        return self.m_list

    @staticmethod
    def check():
        return True

    @staticmethod
    def extend(P_options):
        nucleotide.component.linux.gcc.atom._misc.init(P_options)
        nucleotide.component.linux.gcc.atom.python.Python.extend(P_options)
        nucleotide.component.linux.gcc.atom.warning.Warning.extend(P_options)
        nucleotide.component.linux.gcc.atom.pdb.PDB.extend(P_options)
        nucleotide.component.linux.gcc.atom.blank.Blank.extend(P_options)
        nucleotide.component.linux.gcc.atom.rtl.RTL.extend(P_options)
        nucleotide.component.linux.gcc.atom.rtti.RTTI.extend(P_options)
        nucleotide.component.linux.gcc.atom.pp2f.PP2F.extend(P_options)
        nucleotide.component.linux.gcc.atom.exception.Exception.extend(P_options)
        nucleotide.component.linux.gcc.atom.dialect.Dialect.extend(P_options)
        nucleotide.component.linux.gcc.atom.encode.Encode.extend(P_options)
        nucleotide.component.linux.gcc.atom.executable.Executable.extend(P_options)
        nucleotide.component.linux.gcc.atom.macro.Macro.extend(P_options)
        nucleotide.component.linux.gcc.atom.version.Version.extend(P_options)
        nucleotide.component.linux.gcc.atom.configuration.Configuration.extend(P_options)
        nucleotide.component.linux.gcc.atom.optimization.Optimization.extend(P_options)
        nucleotide.component.linux.gcc.atom.package.Package.extend(P_options)
        nucleotide.component.linux.gcc.atom.alignment.Alignment.extend(P_options)


