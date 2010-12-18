#!/usr/bin/env python

class echo( ):
    target      = None
    debug       = None
    def __init__(self, target, debug = False):
        self.set_target(target)
        self.debug = debug
        
    def set_target(self, target):
        self.target = target
        
    def trypass(self, password):
        if self.debug: print "trying password:", password,
        if password == self.target:
            if self.debug: print "\t[ MATCH ]"
            
            print "match with password:", password,
            return True
        else:
            if self.debug: print "\t[ FAILED! ]"
            return False
    
    def _targetspec(self):
        """
        TARGETSPEC:
            target should be in the form of a string that is the target
            password.
            
            Example:
                echo(target="pAsSwOrD")
        """
        
