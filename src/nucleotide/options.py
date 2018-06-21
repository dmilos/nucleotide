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

import nucleotide
import nucleotide.component
import nucleotide.component.translator

##  Set of atoms grouped around represents
#   An atom can be connected with several represents at the same time
# Answer on Questions: What I can do? or What is possibilities?
class Options:
    m_this = None
    m_represent = None

    def __init__( self, P_enumerate = True ):
        self.m_this = {}
        self.m_represent = {}

        #self.m_this['blank'] = nucleotide.atom.Atom( )

        if( True == P_enumerate ):
            self._enumerate( P_enumerate )

    @staticmethod
    def check():
        #nucleotide.component.translator.Translator.check()
        pass

    def _enumerate( self, P_enumerate = True ):
        if( False == P_enumerate ):
            return

        nucleotide.component.translator.Translator.extend( self )

    ##Extend current options with new atom
    def extend( self, P_name, P_atom ):
        #print( 'Options::extend ( P_name = ' + P_name + ', '+ ' )' )
        #print( '    Options::extend ( P_atom.get_translator().string() = ' + P_atom.get_translator().string() +' )' )
        #print( '    Options::extend ( P_atom.get_klass().others() = ' + str( P_atom.get_klass().others() ) +' )' )

        full_name = self.make_name( P_atom, P_name );
        self.m_this[ full_name ] = P_atom

        for represent in P_atom.get_klass().others():
            if( False == ( represent in self.m_represent ) ):
                self.m_represent[ represent ]  = []
            self.m_represent[ represent ] += [ full_name ]
            #print( '    Options::extend( represent: ' + represent  + '   with: '+ full_name+' )' )

    ##Return specific atom for given translator and universal name
    def get( self, P_translator, P_universal ):
        #print( 'Options::get(' + ' translator =' + P_translator.string()  + ', universal = '+ P_universal + ' )' )

        if( False == ( P_universal in self.m_represent ) ) :
            print( '    Options::get:: 0 - i_classeq = [] for \'' + P_universal + '\'' )
            return nucleotide.atom.Atom( )

        i_classeq = self.m_represent[ P_universal ]
        I_best = { 'level': -1, 'name': 'X' }
        #print( '    Options::get:: 1 - i_classeq = ' + str( i_classeq ) )

        for element in i_classeq:
            if( False == ( element in self.m_this ) ) :
                #print( '            Options::get:: 2 - no key = ' + str( element ) )
                continue
            I_level =  P_translator.similarity( self.m_this[ element ].get_translator() )
            if( I_best['level'] < I_level ):
                I_best['level'] = I_level
                I_best['name'] = element
            #print( '    Options::get:: 3 - ' + ' element:   ' + element + '; ' + ' level: ' + str( I_level ) )

        if( -1 == I_best['level'] ):
            print( '    Options::get:: 4 for: ' + '||' + str( I_best['level'] ) + '|| - ' + P_universal + " - " + I_best['name'] )
            return nucleotide.atom.Atom( )

        Options.message( '    Options::get:: 5 for: ' + '||' + str( I_best['level'] ) + '|| - ' + P_universal + " - " + I_best['name'] )
        return self.m_this[ I_best['name'] ]

    def get_this(self):
        return self.m_this

    def get_represents(self):
        return self.m_represent

    @staticmethod
    def message(P_message):
        print( P_message )

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

