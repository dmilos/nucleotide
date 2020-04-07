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


TABLE = {
    'misleading-indentation'                : {
            'X-X-FSF-gcc-X': 'misleading-indentation'
        },
    'unused-variable'                       : {
            'X-X-FSF-gcc-X'                   : 'unused-variable',
            'Windows-Windows-Microsoft-msvc-X': '4101'
        },
    'unused-variable-but-set'               : {
            'X-X-FSF-gcc-X'                   : 'unused-but-set-variable',
            'Windows-Windows-Microsoft-msvc-X': '4189'
        },
    'unused-local-typedefs'                 : {
            'X-X-FSF-gcc-X'                   :  'unused-local-typedefs',
            'Windows-Windows-Microsoft-msvc-X': '4901'
        },
    'unused-formal-parameter'               : {
            'Windows-Windows-Microsoft-msvc-X': '4100'
        },
    'unused-code':{
            'Windows-Windows-Microsoft-msvc-X': '4702'
        },

     'member-uninitialized'           : {
            #'X-X-FSF-gcc-X': 'TODO'
            #'Windows-Windows-Microsoft-msvc-X': 'TODO'
        },

    'member-order-initialization'           : {
            'X-X-FSF-gcc-X': 'reorder',
            'Windows-Windows-Microsoft-msvc-X': '5038'
        },

    'return-no-return-statement'            : {
            'X-X-FSF-gcc-X': 'return-type'
        },
    'return-address-of-local-variable': {
            'Windows-Windows-Microsoft-msvc-X': '4172',
            'X-X-FSF-gcc-X'                   : 'return-local-addr'
        },

    'uninitialized-variable'                : {
            'X-X-FSF-gcc-X': 'uninitialized'
        },
    'uninitialized-using-of-variable' : {
            'Windows-Windows-Microsoft-msvc-X': '4700',
            'X-X-FSF-gcc-X'                   : 'uninitialized'
        },

    'base-class-destructor-is-inaccessible' : {
            'Windows-Windows-Microsoft-msvc-X': '4624'
        },

    'conversion-comparation' : {
        'Windows-Windows-Microsoft-msvc-X': [ '4388', '4018' ],
        'linux-gcc'                       : 'sign-compare',
        'X-X-FSF-gcc-X'                   : 'sign-compare'
        },

    'conversion-data-loss' : {
        'Windows-Windows-Microsoft-msvc-X': '4242'
        },

    'conversion-force-to-bool' : {
        'Windows-Windows-Microsoft-msvc-X': '4800'
        },

    'enumerator-not-explicitly-handled' : {
        'Windows-Windows-Microsoft-msvc-X': '4601'
        },
    'enumerator-not-handled' : {
        'Windows-Windows-Microsoft-msvc-X': '4602'
        },

    'this-in-initializer-list' : {
        'Windows-Windows-Microsoft-msvc-X': '4355'
        },

    'macro-not-enought-parameter' : {
        'Windows-Windows-Microsoft-msvc-X': '4003'
        },
    'macro-redfinition' : {
        'Windows-Windows-Microsoft-msvc-X': '4005'
        },

    'decorated-name-length-exceeded' : {
        'Windows-Windows-Microsoft-msvc-X': '4503'
    },

    'assignment-within-conditional-expression': {
        'Windows-Windows-Microsoft-msvc-X': '4706',
        'X-X-FSF-gcc-X'                   : 'sign-compare'
    },

    'variable-shadow-variable' : {
    'linux-gcc': 'shadow'
    }

}
