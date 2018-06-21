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
import sys
import platform

import nucleotide
import nucleotide.component
import nucleotide.component._common
import nucleotide.component._common.blank
import nucleotide.component._common.architecture
import nucleotide.component._common.include
import nucleotide.component._common.library


## Ddetect existing translators
class Translator:
    m_list = None

    def __init__(self):
       self.m_list = []
       pass

    @staticmethod
    def extend(P_options):
        nucleotide.component._common.blank.Blank.extend( P_options )
        nucleotide.component._common.architecture.Architecture.extend( P_options )
        nucleotide.component._common.include.Include.extend( P_options )
        nucleotide.component._common.library.Library.extend( P_options )

    @staticmethod
    def platform():
        return platform.system()

    def get(self):
        return self.m_list
