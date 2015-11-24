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
#print 'Begin importing Module: -|' + __file__ + '|-' + '-|' + __name__ + '|-'
import gcc
import mingw
import msvc

## Ddetect existing translators
class Enumerate:
    m_list = []
    def __init__(self):
        i_msvc = msvc.MSVC()
        self.m_list += i_msvc.get()

        i_mingw = mingw.MinGW()
        self.m_list += i_mingw.get()

        i_gcc = gcc.GCC()
        self.m_list += i_gcc.get()
        #print self.m_list

    @staticmethod
    def platform():
        return platform.system()

    def get(self):
        return self.m_list

#print 'End importing Module: -|' + __file__ + '|-' + '-|' + __name__ + '|-'


#print 'os.name            = ' + os.name
#print 'sys.platform       = ' + sys.platform
#print
#print 'platform.uname()' + str( platform.uname() )
#print 'architecture  : ' + str( platform.architecture() )
#print 'dist()        : ' + str( platform.dist() )
#print 'Normal        : ', platform.platform()
#print 'Aliased       : ', platform.platform(aliased=True)
#print 'Terse         : ', platform.platform(terse=True)
#print 'system        : ', platform.system()
#print 'node          : ', platform.node()
#print 'release       : ', platform.release()
#print 'version       : ', platform.version()
#print 'machine       : ', platform.machine()
#print 'processor     : ', platform.processor()
#print platform.system_alias('','','')
#print
#print 'Python Version        :', platform.python_version()
#print 'Python Version tuple  :', platform.python_version_tuple()
#print 'Python Compiler       :', platform.python_compiler()
#print 'Python Build          :', platform.python_build()
#print 'Python Revision       :', platform.python_revision()
#print 'Python Implementation :', platform.python_implementation()
