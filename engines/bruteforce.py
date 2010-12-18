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
    
    Constructor parameters:
        start   - start with n characters
        end     - end with n characters
        target  - interface target
        upper   - use uppercase characters
        lower   - use lowercase characters
        num     - use numbers
        special - use special characters
        punc    - use punctuation characters
    """
    
    def __init__(self, start, end, target, upper = False, lower = False, 
                 num = False, special = False, punc = False):
        self.start  = start
        self.end    = end
        self.target = target
        self.fuzz_set   = [ ]
    
        for i in range(end):
            charset = ""
            if upper:   charset += UPPER
            if lower:   charset += LOWER
            if num:     charset += NUM
            if special: charset += SPECIAL
            if punc:    charset += PUNC
        
            self.fuzz_set.append(charset)
