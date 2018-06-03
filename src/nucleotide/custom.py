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


import copy

## Miscelenious custom data, organised in simple ( key, data ) pairs
class Custom:

    ## Don not use this member directly
    m_dictinary= {}

    def __init__( self, P_dictinary = {} ):
        self.m_dictinary = copy.deepcopy( P_dictinary )

    def get( self, P_name ):
        if( False == ( P_name in self.m_dictinary ) ):
            return None
        return self.m_dictinary[ P_name  ]

    def set( self, P_name, P_value ):
        self.m_dictinary[ P_name ] = P_value

    def exists( self, P_name ):
        if( False == ( P_name in self.m_dictinary ) ):
            return False
        return True

    def get_dictinary( self ):
        return self.m_dictinary
