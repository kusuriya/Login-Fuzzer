#!/usr/bin/env python
"""
Test harness to test fuzzer. Uses echo interface to visualize the output and
verify the fuzzer.
"""

from interfaces.echo import echo
from engines.fuzzer import Fuzzer

fuzz_set = [ ['t', 'T'], ['e', 'E', '3' ], ['s', 'S'], ['t', 'T'], ['i', 'I'], ['n', 'N'], ['g', 'G'], ['!', '#', '$'] ]
password = 'T3StInG#'
target = echo(password)

min = len(password)
max = len(password)

if len(fuzz_set) < len(password):
    print '*** warning fuzz_set and target mismatch!'

fuzzer = Fuzzer(fuzz_set, min, max, target)
print fuzzer.crack()