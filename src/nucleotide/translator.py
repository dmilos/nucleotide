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


import re
import copy

## Translator infromation
#
class Translator:
    m_translator ={}

    def __init__( self, P_platform = {'host'  : 'X','guest' : 'X'}, P_cc = { 'vendor': 'X', 'name': 'X', 'version': 'X'} ):
        self.m_translator = {}
        self.m_translator['platform'] = copy.deepcopy( P_platform )
        self.m_translator['cc'] = copy.deepcopy( P_cc )

    def set_platform_host( self, P_value ):
        self.m_translator['platform']['host'] = P_value

    def set_platform_guest( self, P_value ):
        self.m_translator['platform']['guest'] = P_value

    def set_cc_vendor( self, P_value ):
        self.m_translator['cc']['vendor'] = P_value

    def set_cc_name( self, P_value ):
        self.m_translator['cc']['name'] = P_value

    def set_cc_version( self, P_value ):
        self.m_translator['cc']['version'] = P_value

    def get( self ):
        return self.m_translator

    def similarity( self, P_other ):
        I_level = -1
        #print( __file__ +' - P_other.m_translator == '+ str( P_other.m_translator ) )
        #print( __file__ +' - self.m_translator    == '+ str(    self.m_translator ) )

        I_match = Translator._similarity0( self.m_translator['platform']['host' ], P_other.m_translator['platform']['host' ] );
        if( 0 == I_match ):
            return -1

        I_level += 1

        I_match = Translator._similarity0( self.m_translator['platform']['guest' ], P_other.m_translator['platform']['guest' ] );
        if( 0 == I_match ):
            return -1

        I_level += 1

        I_match = Translator._similarity0( self.m_translator['cc']['vendor'], P_other.m_translator['cc']['vendor'] );
        I_level += [  -9000,    50,    50,    90 ][ I_match ]
        I_match = Translator._similarity0( self.m_translator['cc']['name'], P_other.m_translator['cc']['name'] );
        I_level += [  -9000,   500,   500,   900 ][ I_match ]
        I_match = Translator._similarity0( self.m_translator['cc']['version'], P_other.m_translator['cc']['version'] );
        I_level += [  -9000,  5000,  5000,  9000 ][ I_match ]

        return I_level


    ## Make blank information structure
    @staticmethod
    def blank():
        return copy.deepcopy( {
                'platform' : {
                    'host'  : 'X',
                    'guest' : 'X'
                },
                'cc' : {
                    'vendor' : 'X',
                    'name'   : 'X',
                    'version': 'X'
                }
            })


    @staticmethod
    def _similarity0( P_left, P_right ):
        #print( '        P_left = '+P_left+' , P_right = '+ P_right +' ' )
        if( P_left == P_right ):
            #print( '            2' )
            return 3
        if( 'X' == P_left ):
            #print( '            1' )
            return 2
        if( 'X' == P_right ):
            #print( '            1')
            return 1
        #print( '            0' )
        return 0;


    def string( self ):
        return \
                    self.m_translator['platform']['host'] \
            + '-' + self.m_translator['platform']['guest'] \
            + '-' + self.m_translator['cc']['vendor'] \
            + '-' + self.m_translator['cc']['name'] \
            + '-' + self.m_translator['cc']['version']


    @staticmethod
    def extract( P_string ):
        #print( 'Directory.extract(' + P_string + ')' )
        m = re.match( '(\w*)-(\w*)-(\w*)-(\w*)-(\w*)', P_string )
        if( None == m ):
            #print 'Directory.extract:: return invalid'
            return Translator( {'host'  : 'Y','guest' : 'Y'}, { 'vendor': 'Y', 'name': 'Y', 'version': 'Y'} )

        Ir_return = Translator( {'host' : m.group(1), 'guest' : m.group(2) }, { 'vendor': m.group(3), 'name': m.group(4), 'version': m.group(5)} )
        #print() 'Directory.extract( P_string =' + P_string + ' ) -> ' +str( Ir_return.m_translator ) )
        return Ir_return

