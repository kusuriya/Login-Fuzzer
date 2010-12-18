#!/usr/bin/env python

import itertools

class Fuzzer():
    fuzz_set       = None
    start          = None
    end            = None
    target         = None
    password       = None
    
    def __init__(self, i_fuzz_set, start, end, target):
        self.fuzz_set = i_fuzz_set
        self.start = start
        self.end = end
        self.target = target 

    def crack(self):
        for i in range(self.start, self.end + 1):
            fuzz_set = self.fuzz_set[:i + 1]

            for j in itertools.product(*fuzz_set):
                password = ''.join(j)
                if self.target.trypass(password):
                    print "MATCH:", password
                    return password

        