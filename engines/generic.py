#!/usr/bin/env python
"""
Template engine.
"""

class Generic( ):

    target      = None
    start       = None
    end         = None

    def __init__(self, target, start, end):
        """
        The constructor should take an interface target and the
        minimum (start) and maximum (end) number of characters
        in the password. For engines that only use a fixed
        length, end may be omitted in the parameters but the
        constructor should set self.end = self.start.
        """
        pass

    def crack(self):
        """
        Crack should take no arguments and will return the password
        if one was found or None if the password could not be 
        determined.
        """
        password = None

        # call the authentication testing code here, ex.
        # while self.generate_auths( ): pass

        return password

    def set_target(self, target):
        """
        set_target method allows reusing the engine instance across 
        multiple targets. An example use would be:

        for hosts in host_list:
            self.set_target(host)
            target.trypass(password)

        # i.e. to test the same password across multiple targets

        """

        self.target = target

    # end of Generic class
    
def selector( ):
    """
    The selector function provides an interactive way to set up an
    instance of an engine.
    """

    start   = None
    end     = None
    target  = None
    
    start   = raw_input('Minimum number of chars in password:')
    end     = raw_input('Maximum number of chars in password:')

    if not start.isalpha() or not end.isdigit():
        print 'Number of chars must be a numeric value!'
        return None
    else:
        start   = int(start)
        end     = int(end)
        return Generic(target, start, end)

