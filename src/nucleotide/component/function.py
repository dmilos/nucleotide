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

import nucleotide
import nucleotide.component.constant
#TODO import nucleotide.translator.Translator
#TODO import nucleotide.config.Config
#TODO import nucleotide.klass.Klass
#TODO import nucleotide.atom.Atom



def join_out2(a,b):
    return a + separator_out  + b

def join_in2(a,b):
    return a + separator_in  + b

def join_in4(a,b,c,d):
    return a + separator_in  + b+ separator_in  + c + separator_in  + d

def join_in6(a,b,c,d,e):
    return a + separator_in  + b+ separator_in  + c + separator_in  + d + separator_in  + e

def prefix( P_atom ):
    return join_in4( P_atom['platform']['host'], P_atom['platform']['guest'],P_atom['cc']['vendor'], P_atom['cc']['name'], P_atom['cc']['version'] )

def make_name( P_atom ):
    return join_out2( prefix( P_atom ), P_atom['name'] )

def append( P_option, P_class, P_data ):
    full_name = make_name( P_data );
    P_option[ full_name ] = P_data['config']
    P_class[ P_data['class'] ]  += [ full_name ]

def extend( P_option, P_name, P_data ):
    I_translator = nucleotide.translator.Translator( P_data['platform'], P_data['cc'] )
    I_config    = nucleotide.config.Config( P_data['config']  )
    I_klass     = nucleotide.klass.Klass( P_data['class'] )

    I_atom = nucleotide.atom.Atom( I_translator, I_config, I_klass )
    P_option.extend( P_name, I_atom )


def check__env( P_name ) :
    value = os.getenv( P_name )
    if None == value:
        print(  P_name + ' Not exists' )
        return False
    print( P_name + ': -|' + value +'|-' )
    return True

