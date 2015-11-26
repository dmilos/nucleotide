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

class MinGW:
    m_list = []
    def __init__(self):
        self.m_list = []
        if( 'Windows' != platform.system() ):
            return
        try:
            process = subprocess.Popen( [ 'gcc', '-dumpversion' ], stdout = subprocess.PIPE )
        except EnvironmentError, e:
            #print 'No Mingw'
            return

        version = str.split( process.communicate()[0], os.linesep )[0]
        self.m_list.append( nucleotide.Translator( {
                'platform' : {
                    'host'  : 'Windows',
                    'guest' : 'Windows'
                },
                'cc' : {
                    'vendor' : 'FSF',
                    'name'   : 'gcc',
                    'version': version
                }
            } ) )

    def get(self):
        return self.m_list
