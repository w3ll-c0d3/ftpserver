from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

PORT = 2121 # Ftp port
USER = "admin"
PASSWORD = "admin"

# The directory that is going to be exposed
FTP_DIRECTORY = "/home"

def main():
    authorizer = DummyAuthorizer()

    # anonymous user
    authorizer.add_user(USER, PASSWORD, FTP_DIRECTORY, perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())

    handler = FTPHandler
    handler.authorizer = authorizer

    handler.passive_ports = range(60000, 65535)

    # String returned when client connects 
    handler.banner = "pyftpd.ib based ftpd ready."
    
    address = ('', PORT)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

if __name__ == '__main__':
    main()


