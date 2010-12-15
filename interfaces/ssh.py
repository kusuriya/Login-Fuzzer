#!/usr/bin/env python
"""
Code to test SSH connections.
"""

import datetime
import paramiko
import sys
from socket import error

class ssh( ):
    
    err             = sys.stderr.write
    exception_type  = None
    host            = None
    user            = None
    conn            = None
    
    def __init__( self, hostname, username ):
        self.set_target(hostname, username)
        self.conn     = paramiko.SSHClient()
        self.conn.load_system_host_keys()
    
    def test_pass(self, passwd):
        self.clear_error()
        
        ret_val         = False
    
        try:
            conn.connect(self.host, username = self.user, password = passwd,
                         timeout = 1)
        except paramiko.AuthenticationException:
            err(str(datetime.datetime.now()))
            err(' - %s@%s using %s: ' % (host, user, passwd))
            err('bad password!\n')
            self.exception_type = paramiko.AuthenticationException
            ret_val = False
        except paramiko.BadHostKeyException:
            err(str(datetime.datetime.now()))
            err(' - %s@%s: ' % (host, user))
            err('bad host key!\n')
            self.exception_type = paramiko.BadHostKeyException
            ret_val = False
        except paramiko.SSHException:
            err(str(datetime.datetime.now()))
            err(' - %s@%s: ' % (host, user))
            err('SSH exception!\n')
            self.exception_type = paramiko.SSHException
            ret_val = False
        except socket.error:
            err(str(datetime.datetime.now()))
            err(' - %s@%s: ' % (host, user))
            err('bad host key!\n')
            self.exception_type = socket.error
            ret_val = False
        else:
            (stdin, stdout, stderr)     = self.conn.exec_command('whoami')
            whoami                      = stdout.read().strip()
            if not whoami == user:
                err('$(whoami) doesn\'t match user (expected %s, got %s)\n' %
                    (user, whoami))
                ret_val = False
            else:
                err(str(datetime.datetime.now()))
                err(' - %s@%s using %s: ' % (host, user, passwd))
                err('successful login!\n')
                ret_val = True
            self.conn.close()
        finally:
            return ret_val
    
    
    def clear_error(self):
        """
        Reset the global exception type variable.
        """
        global err_str
        err_str     = None
        
        return True
    
    
    def set_target(self, hostname, username):
        """
        """
        global host
        global user
        
        user    = username
        host    = hostname

