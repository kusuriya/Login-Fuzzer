#!/usr/bin/env python
"""

"""

from interfaces.echo import echo
from engines.fuzzer import Fuzzer

fuzz_set = [ ['t', 'T'], ['e', 'E'], ['s', 'S'], ['t', 'T'], ['i', 'I'], ['n', 'N'], ['g', 'G'] ]
target = echo('TeStInG')
fuzzer = Fuzzer(fuzz_set, 6, 8, target)
print fuzzer.crack()