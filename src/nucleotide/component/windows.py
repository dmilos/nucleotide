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


import function
import nucleotide.direction
import nucleotide.config
import nucleotide.klass
import nucleotide.component.warning


atom_windows_blank = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor' : 'Microsoft',
        'name'   : 'msvc',
        'version': 'X'
    },
    'name' :'blank',
    'config' : {
        'CPPDEFINES'   : ['WIN32', '_WINDOWS' ],
        'CPPFLAGS'     : ['/Zc:forScope'],
        #'LIBS'   : [ 'kernel32.lib', 'user32.lib', 'gdi32.lib', 'winspool.lib', 'comdlg32.lib', 'advapi32.lib', 'shell32.lib', 'ole32.lib', 'oleaut32.lib', 'uuid.lib', 'odbc32.lib', 'odbccp32.lib' ]
    },
    'class': [ 'blank', 'windows:blank' ]
}

atom_windows_unicode = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
    'name' :'encoding:unicode',
    'config' : {
        'CPPDEFINES'   : ['_UNICODE', 'UNICODE' ],
    },
    'class':  [ 'encoding:unicode', 'windows:encoding:unicode' ]
}
def _windows_RTTI_CPPFLAGS( P_data ):
    if( False == P_data.has_key( 'enable ') ):
        return ['/GR']

    if( 'true' == P_data.has_key( 'enable' ) ):
        return ['/GR' ]

    if( 'false' == P_data.has_key( 'enable' ) ):
        return [ '/GR-' ]

    return ['/GR']

atom_windows_RTTI = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
     'config' : {
        'CPPFLAGS'   : _windows_RTTI_CPPFLAGS
    },
    'name' :'RTTI',
    'class':  [ 'RTTI', 'windows:RTTI' ]
}

atom_windows_CompileAs_C = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
     'config' : {
        'CPPFLAGS'   : ['/TC' ],
    },
    'name' :'source:c++',
    'class':  [ 'source:c' ]
}

atom_windows_CompileAs_CPP = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
     'config' : {
        'CPPFLAGS'   : ['/TP' ],
    },
    'name' :'source:c++',
    'class':  [ 'source:c++', 'source:c++11' ]
}


def _windows_configuration_CPPDEFINES( P_data ):
    Ir_list = []

    if( False == P_data.has_key( 'name ') ):
        return Ir_list

    if( 'debug '== P_data[ 'name ' ] ):
        Ir_list += [ '_DEBUG' ]

    if( 'release'== P_data[ 'name ' ] ):
        Ir_list += [ 'NDEBUG' ]
    return Ir_list

def _windows_configuration_CPPFLAGS( P_data ):
    Ir_list = []

    if( False == P_data.has_key( 'name ') ):
        return Ir_list

    if( 'debug '== P_data[ 'name ' ] ):
        Ir_list += [ '/RTC1'  ]

    if( 'release'== P_data[ 'name ' ] ):
        pass
    return Ir_list

def _windows_configuration_LINKFLAGS( P_data ):
    Ir_data = []

    if( False == P_data.has_key( 'name ') ):
        return Ir_data

    if( 'debug '== P_data[ 'name ' ] ):
        Ir_list += [ '/DEBUG' ]

    if( 'release'== P_data[ 'name ' ] ):
        pass

    return Ir_data

# debug   'CPPDEFINES' : [ '_DEBUG' ],
# debug   'CPPFLAGS'   : [ '/RTC1'  ],
# debug   'LINKFLAGS'  : [ '/DEBUG' ]

# release:  'CPPDEFINES'   : [ 'NDEBUG' ],

atom_windows_configuration = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
    'config' : {
        'CPPDEFINES' : _windows_configuration_CPPDEFINES,
        'CPPFLAGS'   : _windows_configuration_CPPFLAGS,
        'LINKFLAGS'  : _windows_configuration_LINKFLAGS
    },
    'name' :'compiler:configuration',
    'class': [ 'compiler:configuration', 'windows:compiler:configuration' ]
}

atom_windows_exe_console = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
     'config' : {
           'CPPDEFINES'  : ['_CONSOLE' ],
            'LINKFLAGS'   : [ '/SUBSYSTEM:CONSOLE' ]
    },
    'name' : 'executable:console' ,
    'class': [  'executable:console'  ]
}

atom_windows_exe_UI = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
    'config' : {
            'CPPDEFINES'  : ['TODO' ],
            'LINKFLAGS'   : [ '/SUBSYSTEM:WINDOWS' ]
    },
    'name' : 'executable:UI',
    'class': [ 'executable:UI' ]
}

atom_windows_shared_library = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
    'config' : {
        'CPPDEFINES'  : ['_USRDLL', '_WINDLL' ],
        'LINKFLAGS'   : [ '/DLL', '/SUBSYSTEM:WINDOWS' ]
    },
    'name' :'dll',
    'class':  [ 'shared:library' ]
}

atom_windows_shared_object = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
     'config' : {
        'CPPDEFINES'  : ['_LIB' ],
    },
    'name' :'lib',
    'class': [  'shared:object' ]
}

def _windows_RTL_CPPFLAGS( P_data ):
    I_flag = 'M'

    if( 'dynamic' == P_data['type'] ):
       I_flag += 'D'
    if( 'static' == P_data['type'] ):
       I_flag += 'T'

    if( True == P_data.has_key( 'configuration' ) ):
        if( 'debug' == P_data['configuration'] ):
           I_flag += 'd'
        if( 'release' == P_data['configuration'] ):
           pass

    return [ '/' + I_flag ]

atom_windows_RTL= {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
    'config' : {
        'CPPFLAGS'  : _windows_RTL_CPPFLAGS
    },
    'name' :'RTL',
    'class':  [ 'RTL', 'windows:RTL' ]
}

def _windows_PDB_CPPFLAGS( P_data ):
    Ir_list = []

    if( True == P_data.has_key( 'configuration' ) ):
        if( 'debug' == P_data[ 'configuration' ] ):
           Ir_list.append( '/ZI' )
        if( 'release' == P_data[ 'configuration' ] ):
           Ir_list.append( '/Zi' )

    if( True == P_data.has_key( 'synchronous' ) ):
        if( 'true' == P_data[ 'synchronous' ] ):
           Ir_list.append( '/FS' )

    if( True == P_data.has_key( 'file-name-compile' ) ):
        Ir_list.append( '/Fd"' + P_data['file-name-compile'] + '"' )
    else:
        if( True == P_data.has_key( 'file-name' ) ):
            Ir_list.append( '/Fd"' + P_data['file-name'] + '"' )

    return Ir_list

def _windows_PDB_LINKFLAGS( P_data ):
    Ir_list = []
    if( True == P_data.has_key( 'configuration' ) ):
        if( 'debug' == P_data['configuration'] ):
           Ir_list.append( '/DEBUG' )
        if( 'release' == P_data['configuration'] ):
           Ir_list.append( '/DEBUG' )

    if( True == P_data.has_key( 'file-name-executable' ) ):
        Ir_list.append( '/PDB:"' + P_data['file-name-executable'] + '"' )
    else:
        if( True == P_data.has_key( 'file-name' ) ):
            Ir_list.append( '/PDB:"' + P_data['file-name'] + '"' )

    return Ir_list

atom_windows_PDB = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
    'config' : {
        'CPPFLAGS'  : _windows_PDB_CPPFLAGS,
        'LINKFLAGS' : _windows_PDB_LINKFLAGS,
    },
    'name' : 'PDB',
    'class': [  'PDB', 'windows:PDB' ]
}

atom_windows_exception = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
    'config' : {
        'CPPFLAGS'  : ['/EHsc' ],
    },
    'name' : 'exception',
    'class': [ 'exception' ]
}

def _windows_optimisation_CPPFLAGS( P_data ):
    Ir_list = []
    if( True == P_data.has_key( 'configuration' ) ):
        if( 'debug' == P_data['configuration'] ):
           Ir_list.append( '/Od' )
        if( 'release' == P_data['configuration'] ):
           Ir_list.append( '/O2' )

    return Ir_list

atom_windows_optimisation = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
    'config' : {
        'CPPFLAGS'  : _windows_optimisation_CPPFLAGS,
    },
    'name' : 'release-optimisation',
    'class': [ 'compiler:optimisation', 'windows:compiler:configuration' ]
}

atom_windows_pp2f = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
    'config' : {
        'CPPFLAGS'  : ['/P' ],
    },
    'name' : 'pp2f',
    'class':  [ 'pp2f', 'windows:pp2f' ]
}

def _windows_architecture_TARGET_ARCH( P_data ):
    if( False == P_data.has_key( 'name' ) ):
        return ''
    return P_data[ 'name' ]

atom_windows_architecture= {
    'platform' : {
        'host'  : 'X',
        'guest' : 'X'
    },
    'cc' : {
        'vendor': 'X',
        'name': 'X',
        'version': 'X'
    },
    'config' : {
        'TARGET_ARCH' : _windows_architecture_TARGET_ARCH
    },
    'name' :'architecture',
    'class':  [ 'architecture' ]
}

def _windows_compiler_warning_CPPFLAGS( P_list ):
    Ir_list= []
    I_direction = nucleotide.direction.Direction( {'host'  : 'Windows','guest' : 'Windows'}, P_cc = { 'vendor': 'Microsoft', 'name': 'msvc', 'version': 'X'} )

    return nucleotide.component.warning.util.list( P_list, I_direction )

atom_windows_compiler_warning = {
    'platform' : {
        'host'  : 'Windows',
        'guest' : 'Windows'
    },
    'cc' : {
        'vendor': 'Microsoft',
        'name': 'msvc',
        'version': 'X'
    },
    'config' : {
        'CPPFLAGS' : _windows_compiler_warning_CPPFLAGS
    },
    'name' :'compiler:warning',
    'class':  [ 'compiler:warning', 'windows:compiler:warning' ]
}


def init( P_option ) :
    function.extend( P_option, 'window:blank', atom_windows_blank )

    function.extend( P_option, 'window:encoding:unicode',   atom_windows_unicode)

    function.extend( P_option, 'window:c',              atom_windows_CompileAs_C    )
    function.extend( P_option, 'window:c++',            atom_windows_CompileAs_CPP  )
   #function.extend( P_option, 'window:c++11',          atom_windows_CompileAs_CPP  )
   #function.extend( P_option, 'window:c++:dialekt',    atom_windows_CompileAs_CPP_dialekt )

    function.extend( P_option, 'window:compiler:warning',          atom_windows_compiler_warning )
    function.extend( P_option, 'window:compiler:configuration',    atom_windows_configuration )
    function.extend( P_option, 'window:compiler:optimisation',     atom_windows_optimisation )

    function.extend( P_option, 'window:executable:console',  atom_windows_exe_console)
    function.extend( P_option, 'window:executable:UI',       atom_windows_exe_UI)

    function.extend( P_option, 'window:shared:library', atom_windows_shared_library)
    function.extend( P_option, 'window:shared:object',  atom_windows_shared_object)

    function.extend( P_option, 'window:RTTI', atom_windows_RTTI)
    function.extend( P_option, 'window:RTL',  atom_windows_RTL )
    function.extend( P_option, 'window:PDB',  atom_windows_PDB )

    function.extend( P_option, 'window:exception',    atom_windows_exception)

    function.extend( P_option, 'window:pp2f',   atom_windows_pp2f    )

    function.extend( P_option, 'window:architecture',        atom_windows_architecture )

   #function.extend( P_option, 'window:linker:warning',      atom_windows_linker_warning )
   #function.extend( P_option, 'window:linker:optimisation', atom_windows_linker_warning )


def check():
    pass


