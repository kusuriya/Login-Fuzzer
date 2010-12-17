#!/usr/bin/env python
"""
Code to test SSH connections.
"""

import datetime
import paramiko
import pdb
import sys
import time
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
        self.conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def set_target(self, target ):
        """
        """
        hostname = target[0]
        username = target[1]
        
        self.user    = username
        self.host    = hostname

    def trypass(self, passwd):
        if not self.test_pass(passwd):
            while "Error reading SSH protocol banner" == self.err_str:
                print 'Sleeping for SSH timeout...'
                time.sleep(5)
                if not self.test_pass(passwd): return False
                else: return True
            return False
        else:
            return True
    
    def test_pass(self, passwd):
        self.clear_error()
        ret_val         = False
        
        try:
            self.conn.connect(self.host, username = self.user, password = passwd,
                         timeout = 1)
        except paramiko.AuthenticationException, e:
            self.err_str == str(e)
            self.err(str(datetime.datetime.now()))
            self.err(' - %s@%s using %s: ' % (self.user, self.host, passwd))
            self.err('bad password!\n\tError message: ' + str(e) + '\n')
            self.exception_type = paramiko.AuthenticationException
            ret_val = False
        except paramiko.BadHostKeyException, e:
            self.err_str == str(e)
            self.err(str(datetime.datetime.now()))
            self.err(' - %s@%s: ' % (self.user, self.host))
            self.err('bad host key!\n\tError message: ' + str(e) + '\n')
            self.exception_type = paramiko.BadHostKeyException
            ret_val = False
        except paramiko.SSHException, e:
            self.err_str == str(e)
            self.err(str(datetime.datetime.now()))
            self.err(' - %s@%s: ' % (self.user, self.host))
            self.err('SSH exception!\n\tError message: ' + str(e) + '\n')
            self.exception_type = paramiko.SSHException
            ret_val = False
        except error, e:
            self.err_str == str(e)
            self.err(str(datetime.datetime.now()))
            self.err(' - %s@%s: ' % (self.user, self.host))
            self.err('bad host key!\n\tError message: ' + str(e) + '\n')
            self.exception_type = socket.self.error
            ret_val = False
        except:
            self.err('unknown error!\n')
            self.exception_type = 'GENERIC EXCEPTION'
            ret_val = False
        else:
            (stdin, stdout, stderr)     = self.conn.exec_command('whoami')
            whoami                      = stdout.read().strip()
            if not whoami == self.user:
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
        self.err_str        = None
        self.exception_type = None
        return True
    
    def reset_client(self):
        self.conn.close()
        self.conn     = paramiko.SSHClient()
        self.conn.load_system_host_keys()
        self.conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

