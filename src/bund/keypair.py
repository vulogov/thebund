##
## Generate and manipulate RSA keypair
##
import os
import socket
import posixpath
import rsa

class KeyPair:
    def __init__(self, name=socket.gethostname(), path=None):
        self.KEYSIZE = 1024
        self.state   = False
        self.name    = name
        if not self.load_keys(name, path):
            self.generate_keys(name, path)
    def load_keys(sedf, name, path):
        if path == None:
            return False
        pub = "%s/%s.pub"%(path, name)
        pri = "%s/%s.key"%(path, name)
        if not posixpath.exists(pub) or not posixpath.exists(pri):
            return False
        try:
            with open(pri) as f_pri:
                self.key = rsa.PrivateKey.load_pkcs1(f_pri.read())
            with open(pub) as f_pub:
                self.pub = rsa.PublicKey.load_pkcs1(f_pub.read())
        except:
            return False
        self.state = True
        return True
    def generate_keys(self, name, path):
        pub = "%s/%s.pub"%(path, name)
        pri = "%s/%s.key"%(path, name)
        self.state  = False
        try:
            self.pub, self.key = rsa.newkeys(self.KEYSIZE)
            if path != None:
                with open(pri, mode='wb') as f_pri:
                    f_pri.write(self.key.save_pkcs1())
                with open(pub, mode='wb') as f_pub:
                    f_pub.write(self.pub.save_pkcs1())
        except:
            return False
        self.state = True
        return True
    def exportPRI(self):
        if not self.state:
            return None
        return self.key.save_pkcs1().decode('ascii')
    def exportPUB(self):
        if not self.state:
            return None
        return self.pub.save_pkcs1().decode('ascii')
    def importPRI(self, data):
        self.key = rsa.PrivateKey.load_pkcs1(data)
    def importPUB(self, data):
        self.pub = rsa.PublicKey.load_pkcs1(data)




if __name__ == '__main__':
    k = KeyPair()
