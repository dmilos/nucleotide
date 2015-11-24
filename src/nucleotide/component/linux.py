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


atom_linux_blank = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'name' :'blank',
    'config' : {
        #'CPPDEFINES'  : ['_BLANK' ],
        #'LIBS'        : [ 'libc.lib', 'libcpp', 'lmath', 'lptrehread' ]
    },
    'class': [ 'blank', 'linux:blank' ]
}

atom_linux_unicode = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'name' :'unicode',
    'config' : {
        #'CPPDEFINES'   : ['_UNICODE', 'UNICODE' ],
    },
    'class':  [ 'encoding:unicode', 'linux:encoding:unicode' ]
}

option_linux_CompileAs_Cpp11 = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
     'config' : {
        'CPPFLAGS'   : ['-std=c++11' ],
    },
    'name' :'source:c++11',
    'class':  [ 'source:c++11', 'linux:source:c++11' ]
}

def _linux_CompileAs_CPP_CPPFLAGS( P_data ):
    if( False == P_data.has_key( 'dialekt' ) ):
        return [ '' ]

    return [ '-std=' + P_data['dialekt'] ]

option_linux_CompileAs_CPP_dialekt = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor': 'FSF',
        'name': 'gcc',
        'version': 'X'
    },
     'config' : {
        'CPPFLAGS'   : _linux_CompileAs_CPP_CPPFLAGS
    },
    'name' :'source:c++:dialekt',
    'class':  [ 'source:c++', 'source:c++:dialekt' ,'linux:source:c++:dialekt'  ]
}

def _linux_RTTI_CPPFLAGS( P_data ):
    if( False == P_data.has_key( 'enable' ) ):
        return [ '' ]

    if( 'true' == P_data.has_key( 'enable' ) ):
        return [ '' ]

    if( 'false' == P_data.has_key( 'enable' ) ):
        return [ '-fno-rtti' ]

    return [ '' ]

atom_linux_RTTI = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
     'config' : {
        'CPPFLAGS'   : _linux_RTTI_CPPFLAGS
    },
    'name' :'RTTI',
    'class':  [ 'RTTI', 'linux:RTTI' ]
}

atom_linux_debug = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
        'CPPDEFINES' : ['_DEBUG'],
        'CPPFLAGS'   : ['/TODO' ],
        'LINKFLAGS'  : [ '/DEBUG']
    },
    'name' :'debug',
    'class': [  'debug', 'linux:debug' ]
}

atom_linux_release = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
            'CPPDEFINES'   : [ 'NDEBUG' ],
    },
    'name' :'release',
    'class':  [ 'release' , 'linux:release' ]
}

atom_linux_exe_console = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
     'config' : {
           'CPPDEFINES'  : ['_TODO' ],
            'LINKFLAGS'   : [ '/TODO' ]
    },
    'name' : function.join_in2( 'exe', 'console'  ) ,
    'class': [ 'executable:console', 'linux:executable:console' ]
}

atom_linux_exe_UI = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
            'CPPDEFINES'  : ['TODO' ],
            'LINKFLAGS'   : [ '/TODO' ]
    },
    'name' : function.join_in2( 'exe', 'win' ),
    'class': [ 'executable:UI', 'linux:executable:UI' ]
}

atom_linux_shared_library = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
            'CPPDEFINES'  : ['TODO' ],
            'LINKFLAGS'   : [ '/TODO' ]
    },
    'name' :'dll',
    'class':  [ 'executable:shared_object', 'linux:executable:shared_object' ]
}

atom_linux_shared_object = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor': 'FSF',
        'name': 'gcc',
        'version': 'X'
    },
     'config' : {
           'CPPDEFINES'  : ['_LIB' ],
    },
    'name' :'lib',
    'class': [  function.join_out2( 'nucleotide', function.join_in2( 'shared', 'library'  )   )  ]
}


def _linux_RTL_LINKFLAGS( P_data ):
    I_flag = ''
 
    #if( 'dynamic' == P_data['type'] ):
    #   I_flag += 'D'
    if( 'static' == P_data['type'] ):
       I_flag += '-static'
    return [ I_flag ]

atom_linux_RTL = {
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
        'LINKFLAGS'  : _linux_RTL_LINKFLAGS
    },
    'name' :'RTL',
    'class':  [ 'RTL', 'linux:RTL' ]
}

def _linux_PDB_CPPFLAGS( P_data ):
    Ir_list = []

    if( True == P_data.has_key( 'configuration' ) ):
        if( 'debug' == P_data[ 'configuration' ] ):
           Ir_list.append( 'TODO' )
        if( 'release' == P_data[ 'configuration' ] ):
           Ir_list.append( 'TODO' )

    if( True == P_data.has_key( 'synchronous' ) ):
        if( 'true' == P_data[ 'synchronous' ] ):
           Ir_list.append( 'TODO' )

    if( True == P_data.has_key( 'file-name-compile' ) ):
        Ir_list.append( 'TODO"' + P_data['file-name-compile'] + '"' )
    else:
        if( True == P_data.has_key( 'file-name' ) ):
            Ir_list.append( 'TODO"' + P_data['file-name'] + '"' )

    return Ir_list

def _linux_PDB_LINKFLAGS( P_data ):
    Ir_list = []
    if( True == P_data.has_key( 'configuration' ) ):
        if( 'debug' == P_data['configuration'] ):
           Ir_list.append( 'TODO' )
        if( 'release' == P_data['configuration'] ):
           Ir_list.append( 'TODO' )

    if( True == P_data.has_key( 'file-name-executable' ) ):
        Ir_list.append( 'TODO"' + P_data['file-name-executable'] + '"' )
    else:
        if( True == P_data.has_key( 'file-name' ) ):
            Ir_list.append( 'TODO"' + P_data['file-name'] + '"' )

    return Ir_list

atom_linux_PDB = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
        'CPPFLAGS'  : _linux_PDB_CPPFLAGS,
        'LINKFLAGS' : _linux_PDB_LINKFLAGS,
    },
    'name' : 'PDB',
    'class': [  'PDB', 'linux:PDB' ]
}
atom_linux_exception = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
            'CPPFLAGS'  : ['-fexceptions' ],
    },
    'name' : 'exception',
    'class': [  'exception', 'linux:exception' ]
}

atom_linux_release_optimisation = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
            'CPPFLAGS'  : ['/O2' ],
    },
    'name' : 'release-optimisation',
    'class':  [ function.join_out2( 'nucleotide', 'release-optimisation'  )   ]
}

atom_linux_debug_optimisation = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
            'CPPFLAGS'  : ['/Od' ],
    },
    'name' : 'debug-optimisation',
    'class':  [ function.join_out2( 'nucleotide', 'debug-optimisation'  ) ]
}

atom_linux_pp2f = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
            'CPPFLAGS'  : ['-E' ],
    },
    'name' : 'pp2f',
    'class':  [ 'pp2f', 'linux:pp2f' ]
}

def _linux_compiler_warning_CPPFLAGS( P_list ):
    Ir_list= []
    I_direction = nucleotide.direction.Direction( {'host'  : 'Linux','guest' : 'Linux'}, P_cc = { 'vendor': 'FSF', 'name': 'gcc', 'version': 'X'} )

    return nucleotide.component.warning.util.list( P_list, I_direction )

atom_linux_compiler_warning = {
    'platform' : {
        'host'  : 'Linux',
        'guest' : 'Linux'
    },
    'cc' : {
        'vendor' : 'FSF',
        'name'   : 'gcc',
        'version': 'X'
    },
    'config' : {
        'CPPFLAGS' : _linux_compiler_warning_CPPFLAGS
    },
    'name' :'compiler:warning',
    'class':  [ 'compiler:warning', 'linux:compiler:warning' ]
}


def init( P_option ) :
    function.extend( P_option, 'blank',               atom_linux_blank)
   #function.extend( P_option, 'architecture',        atom_linux_architecture )

   #function.extend( P_option, 'source:c',             option_linux_CompileAs_C_strait )
   #function.extend( P_option, 'source:c++',           option_linux_CompileAs_CPP_strait)
    function.extend( P_option, 'linux:source:c++11',         option_linux_CompileAs_Cpp11 )
    function.extend( P_option, 'linux:source:c++:dialekt',   option_linux_CompileAs_CPP_dialekt )

    function.extend( P_option, 'linux:RTTI',                atom_linux_RTTI)
    function.extend( P_option, 'linux:RTL',                 atom_linux_RTL )
    function.extend( P_option, 'linux:PDB',                 atom_linux_PDB )
    function.extend( P_option, 'linux:pp2f',                atom_linux_pp2f    )

    function.extend( P_option, 'linux:encoding:unicode',      atom_linux_unicode    )
    function.extend( P_option, 'linux:debug',                 atom_linux_debug      )
    function.extend( P_option, 'linux:release',               atom_linux_release    )

    function.extend( P_option, 'linux:executable:console',    atom_linux_exe_console)
    function.extend( P_option, 'linux:executable:UI',         atom_linux_exe_UI)

    function.extend( P_option, 'linux:shared_library',        atom_linux_shared_library)
    function.extend( P_option, 'linux:shared_object',         atom_linux_shared_object)
    #function.extend( P_option, 'linux:static_release',        atom_linux_static_release)
    function.extend( P_option, 'linux:exception',             atom_linux_exception)

    function.extend( P_option, 'linux:release_optimisation',  atom_linux_release_optimisation)
    function.extend( P_option, 'linux:debug_optimisation',    atom_linux_debug_optimisation)

    function.extend( P_option, 'linux:compiler:warning',  atom_linux_compiler_warning )
   #function.extend( P_option, 'linux:linker:warning',    atom_linux_linker_warning )
   #function.extend( P_option, 'linux:compiler:feature:for-scope',  atom_linux_compiler_warning )   -ffor-scope

def check():
    pass

