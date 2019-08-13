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


import SCons.Script

## Create Scons Environment from accumulated atoms from the given settings
class Environment:

    M_native = None

    def __init__( self, P_settings ):

        #print( 'Environment::P_settings.get_config().m_native: ' + str( P_settings.get_config().m_native ) )

        I_init = {}

        if( True == P_settings.get_config().exists( 'TARGET_ARCH' ) ):
            #print( 'TARGET_ARCH: -|' + str( P_settings.get_config().get( 'TARGET_ARCH'  ) ) + '|-' )
            I_init[ 'TARGET_ARCH' ] = P_settings.get_config().get( 'TARGET_ARCH' )

        if( True == P_settings.get_config().exists( 'MSVC_VERSION' ) ):
            if( None != P_settings.get_config().get( 'MSVC_VERSION' ) ):
            #print( 'MSVC_VERSION: -|' + str( P_settings.get_config().get( 'MSVC_VERSION'  ) ) + '|-' )
                I_init[ 'MSVC_VERSION' ] = P_settings.get_config().get( 'MSVC_VERSION' )

        if( True == P_settings.get_config().exists( 'tools' ) ):
            if( None != P_settings.get_config().get( 'tools' ) ):
            #print( 'MSVC_VERSION: -|' + str( P_settings.get_config().get( 'MSVC_VERSION'  ) ) + '|-' )
                I_init[ 'tools' ] = P_settings.get_config().get( 'tools' )

        self.M_native = SCons.Script.Environment( **I_init )

        if( P_settings.get_config().exists( 'CPPFLAGS'   ) ): self.M_native.Append( CPPFLAGS    = P_settings.get_config().get( 'CPPFLAGS'  ) )
        if( P_settings.get_config().exists( 'CPPPATH'    ) ): self.M_native.Append( CPPPATH     = P_settings.get_config().get( 'CPPPATH'   ) )
        if( P_settings.get_config().exists( 'CPPDEFINES' ) ): self.M_native.Append( CPPDEFINES  = P_settings.get_config().get( 'CPPDEFINES') )
        if( P_settings.get_config().exists( 'LIBPATH'    ) ): self.M_native.Append( LIBPATH     = P_settings.get_config().get( 'LIBPATH'   ) )
        if( P_settings.get_config().exists( 'LIBS'       ) ): self.M_native.Append( LIBS        = P_settings.get_config().get( 'LIBS'      ) )
        if( P_settings.get_config().exists( 'LINKFLAGS'  ) ): self.M_native.Append( LINKFLAGS   = P_settings.get_config().get( 'LINKFLAGS' ) )

        if( True == P_settings.get_config().exists( 'CC'   ) ) and ( None != P_settings.get_config().get( 'CC'   ) ): self.M_native.Replace( CC   = P_settings.get_config().get( 'CC'   ) )
        if( True == P_settings.get_config().exists( 'CXX'  ) ) and ( None != P_settings.get_config().get( 'CXX'  ) ): self.M_native.Replace( CXX  = P_settings.get_config().get( 'CXX'  ) )
        if( True == P_settings.get_config().exists( 'LINK' ) ) and ( None != P_settings.get_config().get( 'LINK' ) ): self.M_native.Replace( LINK = P_settings.get_config().get( 'LINK' ) )

        #print ( P_settings.get_config().get( 'CPPFLAGS'  )  )
        #print ( P_settings.get_config().get( 'CPPPATH'  )   )
        #print ( P_settings.get_config().get( 'CPPDEFINES'   )
        #print ( P_settings.get_config().get( 'LIBPATH'  )   )
        #print ( P_settings.get_config().get( 'LIBS'  )      )
        #print ( P_settings.get_config().get( 'LINKFLAGS'  ) )

    def native( self ):
        return self.M_native
