#!/usr/bin/env python

class echo( ):
    target      = None
    def __init__(self, target, dump = False):
        self.set_target(target)
        
    def set_target(self, target):
        self.target = target
        
    def trypass(self, password):
        if dump: print "trying password:", password,
        if password == self.target:
            if debug: print "\t[ MATCH ]"
            
            print "match with password:", password,
            return True
        else:
            if debug: print "\t[ FAILED! ]"
            return False
    
    def _targetspec(self):
        """
        TARGETSPEC:
            target should be in the form of a string that is the target
            password.
            
            Example:
                echo(target="pAsSwOrD")
        """
        
