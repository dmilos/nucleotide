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
import platform
import itertools
import copy
import sys


def find_ENVIRONMENT__generic( P_prefix, P_list, P_folder, P_ensure ):

    version =''
    architecture=''
    compiler=''

    I_element=[]
    if( "version"           in P_ensure ):
        if( True == ( 'version'         in P_list ) ): I_element += [ P_list['version']        ]
    if( "architecture"      in P_ensure ):
        if( True == ( 'architecture'    in P_list ) ): I_element += [ P_list["architecture"]   ]
    if( "compiler"          in P_ensure ):
        if( True == ( 'compiler'        in P_list ) ): I_element += [ P_list["compiler"]       ]
    if( "configuration"     in P_ensure ):
        if( True == ( 'configuration'   in P_list ) ): I_element += [ P_list["configuration"]  ]

    #print " elements: " + str(I_element)
    for prefix in P_prefix:
        for folder in P_folder:
            I_detail =  copy.deepcopy( I_element )
            if( "folder"     in P_ensure ):
                I_detail += [folder]
            #print I_detail
            #print "    " + str(P_ensure) + str(I_detail) + prefix+" "+folder

            #continue;
            for permutation in itertools.permutations( I_detail ):
                variation = [ prefix ]
                variation += permutation
                #print variation

                variable = ""
                for element in variation:
                    variable += element + "_"

                variable = variable.strip( "_" )
                #print variable
                e = os.environ.get( variable )
                if( None != e ):
                    #print variable +" = "+ str( [ e ] )
                    return [ variable, e ]

    return []

def find_ENVIRONMENT_PATH( P_include, P_prefix, P_list ):

    I_decoration = [ "version", "architecture", "folder", "compiler", "configuration" ]

    max = 0;
    I_list = copy.deepcopy( P_list )
    I_list['version'] = ''

    if( False == "version"  in P_list ):
        P_list['version'] = ['']

    for flag in range( 0, 32 ):
        ornament = []
        if ( 0 != ( flag &  1 ) ): ornament += [ I_decoration[ 0 ]];
        if ( 0 != ( flag &  2 ) ): ornament += [ I_decoration[ 1 ]];
        if ( 0 != ( flag &  4 ) ): ornament += [ I_decoration[ 2 ]];
        if ( 0 != ( flag &  8 ) ): ornament += [ I_decoration[ 3 ]];
        if ( 0 != ( flag & 16 ) ): ornament += [ I_decoration[ 4 ]];

        #print ornament

        for version in P_list['version'] :
            I_list['version'] = version
            I_result = find_ENVIRONMENT__generic( P_prefix, I_list, P_include, ornament )
            if( 0 != len( I_result ) ):
                if( max < len( ornament ) ):
                    Ir_result = copy.deepcopy( I_result )
                    max = len( ornament )

    if( 0 == max ):
       print()
       return []
    print( Ir_result[0] + " = " +Ir_result[1] )
    return [ Ir_result[1] ]


def find_ENVIRONMENT_CPPPATH( P_prefix, P_list ):
    sys.stdout.write( '        CPPPATH: ' )

    I_include = { "INCLUDE", "INC",
                              "INCLUDE_PATH", "INC_PATH", "PATH_INC", "PATH_INCLUDE",
                              "INCLUDE_DIR",  "DIR_INCLUDE",
                              "INCLUDE_DIRS", "DIRS_INCLUDE",
                              "INCLUDEDIR", "DIRINCLUDE",
                              "PATH" }

    return find_ENVIRONMENT_PATH( I_include, P_prefix, P_list )


def find_ENVIRONMENT_LIBPATH( P_prefix, P_list ):
    sys.stdout.write('        LIBPATH: ' )

    I_library ={ "LIBRARY", "LIB", "LIBS", "LIBRARIES", "LIBPATH",
                          "LIBRARYPATH",  "LIBRARY_PATH", "LIB_PATH", "LIBS_PATH", "PATH_LIBS", "PATH_LIB",
                          "LIBRARYDIR",   "LIBRARY_DIR",  "LIB_DIR",  "LIBS_DIR",  "DIR_LIBS",  "DIR_LIB",
                          "LIBRARYDIRS",  "LIBRARY_DIRS", "LIB_DIRS", "LIBS_DIRS", "DIRS_LIBS", "DIRS_LIB",
                          "PATH" }

    return find_ENVIRONMENT_PATH( I_library, P_prefix, P_list )
