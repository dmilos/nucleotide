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

import platform

import nucleotide
import nucleotide.component
import nucleotide.component.warning.table
import nucleotide.translator

def windows_make( P_native, P_status ):
    Ir_switch = ''
   #if( 'enable'   == P_status ): Ir_switch = ''
    if( 'disable'  == P_status ): Ir_switch = '/wd' + P_native 
    if( 'error'    == P_status ): Ir_switch = '/we' + P_native 
    if( 'once'     == P_status ): Ir_switch = '/wo' + P_native 
    return Ir_switch

def linux_make( P_native, P_status ):
    Ir_switch = ''
    if( 'enable'   == P_status ): Ir_switch = ''
    if( 'disable'  == P_status ): Ir_switch = '-Wno-'    + P_native
    if( 'error'    == P_status ): Ir_switch = '-Werror=' + P_native
    if( 'once'     == P_status ): Ir_switch = ''
    return Ir_switch

def convertor(P_translator):
    if( 'Linux'   == platform.system() ):
        return linux_make 
    if( 'Windows' == platform.system() ): 
        return windows_make 

def list( P_list, P_translator ):
    #print 
    #print __file__ + ' - ' + str( P_translator.get() )
    Ir_list = []
    I_convertor = convertor( P_translator )
    for item in P_list:
        if( False == nucleotide.component.warning.table.TABLE.has_key( item ) ):
            continue
        I_best = -1
        for elem in nucleotide.component.warning.table.TABLE[item]:
            I_similar = P_translator.smilarity( nucleotide.translator.Translator.extract( elem ) ) 
            if( I_best < I_similar ):
                I_best = I_similar
                I_text = nucleotide.component.warning.table.TABLE[item][elem]
        if( -1 != I_best ):
            Ir_list += [ I_convertor( I_text, P_list[item]) ]
            #print '        ' + __file__ + ' - ||' + str( I_best ) + '||  Name = ' + I_text
    #print '    ' + __file__ + ' - ' + str( Ir_list )
    return Ir_list
