#!/usr/bin/env python
"""
Code to test SSH connections.
"""

import datetime
import paramiko
import pdb
import sys
from socket import error

class ssh( ):
    
    err             = sys.stderr.write
    exception_type  = None
    host            = None
    user            = None
    conn            = None
    err_str         = None
    
    def __init__( self, target ):
        self.set_target(target)
        self.conn     = paramiko.SSHClient()
        self.conn.load_system_host_keys()

    def set_target(self, target ):
        """
        """
        hostname = target[0]
        username = target[1]
        
        self.user    = username
        self.host    = hostname

    
    def trypass(self, passwd):
        ret_val         = False
    
        try:
            self.conn.connect(self.host, username = self.user, password = passwd,
                         timeout = 1)
        except paramiko.AuthenticationException:
            self.err(str(datetime.datetime.now()))
            self.err(' - %s@%s using %s: ' % (self.user, self.host, passwd))
            self.err('bad password!\n')
            self.exception_type = paramiko.AuthenticationException
            ret_val = False
        except paramiko.BadHostKeyException:
            self.err(str(datetime.datetime.now()))
            self.err(' - %s@%s: ' % (self.user, self.host))
            self.err('bad host key!\n')
            self.exception_type = paramiko.BadHostKeyException
            ret_val = False
        except paramiko.SSHException:
            self.err(str(datetime.datetime.now()))
            self.err(' - %s@%s: ' % (self.user, self.host))
            self.err('SSH exception!\n')
            self.exception_type = paramiko.SSHException
            ret_val = False
        except error:
            self.err(str(datetime.datetime.now()))
            self.err(' - %s@%s: ' % (self.user, self.host))
            self.err('bad host key!\n')
            self.exception_type = socket.self.error
            ret_val = False
        except:
            self.err('unknown error!\n')
            self.exception_type = 'GENERIC EXCEPTION'
            ret_val = False
        else:
            (stdin, stdout, stdself.err)     = self.conn.exec_command('whoami')
            whoami                      = stdout.read().strip()
            if not whoami == user:
                self.err('$(whoami) doesn\'t match user (expected %s, got %s)\n' %
                    (user, whoami))
                ret_val = False
            else:
                self.err(str(datetime.datetime.now()))
                self.err(' - %s@%s using %s: ' % (self.user, self.host, passwd))
                self.err('successful login!\n')
                ret_val = True
            self.conn.close()
        return ret_val
    
    def _targetspec(self):
        """
        TARGETSPEC:
            target is a tuple in the form (host, username).
            
            Example:
                ssh(target = ('192.168.1.1', 'root'))
                ssh(target = ('foo.megacorp.com', 'joeuser'))
        """
        pass
    
    def clear_error(self):
        """
        Reset the global exception type variable.
        """
        self.err_str     = None
        
        return True
    
    

