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

import platform
import copy

import nucleotide.translator

##TODO Detect MSVC on Window
class MSVC:
    m_list = []
    def __init__(self):
        self.m_list = []

        if( 'Windows' != platform.system() ):
            return

        I_data = nucleotide.Translator.blank()
        I_data['platform']['host'] = 'Windows'
        I_data['platform']['guest'] = 'Windows'
        I_data['cc']['vendor'] = 'Microsoft'
        I_data['cc']['name'] = 'msvc'

        if( True == MSVC._exists( _winreg_HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\VisualStudio\\12.0' ) ):
            I_data['cc']['version'] = '12'
            I_c = copy.deepcopy( I_data )
            self.m_list.append( nucleotide.Translator( I_c['platform'], I_c['cc'] ) )

        if( True == MSVC._exists( _winreg_HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\VisualStudio\\11.0' ) ):
            I_data['cc']['version'] = '11'
            I_c = copy.deepcopy( I_data )
            self.m_list.append( nucleotide.Translator( I_c['platform'], I_c['cc'] ) )

        if( True == MSVC._exists( _winreg_HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\VisualStudio\\10.0' ) ):
            I_data['cc']['version'] = '10'
            I_c = copy.deepcopy( I_data )
            self.m_list.append( nucleotide.Translator( I_c['platform'], I_c['cc'] ) )

        if( True == MSVC._exists( _winreg_HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\VisualStudio\\9.0' ) ):
            I_data['cc']['version'] = '9'
            I_c = copy.deepcopy( I_data )
            self.m_list.append( nucleotide.Translator( I_c['platform'], I_c['cc'] ) )


        #print self.m_list[0].get()
        #print self.m_list[1].get()
        #print self.m_list[2].get()
        #print self.m_list[3].get()

    def get(self):
        return self.m_list

    @staticmethod
    def _exists( key, sub_key ):
        try:
            k = _winreg_OpenKey( key, sub_key )
            _winreg_CloseKey( k )
            result = True
        except WindowsError:
            result = False
        return result

msvc = MSVC()
