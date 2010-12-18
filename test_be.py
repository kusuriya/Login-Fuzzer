#!/usr/bin/env python
"""
Test harness to test bruteforcer. Uses echo interface to visualize the output 
and verify the bruteforcer.
"""

from interfaces.echo import echo
from engines.bruteforce import Bruteforcer

password = ':fO0!'
target = echo(password)

min = len(password) - 2
max = len(password) + 1

brute = Bruteforcer(min, max, target, upper = True, lower = True, num = True,
                special = True, punc = True)
print brute.crack()
