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


import sys
import platform

import atom
import translator
import component

## TODO
#    Set of atoms grouped around represents
#   An atom can be grouped around several represents
class Options:
    m_this = {}
    m_represent = {}

    def __init__( self, P_enumerate = True ):
        self.m_this['blank'] = atom.Atom( )
        if( True == P_enumerate ):
            self._enumerate( P_enumerate )

    @staticmethod
    def check():
        component.python.check( )
        component.boost.check( )
        if( 'Windows' == platform.system() ):
            component.windows.check( )
        component.linux.check( )

    def _enumerate( self, P_enumerate = True ):
        if( False == P_enumerate ):
            return
        component.python.init( self )
        component.boost.init( self )
        if( 'Windows' == platform.system() ):
            component.windows.init( self )
        if( 'Linux' == platform.system() ):
            component.linux.init( self )

    ##Extend current options with new atom
    def extend( self, P_name, P_atom ):
        #print 'Options::extend ( P_name = ' + P_name+ ' )'
        full_name = self.make_name( P_atom, P_name );
        self.m_this[ full_name ] = P_atom

        for represent in P_atom.get_klass().others():
            if( False == self.m_represent.has_key( represent ) ):
                self.m_represent[ represent ]  = []
            self.m_represent[ represent ] += [ full_name ]
            #print '    Options::extend( represent: ' + represent  + '   with: '+ full_name+' )'

    ##Extend current options with new atom
    def get( self, P_translator, P_universal ):
        #print 'Options::get(' + ' P_translator =' + P_translator.string()  + ', P_universal = '+ P_universal + ' )'

        if( False == self.m_represent.has_key( P_universal ) ) :
            print '    Options::get:: 0 - i_classeq = [] for ' + P_universal
            return atom.Atom( )

        i_classeq = self.m_represent[ P_universal ]
        I_best = { 'level': -1, 'name': 'X' }
        #print '    Options::get:: 1 - i_classeq = ' + str( i_classeq )

        for element in i_classeq:
            if( False == self.m_this.has_key( element ) ) :
                #print '    Options::get:: 2 - no key = ' + str( element )
                continue
            I_level =  P_translator.smilarity( self.m_this[ element ].get_translator() )
            if( I_best['level'] < I_level ):
                I_best['level'] = I_level
                I_best['name'] = element
            #print '    Options::get:: 3 - ' + ' element:   ' + element + ' ; ' + ' level: ' + str( I_level )

        if( -1 == I_best['level'] ):
            print '    Options::get:: 4 ' + P_universal + ' - I_best[\'level\'] = ' + str( I_best['level'] )
            return atom.Atom( )

        print '    Options::get:: 5 for: ' + P_universal + ' - return: ||' + str( I_best['level'] ) + '|| - '+  I_best['name']
        return self.m_this[ I_best['name'] ]

    def join_out2(self, a, b ):
        return a + '::'  + b

    def join_in2(a,b):
        return a + separator_in  + b

    def join_in4(a,b,c,d):
        return a + separator_in  + b+ separator_in  + c + separator_in  + d

    def join_in6(a,b,c,d,e):
        return a + separator_in  + b+ separator_in  + c + separator_in  + d + separator_in  + e

    def make_name( self,P_atom, P_name ):
        return self.join_out2( P_atom.get_translator().string(), P_name )

