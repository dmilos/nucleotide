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

##TODO Detect GCC on linux
class GCC:
    m_list = []
    def __init__(self):
        self.m_list = []
        if( 'Linux' != platform.system() ):
            return
        process = subprocess.Popen( [ 'gcc', '-dumpversion' ], stdout = subprocess.PIPE )
        version = str.split( process.communicate()[0], os.linesep )[0]

        I_data = {
                'platform' : {
                    'host'  : 'Linux',
                    'guest' : 'Linux'
                },
                'cc' : {
                    'vendor' : 'FSF',
                    'name'   : 'gcc',
                    'version': version
                }
            }

        self.m_list.append( nucleotide.Direction( I_data['platform'], I_data['cc'] ) )
        #print self.m_list

    def get(self):
        #print self.m_list
        return self.m_list
