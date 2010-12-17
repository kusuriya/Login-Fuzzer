#!/usr/bin/env python

class echo( ):
    target      = None
    def __init__(self, target):
        self.set_target(target)
        
    def set_target(self, target):
        self.target = target
        
    def trypass(self, password):
        #print "trying password:", password,
        if password == self.target:
            print "trying password:", password,
            print "\t[ MATCH ]"
            return True
        else:
            #print "\t[ FAILED! ]"
            return False
    
    def _targetspec(self):
        """
        TARGETSPEC:
            target should be in the form of a string that is the target
            password.
            
            Example:
                echo(target="pAsSwOrD")
        """
        
    
    
