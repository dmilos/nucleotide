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
import copy

_winreg_HKEY_LOCAL_MACHINE = 0
_winreg_OpenKey  = None
_winreg_CloseKey = None

try:
    import _winreg
    _winreg_HKEY_LOCAL_MACHINE = _winreg.HKEY_LOCAL_MACHINE
    _winreg_OpenKey  = _winreg.OpenKey
    _winreg_CloseKey = _winreg.CloseKey
except ImportError:
    pass

import nucleotide
import nucleotide.translator
import nucleotide.component
import nucleotide.component.windows
import nucleotide.component.windows.msvc
import nucleotide.component.windows.msvc.atom
import nucleotide.component.windows.msvc.atom._misc
import nucleotide.component.windows.msvc.atom.boost
import nucleotide.component.windows.msvc.atom.python
import nucleotide.component.windows.msvc.atom.warning
import nucleotide.component.windows.msvc.atom.rtti
import nucleotide.component.windows.msvc.atom.rtl
import nucleotide.component.windows.msvc.atom.pdb
import nucleotide.component.windows.msvc.atom.version
import nucleotide.component.windows.msvc.atom.blank
import nucleotide.component.windows.msvc.atom.dialect
import nucleotide.component.windows.msvc.atom.pp2f
import nucleotide.component.windows.msvc.atom.executable
import nucleotide.component.windows.msvc.atom.exception
import nucleotide.component.windows.msvc.atom.macro


##Detect MSVC on Window
class Translator:
    m_list = []
    def __init__(self):
        self.m_list = []

        I_data = nucleotide.Translator.blank()
        I_data['platform']['host'] = 'Windows'
        I_data['platform']['guest'] = 'Windows'
        I_data['cc']['vendor'] = 'Microsoft'
        I_data['cc']['name'] = 'msvc'

        if( True == Translator._exists( _winreg_HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\VisualStudio\\12.0' ) ):
            I_data['cc']['version'] = '12'
            I_c = copy.deepcopy( I_data )
            self.m_list.append( nucleotide.Translator( I_c['platform'], I_c['cc'] ) )

        if( True == Translator._exists( _winreg_HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\VisualStudio\\11.0' ) ):
            I_data['cc']['version'] = '11'
            I_c = copy.deepcopy( I_data )
            self.m_list.append( nucleotide.Translator( I_c['platform'], I_c['cc'] ) )

        if( True == Translator._exists( _winreg_HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\VisualStudio\\10.0' ) ):
            I_data['cc']['version'] = '10'
            I_c = copy.deepcopy( I_data )
            self.m_list.append( nucleotide.Translator( I_c['platform'], I_c['cc'] ) )

        if( True == Translator._exists( _winreg_HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\VisualStudio\\9.0' ) ):
            I_data['cc']['version'] = '9'
            I_c = copy.deepcopy( I_data )
            self.m_list.append( nucleotide.Translator( I_c['platform'], I_c['cc'] ) )

    def get(self):
        return self.m_list

    @staticmethod
    def check():
        return True

    @staticmethod
    def extend(P_options):
        nucleotide.component.windows.msvc.atom._misc.init(P_options)
        nucleotide.component.windows.msvc.atom.boost.Boost.extend(P_options)
        nucleotide.component.windows.msvc.atom.python.Python.extend(P_options)
        nucleotide.component.windows.msvc.atom.warning.Warning.extend(P_options)

        nucleotide.component.windows.msvc.atom.rtti.RTTI.extend(P_options)
        nucleotide.component.windows.msvc.atom.rtl.RTL.extend(P_options)
        nucleotide.component.windows.msvc.atom.pdb.PDB.extend(P_options)

        nucleotide.component.windows.msvc.atom.version.Version.extend(P_options)
        nucleotide.component.windows.msvc.atom.blank.Blank.extend(P_options)
        nucleotide.component.windows.msvc.atom.dialect.Dialect.extend(P_options)
        nucleotide.component.windows.msvc.atom.pp2f.PP2F.extend(P_options)
        nucleotide.component.windows.msvc.atom.executable.Executable.extend(P_options)
        nucleotide.component.windows.msvc.atom.exception.Exception.extend(P_options)
        nucleotide.component.windows.msvc.atom.macro.Macro.extend(P_options)

    @staticmethod
    def _exists( key, sub_key ):
        try:
            k = _winreg_OpenKey( key, sub_key )
            _winreg_CloseKey( k )
            result = True
        except WindowsError:
            result = False
        return result
