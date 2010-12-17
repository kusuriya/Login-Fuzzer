#!/usr/bin/env python

class echo( ):
    target      = None
    def __init__(self, target):
        self.set_target(target)
        
    def set_target(self, target):
        self.target = target
        
    def trypass(self, password):
        print "trying password:", password,
        if password == target:
            print "\t[ MATCH ]"
            return True
        else:
            print "\t[ FAILED! ]"
            return False
        
    
    
