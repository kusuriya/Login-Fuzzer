#!/usr/bin/env python

import datetime
import sys

class Fuzzer():
    fuzz_set       = None
    start          = None
    end            = None
    target         = None
    password       = None
    
    def __init__(self, i_fuzz_set, min, max, target):
        self.fuzz_set = i_fuzz_set
        self.start = min
        self.end = max
        self.target = target 

    def crack(self):    
        for width in range(self.start, self.end + 1):
            if self.password or self._recurse(width, 0, ""):
                return self.password
        
    def _recurse(self, width, position, base): 
        for char in self.fuzz_set[position]:
                if (position < width - 1):
                    if self._recurse(width, position + 1, base + "%c" % char):
                        return True
        if self.target.trypass(base + "%c" % char):
            self.password = base + "%c" % char
            return True

