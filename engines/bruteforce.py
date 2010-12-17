#!/usr/bin/env python

import datetime
import sys
from fuzzer import Fuzzer

UPPER   = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER   = 'abcdefghijklmnopqrstuvwxyz'
NUM     = '0123456789'
SPECIAL = '`~@#$%^&*()_+=[]{}\|\'"/><'
PUNC    = '.?!,;:'

class Bruteforcer(Fuzzer):
    """
    Brute force engine. Extension of fuzzer.
    """
    
    
    
    def __init__(self, start, end, target, upper = False, lower = False, 
                 num = False, special = False, punc = False):
        self.start  = start
        self.end    = end
        self.target = target
        self.fuzz_set   = [ ]
    