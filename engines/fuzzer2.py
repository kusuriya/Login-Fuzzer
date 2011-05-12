#!/usr/bin/env python
"""
New password generation backend, suggested by Evan.
"""

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

    def set_target(self, target):

        self.target = target
        
    def create_map(self):
        map = [ ]
        for i in range(self.start, self.end + 1):
            fuzz_set = self.fuzz_set[:i + 1]
            
            for j in itertools.product(*fuzz_set):
                password    = ''.join(j)
                map.append(password)
        
        return map

def selector( ):
    in_str      = "NOT_NULL"
    fuzz_set    = [ ]
    i           = 0
    
    print "Enter characters for fuzz_set[%d] as a string sequence, empty " % i
    print "line to end."    
    while in_str:
        in_str = raw_input('\tstring for position' + str(i) + ': ')
        
        if in_str:
            fuzz_set.append(in_str)
            i += 1
        
        
    start       = raw_input('minimum number of chars:')
    end         = raw_input('maximum number of chars:')

    if not start.isdigit() or not end.isdigit():
        print 'Number of characters must be a numberic (integer) value!'
        return None
    else:
        start   = int(start)
        end     = int(end)
        return Fuzzer(fuzz_set, start, end, None)
