#!/usr/bin/env python

import datetime
import sys
from ..interfaces import ssh


def Bruteforcer( ):
    """
    Brute force engine.
    """
    alphabet        = None
    host            = None
    user            = None
    interface       = None
    target          = None
    
    err             = sys.stderr.write
    
    
    def set_alphabet(self, alphabet_str):
        self.alphabet     = [ ]
        self.alphabet_set = set(alphabet_str).intersection(set(alphabet_str))
        for i in range(len(alphabet_set)):
            self.alphabet.append(ord(alphabet_set.pop()))
        self.alphabet     = sorted(self.alphabet)
    
    def generate_passwords(self, start = 1, end = 16):
        for width in range(start, end + 1):
            self._recurse(width, 0, "")
    
    def _recurse(self, width, position, base_str):
        #current position
        for char in alphabet:
            if (position < width - 1):
                test_pass[position] = char
                self._recurse(width, position + 1, test_pass)
            if not test_password(host, user, ''.join(test_pass)):
                if not exception_type == paramiko.AuthenticationException:
                    err('ssh error!')
                    sys.exit(2)
    
    def crack(self, start, end, alphabet_str = None):
        if alphabet_str:
            set_alphabet(alphabet_str)
        
        self.generate_passwords(start, end)

    def set_target(self, host, user):
        self.target  = ssh()