#!/usr/bin/env python

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
        for width in range(self.start, self.end + 1):
            self._recurse(width, 0, "")
        return self.password
        
    def _recurse(self, width, position, base):
        for char in self.fuzz_set[position]:
            if (position < width - 1):
                if self._recurse(width, position + 1, '%s%s' % (base, char)):
                    return True
            else:
                print 'trying password: ' + '%s%s' % (base, char)
                if self.target.trypass('%s%s' % (base, char)):
                    self.password = '%s%s' % (base, char)
                    return True

