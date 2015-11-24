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


def windows_make( P_native, P_status ):
   #if( 'enable'   == P_status ): Ir_list += []
    if( 'disable'  == P_status ): Ir_list += ['/wd' + P_native]
    if( 'error'    == P_status ): Ir_list += ['/we' + P_native]
    if( 'once'     == P_status ): Ir_list += ['/wo' + P_native]

def linux_make( P_native, P_status ):
    if( 'enable'   == P_status ): Ir_list += []
    if( 'disable'  == P_status ): Ir_list += [ '-W'       + P_native ]
    if( 'error'    == P_status ): Ir_list += [ '-Werror=' + P_native ]
    if( 'once'     == P_status ): Ir_list += []

def general2specific( P_name, P_specific ):
    if( True == warning_table.Has_key( P_name ) ):
        if( True == warning_table[P_name].Has_key( P_specific ) ):
            return warning_table[P_name][P_specific]
    return ''

def specific2general( P_data, P_specific ):
    #for item in warning_table:
    #    if( True == warning_table[item].Has_key( P_specific ) ):
    #        if( P_data == warning_table[item][P_specific] )
    #            return item
    pass

