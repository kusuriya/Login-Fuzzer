#!/usr/bin/env python

import datetime
import sys

class Fuzzer():
    fuzz_set       = None
    start          = None
    end            = None
    target         = None
    
    def __init__(self, i_fuzz_set, min, max, target):
        self.fuzz_set = i_fuzz_set
        self.start = min
        self.end = max
        self.target = target 

    def crack(self):    
        pass
        
    def _recurse(self, width, position, base): 
        for char in fuzz_set[position]:
            self._recurse(width, position + 1, base + "%c" % char)
        target.trypass(base + "%c" % char)
