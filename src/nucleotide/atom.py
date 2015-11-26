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


import config
import klass
import translator

## Minimal action thats configure translator
class Atom:
    m_translator = None
    m_config    = None
    m_klass     = None

    def __init__( self, P_translator = translator.Translator(), P_config = config.Config(), P_class = klass.Klass() ):
        self.m_translator = P_translator
        self.m_config    = P_config
        self.m_klass     = P_class

    def set_translator( self, P_value ):
        self.m_translator = P_value

    def get_translator( self ):
        return self.m_translator

    def get_config( self ):
        return self.m_config

    def set_config( self, P_value ):
        self.m_config = P_value

    def set_klass( self, P_value ):
        self.m_klass = P_value

    def get_klass( self ):
        return self.m_klass

