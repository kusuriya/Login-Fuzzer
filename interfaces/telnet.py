#!/usr/bin/env python
"""
telnet interface
"""

class telnet( ):
    target      = None
    host        = None
    user        = None
    
    def __init__(self, target):
        self.target = telnetlib.Telnet()

    def set_target(self, target):
        self.host    = target[0]
        self.user    = target[1]
    
    def _targetspec(self):
        """
        TARGETSPEC:
            target should a tuple of two strings: the hostname of the target
            and the user to attempt a login as.
            
            Example:
                telnet(('localhost', 'root'))
        """
        pass

    def reconnect(self):
        self.target.close()
        self.target.open(self.host)

    def trypass(self, password):
        self.reconnect()
        self.target.read_until("login: ")
        self.target.write(self.user + "\n")

        self.target.read_until("Password: ")
        self.target.write(password + "\n")
        response    = self.target.read_all()

        self.target.write("whoami\nexit\n")
        response    = self.target.read_all()
    