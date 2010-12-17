#!/usr/bin/env python
"""
Test code to test SSH engine using fuzzer. 
"""

from engines.fuzzer import Fuzzer
from interfaces.ssh import ssh

fuzz_set = [
                ['C', 'c'],
                ['R', 'r'],
                ['A', 'a', '4'],
                ['C', 'c'],
                ['K', 'k'],
                ['T', 't'],
                ['H', 'h'],
                ['I', 'i', '1'],
                ['S', 's'],
                ['P', 'p'],
                ['A', 'a', '4'],
                ['S', 's', '5'],
                ['S', 's', '5'],
                ['!', '@', '#', '$']
]

min = len(fuzz_set)
max = len(fuzz_set)

host = 'localhost'
user = 'crackme'

target = ssh((host, user))
fuzzer = Fuzzer(fuzz_set, min, max, target)
print fuzzer.crack()