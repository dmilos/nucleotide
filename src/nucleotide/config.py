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



# Scons Native thing only. Stored in (key,data) format
class Config:
    m_native = None

    def __init__( self, P_data = {} ):
        self.m_native = {
            #'TARGET_ARCH' : 'x86', #<purposely omit this key
            #'MSVC_VERSION': '12',  #<purposely omit this key
            #'CC'          : '',    #<purposely omit this key
            #'CXX'         : '',    #<purposely omit this key
            #'LINK'        : '',    #<purposely omit this key
            'CPPFLAGS'     : [],
            'CPPPATH'      : [],
            'CPPDEFINES'   : [],
            'LIBPATH'      : [],
            'LIBS'         : [],
            'LINKFLAGS'    : [],
        }

        #print( 'Config::__init__( P_data = ' + str( P_data ) + ' )' )

        if( True == ( 'CPPFLAGS'     in P_data ) ): self.m_native[ 'CPPFLAGS'   ] = P_data[ 'CPPFLAGS'  ]
        if( True == ( 'CPPPATH'      in P_data ) ): self.m_native[ 'CPPPATH'    ] = P_data[ 'CPPPATH'   ]
        if( True == ( 'CPPDEFINES'   in P_data ) ): self.m_native[ 'CPPDEFINES' ] = P_data[ 'CPPDEFINES']
        if( True == ( 'LIBPATH'      in P_data ) ): self.m_native[ 'LIBPATH'    ] = P_data[ 'LIBPATH'   ]
        if( True == ( 'LIBS'         in P_data ) ): self.m_native[ 'LIBS'       ] = P_data[ 'LIBS'      ]
        if( True == ( 'LINKFLAGS'    in P_data ) ): self.m_native[ 'LINKFLAGS'  ] = P_data[ 'LINKFLAGS' ]
        if( True == ( 'TARGET_ARCH'  in P_data ) ): self.m_native[ 'TARGET_ARCH'  ] = P_data[ 'TARGET_ARCH'  ]
        if( True == ( 'MSVC_VERSION' in P_data ) ): self.m_native[ 'MSVC_VERSION' ] = P_data[ 'MSVC_VERSION' ]
        if( True == ( 'CC'           in P_data ) ): self.m_native[ 'CC'   ] = P_data[ 'CC'   ]
        if( True == ( 'CXX'          in P_data ) ): self.m_native[ 'CXX'  ] = P_data[ 'CXX'  ]
        if( True == ( 'LINK'         in P_data ) ): self.m_native[ 'LINK' ] = P_data[ 'LINK' ]


    def get_native( self ):
        return self.m_native

    def get( self, P_name ):
        return self.m_native[ P_name ]

    def exists( self, P_name ):
        return True == ( P_name in self.m_native )

    def set( self, P_name, P_value ):
        self.m_native[P_name] = P_value

    def append( self, P_name, P_list ):
        #print( P_name + " + " + str(P_list) )
        self.m_native[P_name] += P_list

    ## Take all from other config by respecting P_param
    def accumulate( self, P_config, P_param = {} ):

        #print( 'Config::accumulate::P_config.m_native = ' + str( P_config.m_native ) )

        self._process_list( P_config.get_native(), 'CPPFLAGS'  , P_param )
        self._process_list( P_config.get_native(), 'CPPPATH'   , P_param )
        self._process_list( P_config.get_native(), 'CPPDEFINES', P_param )
        self._process_list( P_config.get_native(), 'LIBPATH'   , P_param )
        self._process_list( P_config.get_native(), 'LIBS'      , P_param )
        self._process_list( P_config.get_native(), 'LINKFLAGS' , P_param )

        self._process_value( P_config.get_native(), 'TARGET_ARCH' , P_param )
        self._process_value( P_config.get_native(), 'MSVC_VERSION' , P_param )

        self._process_value( P_config.get_native(), 'CC'   , P_param )
        self._process_value( P_config.get_native(), 'CXX'  , P_param )
        self._process_value( P_config.get_native(), 'LINK' , P_param )

        #print( 'Config::accumulate::self.m_native = ' + str( self.m_native ) )

    def _process_value( self, P_data, P_key, P_param={} ):
        if( False == ( P_key in P_data ) ):
            return;

        if( False ==  self.exists( P_key ) ):
            self.set( P_key, '' )

        if( True == hasattr( P_data[P_key], '__call__' ) ):
            self.set( P_key, P_data[P_key]( P_param ) );
            return

        self.set(  P_key, P_data[ P_key ] )

    def _process_list( self, P_data, P_key, P_param={} ):
        #print( P_data )
        if( False == ( P_key in P_data ) ):
            return;
        #print( P_key )

        if( False ==  self.exists( P_key ) ):
            self.set( P_key, [] )

        if( True == hasattr( P_data[P_key], '__call__' ) ):
            self.append( P_key, P_data[P_key]( P_param ) );
            return

        self.append( P_key, P_data[ P_key ] );
