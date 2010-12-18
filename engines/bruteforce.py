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

    def set_target(self, target):
        self.target = target

def selector( ):
    upper       = False
    lower       = False
    num         = False
    special     = False
    punc        = False
    
    upper   = 'y' == raw_input('Use uppercase characters (y/n)? ').lower()[0]
    lower   = 'y' == raw_input('Use lowercase characters (y/n)? ').lower()[0]
    num     = 'y' == raw_input('Use numbers (y/n)? ').lower()[0]
    special = 'y' == raw_input('Use special characters (y/n)? ').lower()[0]
    punc    = 'y' == raw_input('Use punctuation (y/n)? ').lower()[0]
    
    start   = raw_input('Start with how many characters? ')
    if not start.isdigit():
        print 'expected a numeric value...'
        return None
    else:
        start   = int(start)
    
    end     = raw_input('End at how many characters? ')
    if not end.isdigit():
        print 'expected a numeric value...'
        return None
    elif int(end) < start:
        print 'end should be greater than or equal to start!'
        return None
    else:
        end     = int(end)
    
    return Bruteforcer(start, end, None, upper, lower, num, special, punc)