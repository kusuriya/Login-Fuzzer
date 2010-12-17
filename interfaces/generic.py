#!/usr/bin/env python
"""
Sample interface class showing the functions that must be implemented and the
required documentation.
"""

class Generic( ):
    target          = None
    
    def __init__(self, target):
        """
        The constructor should take a single parameter target. The format of
        target should be specified in self._targetspec()
        """
        self.set_target(target)
        
    def set_target(self, target):
        """
        Method should take a single parameter called target and feed that to
        the rest of the interface to set up a target.
        """
        self.target = target
    
    def trypass(self, password):
        """
        In the event the password is the correct password, the trypass( )
        method must return True. Otherwise, it must return False.
        """
        
        if password == "PASSWORD MATCHES":
            return True
        else:
            return False
    
    def _targetspec(self):
        """
        TARGETSPEC:
            Empty function whose comment describes the format that the
            set_target( ) method should take. This block describes whether
            target is a simple string, a tuple, or whatever else.
            
            Example:
                Generic(target = 'EXAMPLE_TARGET')
        """
        pass