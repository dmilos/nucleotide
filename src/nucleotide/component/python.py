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

#              dddhgb     nnnnnnnnnnjjh                                        f                          


import os

import pythonX

def init( P_option ) :
    pythonX.common.init( P_option )
    pythonX.linux.init( P_option )
    pythonX.windows.init( P_option )


def check():

    pythonX.common.check()
    pythonX.linux.check()
    pythonX.windows.check()

if '__main__' == __name__:
    import nucleotide.Option
    I_option = universa.Option()
    init( I_option )
    print I_option
    print '-----------------'
    print I_class

