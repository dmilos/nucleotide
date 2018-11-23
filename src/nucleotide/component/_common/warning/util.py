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
import nucleotide.component._common
import nucleotide.component._common.warning
import nucleotide.component._common.warning.table

def windows_make( P_native, P_status ): # https://msdn.microsoft.com/en-us/library/thxezb7y.aspx
    Ir_switch = ''
    if( 'enable'   == P_status ): Ir_switch = '/w1' + P_native
    if( 'disable'  == P_status ): Ir_switch = '/wd' + P_native
    if( 'error'    == P_status ): Ir_switch = '/we' + P_native
    if( 'once'     == P_status ): Ir_switch = '/wo' + P_native
    return Ir_switch

def linux_make( P_native, P_status ):
    Ir_switch = ''
    if( 'enable'   == P_status ): Ir_switch = '-W'       + P_native
    if( 'disable'  == P_status ): Ir_switch = '-Wno-'    + P_native
    if( 'error'    == P_status ): Ir_switch = '-Werror=' + P_native
    if( 'once'     == P_status ): Ir_switch = ''
    return Ir_switch

def convertor(P_translator):
    if( 'Linux'   == platform.system() ):
        return linux_make

    if( 'Windows' == platform.system() ):
        return windows_make

    if( 'CYGWIN_NT' in platform.system() ):
        return linux_make

    print( "Unknown Platform : " + platform.system() )
    return None

def list( P_list, P_translator ):
    Ir_list = []
    I_convertor = convertor( P_translator )

    if( None == I_convertor ):
        print( "Non convertor" )
        return Ir_list;

    for item in P_list:
        if( False == ( item in nucleotide.component._common.warning.table.TABLE ) ):
            continue
        I_best = -1
        for elem in nucleotide.component._common.warning.table.TABLE[item]:
            I_similar = P_translator.similarity( nucleotide.translator.Translator.extract( elem ) )
            if( I_best < I_similar ):
                I_best = I_similar
                I_text = nucleotide.component._common.warning.table.TABLE[item][elem]
        if( -1 != I_best ):
            Ir_list += [ I_convertor( I_text, P_list[item] ) ]
        else:
            pass
        print( "        ||" + str(I_best) + '|| - ' + str( Ir_list ) )

    return Ir_list
