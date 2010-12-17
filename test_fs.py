#!/usr/bin/env python
"""
Test code to test SSH engine using fuzzer. 
"""

from engines.fuzzer import Fuzzer
from interfaces.ssh import ssh

fuzz_set = [ 'Cc', 'Rr', 'Aa4', 'Cc', 'Kk', 'Tt', 'Hh', 'Ii1', 'Ss', 'Pp',
             'Aa4', 'Ss5', 'Ss5', '!@#$' ]

min = len(fuzz_set)
max = len(fuzz_set)

host = 'localhost'
user = 'crackme'

target = ssh((host, user))
fuzzer = Fuzzer(fuzz_set, min, max, target)
print fuzzer.crack()