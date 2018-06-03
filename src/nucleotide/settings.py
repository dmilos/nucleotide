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


import nucleotide


## Manipulate with all data needed to generating Scons.Environment
# Most important function is accumulate. Next one is extend.
class Settings:
    m_translator = None
    m_options    = None # Option or what is possible
    m_config     = None # This goes to Environment
    m_custom     = None
    m_info       = None

    def __init__( self, P_translator = None, P_options = None, P_custom = None ):
        if( None != P_translator ):
            self.m_translator = P_translator;
        else:
            catalog = nucleotide.Catalog()
            if( 0 != len( catalog.get() ) ):
                self.m_translator = catalog.get()[0]

        self.m_config = nucleotide.Config()
        if( None == P_options ):
            P_options = nucleotide.Options( True )
        self.m_options = P_options

        if( None == P_custom ):
            P_custom = nucleotide.Custom()
        self.m_custom = P_custom

    def get_translator( self ):
        return self.m_translator

    def get_options( self ):
        return self.m_options

    def get_config( self ):
        return self.m_config

    def exists_custom( self, P_name ):
        return self.m_custom.exists( P_name )

    def get_custom( self, P_name ):
        return self.m_custom.get( P_name )

    def set_custom( self, P_name, P_value ):
        self.m_custom.set( P_name, P_value )

    def get_info( self ):
        return self.m_info

    ##Add specified atom ( as unified name ) to be available for accumulating
    def extend( self, P_name, P_atom ):
        self.m_options.extend( P_name, P_atom )

    ##Add specified atom ( as unified name ) so the latter will be used for creating Scons.environment
    def accumulate( self, P_name, P_parameter = {} ):
        I_atom = self.m_options.get( self.m_translator, P_name );

        self.m_config.accumulate( I_atom.get_config(), P_parameter )
